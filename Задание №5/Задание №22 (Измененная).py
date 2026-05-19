for K in range(1000, 10000):
    stroka = str(K)

    S = int(stroka[0]) + int(stroka[1]) + int(stroka[2]) + int(stroka[3]) # ЧИСЛО
    M = max(int(stroka[0]), int(stroka[1]), int(stroka[2]), int(stroka[3])) # ЧИСЛО
    N = min(int(stroka[0]), int(stroka[1]), int(stroka[2]), int(stroka[3])) # ЧИСЛО

    P1 = S - M
    P2 = S - N

    pervoe = min(P1, P2)
    vtoroe = max(P1, P2)

    L = str(pervoe) + str(vtoroe)
    if L == '1318':
        print(K)
        break