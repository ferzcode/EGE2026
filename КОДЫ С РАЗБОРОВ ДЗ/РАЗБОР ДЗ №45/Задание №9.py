a = [int(x) for x in open('Задание №9.txt')]
otvet = []

maxdv = max([x for x in a if 10 <= abs(x) <= 99])

for i in range(len(a) - 1):
    if ((100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999)) >= 1 and abs(a[i] + a[i + 1]) % maxdv == 0:
        otvet.append(a[i] + a[i + 1])



print(len(otvet))
print(max(otvet))
