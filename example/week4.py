from ucb import trace

def squre(x):
    return x * x

def sum_squares(x, y):
    return squre(x) + squre(y)

# Test-Driven Development
# domian, range, & behavior of a function

@trace
def gcd(m, n):
    """return the largest k that divides both m and n
    k, m, n are all positive integers.

    >>> gcd(12, 8)
    4
    >>> gcd(16 ,12)
    4
    >>> gcd(22,11)
    11
    >>> gcd(2,16)
    2
    >>> gcd(5,5)
    5
    """
    if m % n == 0:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m-n, n)

# Function Currying

def make_adder(n):
    return lambda k: n + k
# make_adder(2)(3) vs add(2,3)

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

from operator import add

m = curry2(add)
add_three = m(3)

# Implement trace

def trace1(fn):
    """return a version of fn that first print when it is called
    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling ', fn, 'on argument ', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x * x
