for k in range(1000, 10000):
    c1 = int(str(k)[0])
    c2 = int(str(k)[1])
    c3 = int(str(k)[2])
    c4 = int(str(k)[3])

    S = sum([c1, c2, c3, c4])
    M = max([c1, c2, c3, c4])
    N = min([c1, c2, c3, c4])
    P1 = S - M
    P2 = S - N

    L = str(P1) + str(P2)
    if L == '1318':
        print(k)
        break