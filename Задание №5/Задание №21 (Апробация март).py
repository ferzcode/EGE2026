a = []
for N in range(1, 1000):
    b = bin(N)[2:]

    if N % 3 == 0:
        b = b + b[-3:]
    else:
        ost = bin((N % 3) * 3)[2:]
        b = b + ost
    R = int(b, 2)
    if R == 127:
        a.append(N)
print(max(a))
