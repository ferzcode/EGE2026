def tri(N):
    n  = ''
    while N > 0:
        n = str(N % 3) + n
        N //= 3
    return n

a = []
for N in range(1, 1000):
    t = tri(N)
    if N % 3 == 0:
        t = '1' + t + '02'
    else:
        ost = (N % 3) * 5
        t = t + tri(ost)

    R = int(t, 3)
    if R >= 177:
        a.append(N)
print(min(a))