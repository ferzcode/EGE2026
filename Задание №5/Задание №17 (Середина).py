def pyat(N):
    new = ''
    while N > 0:
        new = str(N % 5) + new
        N = N // 5
    return new

a = []
for N in range(1, 10000):
    p = pyat(N)

    if len(p) % 2 == 0:
        left = p[:len(p) // 2]
        right = p[len(p) // 2:]
        p = right + left
    else:
        p = p + str(N % 5)
        left = p[:len(p) // 2]
        right = p[len(p) // 2:]
        p = right + left

    R = int(p, 5)
    if R > 50:
        a.append(N)
print(min(a))
