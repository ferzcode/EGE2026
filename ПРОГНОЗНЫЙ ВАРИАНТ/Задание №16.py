# from sys import *
# from threading import *
#
# stack_size(100 * 1024 * 1024)
# setrecursionlimit(10 ** 9)
#
# def f(n):
#     if n < 10: return 1
#     if n >= 10: return (n + 3) * f(n - 3)
#
# def main():
#     res = (f(247563) // 519 - 477 * f(247560)) // f(247557)
#     print(res)
#
# Thread(target=main).start()

from functools import *

@lru_cache(15000)
def f(n):
    if n < 10: return 1
    if n >= 10: return (n + 3) * f(n - 3)

for n in range(1, 250_000):
    f(n)

print((f(247563) // 519 - 477 * f(247560)) // f(247557))