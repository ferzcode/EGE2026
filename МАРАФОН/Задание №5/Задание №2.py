a = []
for N in range(1, 1000):
    b = bin(N)[2:]

    if N % 3 == 0:
        b = b + b[-3:]
    else:
        ost = (N % 3) * 3
        b = b + bin(ost)[2:]
    R = int(b, 2)

    if R == 127:
        a.append(N)
print(max(a))
