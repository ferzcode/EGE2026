from math import ceil

def f(s, m):
    if s <= 23: return m % 2 == 0
    if m == 0: return 0

    h = [f(s - 3, m - 1), f(s - 5, m - 1), f(ceil(s / 2), m - 1)]
    return any(h) if m % 2 != 0 else all(h)

# 1 2 3 4
# П В П В

print('19: ', [s1 for s1 in range(24, 1000) if not f(s1, 1) and f(s1, 2)])
print('20: ', [s1 for s1 in range(24, 1000) if not f(s1, 1) and f(s1, 3)])
print('21: ', [s1 for s1 in range(24, 1000) if not f(s1, 2) and f(s1, 4)])