otveti = []
for N in range(1, 100000):
    b = bin(N)[2:] # Двоичная запись

    summa = b.count('1')
    ostat = summa % 2
    b = b + str(ostat)

    summa = b.count('1')
    ostat = summa % 2
    b = b + str(ostat)

    R = int(b, 2) # Перевод в 10 с.с.
    if R > 253:
        otveti.append(N)
print(min(otveti))