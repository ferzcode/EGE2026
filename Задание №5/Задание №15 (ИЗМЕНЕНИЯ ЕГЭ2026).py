for K in range(1000, 10000):
    num = str(K)
    cifra1 = int(num[0])
    cifra2 = int(num[1])
    cifra3 = int(num[2])
    cifra4 = int(num[3])

    S = cifra1 + cifra2 + cifra3 + cifra4
    M = max(cifra1, cifra2, cifra3, cifra4)
    N = min(cifra1, cifra2, cifra3, cifra4)

    P1 = S - M
    P2 = S - N

    L = str(P1) + str(P2)
    if L == '1318':
        print(K)