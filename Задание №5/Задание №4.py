otveti = []
for N in range(1, 100000):
    b = bin(N)[2:] # Двоичная запись

    if N % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'

    if b.count('1') % 3 == 0:
        b = '11' + b[2:]
    else:
        b = '10' + b[2:]

    R = int(b, 2) # Перевод в 10 с.с.
    if R >= 26:
        otveti.append(N)
print(min(otveti))
