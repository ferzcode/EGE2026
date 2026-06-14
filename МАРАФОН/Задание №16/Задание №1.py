from functools import lru_cache

@lru_cache(None)
def f(n):
    return 2 * (g(n -3) + 8)

@lru_cache(None)
def g(n):
    if n < 10: return 2 * n
    if n >= 10: return g(n - 2) + 1

for n in range(0, 16000):
    g(n)
    f(n)

print(f(15548))

