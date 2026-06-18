from functools import *

@lru_cache(15000)
def f(n):
    if n < 10: return 1
    if n >= 10: return (n + 3) * f(n - 3)

for n in range(1, 248_000):
    f(n)

print((f(247_563) // 519 - 477 * f(247_560)) // f(247_557))