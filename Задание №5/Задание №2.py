otveti = []
for N in range(1, 100000):
    b = bin(N)[2:] # Двоичная запись

    if N % 4 == 0:
        b = b * 2
        # b = b + b
    else:
        b = b + b[::-1]
    R = int(b, 2) # Перевод в 10 с.с.
    if R >= 544:
        otveti.append(N)
print(min(otveti))