otveti = []
for N in range(1, 100000):
    b = bin(N)[2:] # Двоичная запись

    if N % 2 == 0:
        b = b.replace('1', '11')
    else:
        b = b.replace('0', '00')

    R = int(b, 2) # Перевод в 10 с.с.
    if R > 70:
        otveti.append(N)
print(min(otveti))
