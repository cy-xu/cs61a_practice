"""Our first Python source file."""

from operator import floordiv, mod

def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """Return the absolute value of X."""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return 0

i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i

"""genenralizaion"""

from math import pi, sqrt

def area(r, shape_constant):
    assert r > 0, 'A length must be positive.'
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

"""example on Sum"""

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Summation of the first N seaquence numbers

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)


def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)
