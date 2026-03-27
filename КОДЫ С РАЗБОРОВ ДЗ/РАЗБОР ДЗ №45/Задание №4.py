a = [int(x) for x in open('Задание №4.txt')]
otvet = []

max_nc = max([x for x in a if x % 2 != 0])

for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) * 2 > max_nc:
        otvet.append(a[i] + a[i + 1])

print(len(otvet))
print(min(otvet))
