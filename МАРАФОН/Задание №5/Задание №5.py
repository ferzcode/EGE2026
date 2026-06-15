a = []
for N in range(1, 1000):
    b = bin(N)[2:]

    summa = b.count('1')
    ost = summa % 2
    b = b + str(ost)

    summa = b.count('1')
    ost = summa % 2
    b = b + str(ost)

    R = int(b, 2)
    if R > 253:
        a.append(N)
print(min(a))

