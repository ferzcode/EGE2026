otveti = []
for N in range(1, 100000):
    b = bin(N)[2:] # Двоичная запись

    if N % 3 == 0:
        b = b + b[-3:]
        # b = b + b[-3] + b[-2] + b[-1]
    else:
        ostatok = (N % 3) * 3
        ostatok = bin(ostatok)[2:]
        b = b + ostatok

    R = int(b, 2) # Перевод в 10 с.с.
    if R >= 200:
        otveti.append(N)
print(min(otveti))
