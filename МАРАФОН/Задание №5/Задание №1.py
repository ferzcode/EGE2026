def tri(N):
    n = ''
    while N > 0:
        n = str(N % 3) + n
        N //= 3
    return n


a = []
for N in range(1, 1000):
    t = tri(N)

    if N % 3 == 0:
        t = t + t[-2:]
    else:
        summa = sum(map(int, t))
        summa = tri(summa)
        t = t + summa

    R = int(t, 3)
    if R > 220 and R % 2 == 0:
        a.append(R)
print(min(a))