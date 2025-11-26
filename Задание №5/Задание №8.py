otveti = []
for N in range(1, 100000):
    b = bin(N)[2:] # Двоичная запись

    if N % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'

    R = int(b, 2) # Перевод в 10 с.с.

    if R < 30:
        otveti.append(N)
print(max(otveti))