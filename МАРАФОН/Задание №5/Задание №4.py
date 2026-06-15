def tri(N):
    n = ''
    while N > 0:
        n = str(N % 3) + n
        N //= 3
    return n

a = []
for N in range(1, 1000):
    t = tri(N)

    if N % 3 != 0:
        t = '1' + t + t[-3:]
    else:
        summa = sum(map(int, t)) * 8
        t = t + tri(summa)

    R = int(t, 3)
    if R == 1205:
        a.append(R)
print(max(a))

