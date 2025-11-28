def f(n):
    new = ''
    while n > 0:
        new = str(n % 3) + new
        n = n // 3
    return new


a = []
for n in range(1, 100000):
    b = f(n)

    summa = b.count('2') * 2 + b.count('1') * 1
    if summa % 3 == 0:
        b = b.replace('1', '*')
        b = b.replace('0', '1')
        b = b.replace('*', '0')

        b = '10' + b
    else:
        b = '22' + b[2:] + '101'

    R = int(b, 3)

    if R == 315:
        a.append(n)
print(min(a))

#     if R > 314:
#         a.append(R)
# print(min(a))