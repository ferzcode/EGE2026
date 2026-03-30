def f(s1, s2, m):
    if s1 + s2 > 60: return m % 2 == 0
    if m == 0: return 0

    if s1 > s2: h = [f(s1, s2 + 1, m - 1), f(s1, s2 + 2, m - 1), f(s1, s2 * 2, m - 1)]
    else: h = [f(s1 + 1, s2, m - 1), f(s1 + 2, s2, m - 1), f(s1 * 2, s2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)

# П В П В
print('19: ', [s2 for s2 in range(1, 53) if not f(8, s2, 1) and f(8, s2, 2)])
print('20: ', [s2 for s2 in range(1, 53) if not f(8, s2, 1) and f(8, s2, 3)])
print('21: ', [s2 for s2 in range(1, 53) if not f(8, s2, 2) and f(8, s2, 4)])



