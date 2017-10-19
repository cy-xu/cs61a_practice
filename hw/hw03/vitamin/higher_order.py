"""
def square_root(a):
    x = 1
    while x * x != a:
        print(x)
        x = square_root_update(x, a)
    return x

def cube_root(a):
    x = 1
    while x * x * x != a:
        print(x)
        x = cube_root_update(x, a)
    return x
"""

def trace1(fn):
    """Returns a version of fn that first prints before it's called.

    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling ', fn, 'on argument', x)
        return fn(x)
    return traced

def square_root_update(x, a):
    return (x + a/x) / 2

def cube_root_update(x, a):
    return (2*x + a/(x*x)) / 3

def improve(update, close, guess=1, max_update=100):
    k = 0
    while not close(guess) and k < max_update:
        k = k + 1
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def square_root(a):
    def update(x):
        return square_root_update(x, a)
    def close(x):
        return approx_eq(x * x, a)
    return improve(update, close)

def cube_root(a):
    return improve(lambda x: cube_root_update(x, a),
                   lambda x: approx_eq(x*x*x, a))

def average(x, y):
    return (x + y) / 2

def sqrt_update(x, a):
    return average(x, a/x)

@trace1
def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

def summation(n, term):
    total, k = 0, 1
    while k < n:
        total, k = total + term(k), k + 1
    return total

from operator import mul
def pi_term(k):
    return 8 / mul(4 * k - 3, 4 * k - 1)

def make_adder(n):
    """Return a function that takes one argument K and return K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        print(k)
        return k + n
    print(n)
    return adder

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def square(x):
    return x * x

def successor(x):
    return x + 1

def f(x):
    return -x

minus_successor = compose1(f, successor)

# Newton's Method （不会，跳过了）

# Curring

def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    while start <= end:
        print(f(start))
        start += 1

# Function Decorators

def trace1(fn):
    """Returns a version of fn that first prints before it's called.

    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling ', fn, 'on argument', x)
        return fn(x)
    return traced

def trace_wrapped(fn):
    def wrapped(x):
        print('-> ', fn, '(', x,')')
        return fn(x)
    return wrapped

@trace_wrapped
def square(x):
    return x * x

@classmethod
def triple(x):
    return 3 * x

#triple = trace_wrapped(triple)


#Suppose we want to compute the Fibonacci numbers using a recursive function1. The following function definition does the trick:

def memorize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper

@memorize
@trace_wrapped
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)
