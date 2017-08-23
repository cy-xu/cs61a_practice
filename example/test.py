def fib(n):
    """Compute the nth Fibonacci number?"""
    pred, curr = 1, 0
    k = 0
    while k < n:
        print(curr)
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

print(fib(5))

def fiboNumberList(howMany):
    startNumber = 1
    nextNumber = 0
    countNumber = 0
    fiboList = []
    if howMany%1 != 0 or howMany < 0:
        print("Positive integer please!")
    else:
        while countNumber < howMany:
            fiboList.append(nextNumber)
            startNumber = nextNumber
            nextNumber = startNumber + nextNumber
            countNumber += 1
    return fiboList

print(fiboNumberList(0))
