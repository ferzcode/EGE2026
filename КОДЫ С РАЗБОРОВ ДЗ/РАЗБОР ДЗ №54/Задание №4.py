from re import fullmatch

for x in range(0, 10 ** 10, 9231):
    if fullmatch(r'[02468]*12[13579]4[13579]', str(x)):
        print(x, x // 9231)