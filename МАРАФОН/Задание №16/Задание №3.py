from functools import *

@lru_cache(None)
def f(n):
    if n >= 2025: return n
    if n < 2025: return n * 2 + f(n + 2)

for n in range(3000, 0, -1):
    f(n)

print(f(82) - f(81))