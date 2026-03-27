from re import fullmatch

for x in range(0, 10 ** 8, 153):
    if fullmatch(r'1[13579]*2[02468]3[13579]*45', str(x)):
        print(x, x // 153)