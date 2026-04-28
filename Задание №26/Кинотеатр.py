f = open('Кинотеатр.txt')
N, M, K = map(int, f.readline().split())

min_ryad = [M + 1] * (K + 1)

for i in range(N):
    ryad, mesto = map(int, f.readline().split())

    min_ryad[mesto] = min(ryad, min_ryad[mesto])

max_ryad = 0
best_mesto = 0

for i in range(1, K):
    ryad = min(min_ryad[i], min_ryad[i + 1]) - 1

    if ryad > max_ryad:
        max_ryad = ryad
        best_mesto = i

    if ryad == 21028:
        print(i)