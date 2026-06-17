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
        summa = sum(map(int, t)) * 2
        # summa = t.count('2') * 2 + t.count('1') * 1
        t = t + tri(summa)

    R = int(t, 3)
    if R % 2 != 0 and R > 520:
        a.append(R)
print(min(a))
