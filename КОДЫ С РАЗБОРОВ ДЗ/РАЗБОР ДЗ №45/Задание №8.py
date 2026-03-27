a = [int(x) for x in open('Задание №8.txt')]
otvet = []

maxdv = max([x for x in a if 10 <= x <= 99])

for i in range(len(a) - 1):
    if ((10 <= a[i] <= 99) + (10 <= a[i + 1] <= 99)) == 1 and (a[i] + a[i + 1]) % maxdv == 0:
        otvet.append(a[i] + a[i + 1])


print(len(otvet))
print(max(otvet))
