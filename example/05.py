# nested funciton
def make_adder(n):
    def adder(k):
        return k + n
    return adder

""" Function Composition"""

def square(x):
    return x * x

def triple(x):
    return x * 3

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

squible = compose1(square, triple)
squible(5)

tripare = compose1(triple, square)
tripare(5)

squadder = compose1(square, make_adder(2))
squadder(3)
# equals to:
compose1(square, make_adder(2))(3)

""" Lambda expressions """
lambda_square = lambda x: x * x

lambda_square(4)

(lambda x: x * x)(3)
