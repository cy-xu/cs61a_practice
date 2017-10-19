from random import randint

def make_averaged(fn, num_samples=1000):
    def average(*args):
        count = 0
        result = 0
        while count <= num_samples:
            result += fn(*args)
            count += 1
        print(result)
        return result / num_samples
    return average
    # END PROBLEM 7

def x(a, b):
    return randint(a, b)
randomoo = x(-1, 10)
make_averaged(randomoo, 10)