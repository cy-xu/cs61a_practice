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


def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    numberString = str(n)
    uniqueList = list()
    for aDigit in numberString:
        if aDigit not in uniqueList:
            uniqueList.append(aDigit)
    return len(uniqueList)
