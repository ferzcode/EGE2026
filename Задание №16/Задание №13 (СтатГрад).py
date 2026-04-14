from sys import *
from fractions import *
from threading import *

setrecursionlimit(10 ** 9)
stack_size(250 * 1024 * 1024)

def f(n):
    if n >= 14: return n * f(n - 1)
    if n < 14: return 8 * g(n - 3)

def g(n):
    if n < 31: return 4
    if n >= 31: return (n // 2) * g(n - 2)


def main():
    res = Fraction(f(320726), g(641450))
    print(res)

Thread(target=main).start()