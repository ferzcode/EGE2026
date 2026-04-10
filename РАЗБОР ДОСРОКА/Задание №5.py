a = []
for N in range(1, 1000):
    b = bin(N)[2:]

    ost = b.count('1') % 2
    b = b + str(ost)

    ost = b.count('1') % 2
    b = b + str(ost)

    R = int(b, 2)
    if R > 253:
        a.append(N)
print(min(a))

# Укажите минимальное N, при котором получается число ближайшее к 253