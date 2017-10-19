
def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

"""
def luhn_sum(n):
    if n < 10:
        return n
    else:
        double_digit, unchange_digit = 2 * (n // 10 % 10), n % 10
        if double_digit > 10:
            double_digit = double_digit % 10 + double_digit // 10
        sumall = double_digit + unchange_digit
        remain_digits = n // 100
        return luhn_sum(remain_digits) + sumall

def luhn_check(x):
    return luhn_sum(x) == 10 * (x % 10)

"""

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def cascade2(n):
    print(n)
    if n > 10:
        cascade2( n // 10)
        print(n)

"""
def inverse_cascade(n):
    grow(n)
    shrink(n)

def grow(n):
    if n < 10:
        print(n)
    else:
        grow(n//10)
        print(n)

def shrink(n):
    if n < 10:
        print(n)
    else:
        print(n//10)
        shrink(n//100)
"""

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

# tree structured

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# Exmaple: Counting Partitions (其实还没懂)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m