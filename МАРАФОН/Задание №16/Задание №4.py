from sys import *
from threading import *
from fractions import *

# from functools import *
#
# @lru_cache(15000)
# def f(n):
#     if n < 10: return 1
#     if n >= 10: return (n + 3) * f(n - 3)
#
# for n in range(250_000):
#     f(n)
#
# print((f(247563) // 519 - 477 * f(247560)) // f(247557))

from sys import *
from threading import *

setrecursionlimit(10 ** 9)
stack_size(250 * 1024 * 1024)
def f(n):
    if n < 10: return 1
    if n >= 10: return (n + 3) * f(n - 3)

def main():
    res = (f(247563) // 519 - 477 * f(247560)) // f(247557)
    print(res)

Thread(target=main).start()