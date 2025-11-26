otveti = []
for N in range(1, 100000):
    b = bin(N)[2:] # Двоичная запись

    dlina = len(b)
    if dlina % 2 == 0:
        seredina = dlina // 2
        b = b[:seredina] + '1' + b[seredina:]

    R = int(b, 2) # Перевод в 10 с.с.
    if R >= 26:
        otveti.append(N)
print(min(otveti))