otveti = []
for N in range(4, 100000):
    b = bin(N)[2:] # Двоичная запись

    if N % 2 == 0:
        b = b + b[-2] + b[-1]
        # b = b + b[-2:]
    else:
        b = b + b[-3] + b[-2] + b[-1]
        # b = b + b[-3:]

    R = int(b, 2) # Перевод в 10 с.с.
    if R > 256:
        otveti.append(N)
print(min(otveti))