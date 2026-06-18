def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else:
        if str(x)[1] < str(x)[2]:
            return f(x + 1, y) + f(int(str(x)[0] + str(x)[2] + str(x)[1]), y)
        else:
            return f(x + 1, y)
print(f(101, 151))