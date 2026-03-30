def f(s1, s2, m):
    if s1 + s2 > 46: return m % 2 == 0
    if m == 0: return 0

    if s1 > s2: h = [f(s1 + 1, s2, m - 1), f(s1 + 2,s2, m - 1), f(s1 + 3, s2, m - 1), f(s1, s2 * 2, m - 1)]
    elif s2 > s1: h = [f(s1, s2 + 1, m - 1), f(s1, s2 + 2, m - 1), f(s1, s2 + 3, m - 1), f(s1 * 2, s2, m - 1)]
    elif s1 == s2: h = [f(s1 + 1, s2, m - 1), f(s1 + 2,s2, m - 1), f(s1 + 3, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 + 2, m - 1), f(s1, s2 + 3, m - 1)]

    return any(h) if m % 2 != 0 else all(h)

# П В П В

print('19: ', min([s1 + s2 for s1 in range(1, 100) for s2 in range(1, 100) if f(s1, s2, 1)]))
print('20: ', [s2 for s2 in range(1, 42) if not f(5, s2, 1) and f(5, s2, 3)])
print('21: ', [s2 for s2 in range(1, 25) if not f(22, s2, 2) and f(22, s2, 4)])

