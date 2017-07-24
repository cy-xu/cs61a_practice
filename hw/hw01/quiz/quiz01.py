def multiple(a, b):
# 最小公倍数
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    if a - b > 0:
        bigNum = a
        smallNum = b
    else:
        bigNum = b
        smallNum = a
    n = 1
    testNum = bigNum
    while testNum % smallNum != 0:
        testNum = bigNum * n
        n += 1
        print(testNum)
    return testNum

