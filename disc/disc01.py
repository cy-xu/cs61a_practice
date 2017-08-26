def wears_jacket(temp, raining):
     """
     >>> rain = False
     >>> wears_jacket(90, rain)
     False
     >>> wears_jacket(40, rain)
     True
     >>> wears_jacket(100, True)
     True
     """
     return temp < 60 or raining == True

def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow.
    >>> handle_overflow(35, 29)
    1 spot left in Section 2.
    >>> handle_overflow(20, 32)
    10 spots left in Section 1.
    >>> handle_overflow(35, 30)
    No space left in either section.
    """
    if s1 < 30 and s2 < 30:
        print("No overflow.")
    elif s1 < 30 and s2 > 30:
        print(str(30-s1) + " spots left in Section 1.")
    elif s1 > 30 and s2 < 30:
        print(str(30-s2) + " spot left in Section 2.")
    else:
        print("No space left in either section.")

"""two ways of finding prime number."""

from math import sqrt

def is_prime_slow(n):
    x = n // 2 + 1
    print(str(x))
    steps = 1
    while x > 1:
        if n % x == 0:
            return (False, steps)
        x = x - 1
        steps += 1
    return (True, steps)

def is_prime_quick(n):
    x = int(sqrt(n))
    print(str(x))
    steps = 1
    while x > 1:
        if n % x == 0:
            return (False, steps)
        x = x - 1
        steps += 1
    return (True, steps)

def keep_ints(cond, x):
    n = 1
    while n < x:
        if is_even(n):
            print(n)
        n += 1
    return

def is_even(x):
    return x % 2 == 0

keep_ints(is_even, 10)
