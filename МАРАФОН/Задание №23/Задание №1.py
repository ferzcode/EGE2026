def f(x, y):
    if x == y: return 1
    elif x < y or x == 8: return 0
    else: return f(x - 1, y) + f(x - 4, y) + f(x // 2, y)

print(f(30, 12) * f(12, 4))