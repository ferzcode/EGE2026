from re import fullmatch

c = 0
for x in range(0, 10 ** 10, 10980):
    if fullmatch(r'20[13579][13579]22[02468]*', str(x)):
        print(x, x // 10980)
        c += 1

    if c == 5:
        break