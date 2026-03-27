a = [int(x) for x in open('Задание №10.txt')]
otvet = []

maxtr = max([x for x in a if 100 <= abs(x) <= 999])

for i in range(len(a) - 1):
    if ((100 <= abs(a[i]) <= 999) + (100 <= abs(a[i + 1]) <= 999)) == 1 and (a[i] + a[i + 1]) <= maxtr:
        otvet.append(a[i] + a[i + 1])


print(len(otvet))
print(max(otvet))
