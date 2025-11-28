def f(n):
    new = ''
    while n > 0:
        new = str(n % 3) + new
        n = n // 3
    return new


a = []
for N in range(167, 100000):
    b = f(N)

    # 222211111 = 4 * 2 + 5 * 1 = 13
    summa = b.count('2') * 2 + b.count('1') * 1

    if summa % 9 == 0:
        b = b + '2'
    else:
        ostatok = summa % 9
        b = b + f(ostatok)

    R = int(b, 3)
    a.append(R)
print(min(a))