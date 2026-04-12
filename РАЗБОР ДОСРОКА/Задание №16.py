# ПАМЯТЬ В ПОТОЛОК !!!

# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n < 10: return 3
#     if n >= 10: return (n + 4) * f(n - 5)
#
# for i in range(0, 258000):
#     f(i)
#
# print((f(257487) // 683 + f(257477) // 67) // f(257472))

# ПАМЯТЬ В ПОТОЛОК !!!
#
# f = [0] * 258000
# for n in range(0, 258000):
#     if n < 10: f[n] = 3
#     if n >= 10: f[n] = (n  + 4) * f[n - 5]
#
# print(((f[257487]) // 683 + f[257477] // 67) // f[257472])


from sys import *
from threading import *
from fractions import *

setrecursionlimit(10 ** 8)
stack_size(250 * 1024 * 1024)

def f(n):
    if n < 10: return 3
    if n >= 10: return (n + 4) * f(n - 5)


def main():
    # Fraction(a, b) = a / b

    res = Fraction(Fraction(f(257487), 683) + Fraction(f(257477), 67), f(257472))
    print(res)

Thread(target=main).start()