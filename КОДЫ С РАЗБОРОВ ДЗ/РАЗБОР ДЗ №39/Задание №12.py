def tri(N):
    new = ''
    while N > 0:
        new += str(N % 3)
        N //= 3
    return new[::-1]


otvet = []
for N in range(1, 1000):
    triple = tri(N)

    if N % 3 == 0:
        triple = triple + triple[-2:]
    else:
        summa = sum(map(int, triple))
        summa = tri(summa)
        triple = triple + summa

    R = int(triple, 3)
    if R % 2 == 0 and R > 220:
        otvet.append(R)
print(min(otvet))
