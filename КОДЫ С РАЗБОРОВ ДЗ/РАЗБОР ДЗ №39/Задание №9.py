otvet = []
for N in range(1, 1000):
    binary = bin(N)[2:]

    if N % 5 == 0:
        binary += '11'
    else:
        res = bin(N // 5)[2:]
        binary += res

    R = int(binary, 2)
    if R > 896 and N % 2 == 0:
        otvet.append(N)
print(min(otvet))