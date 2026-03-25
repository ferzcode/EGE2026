a = [int(x) for x in open('Задание №1.txt')]
max30 = max([x for x in a if abs(x) % 100 == 30])

otvet = []

for i in range(0, len(a) - 2):
    if ((1000 <= abs(a[i]) <= 9999) + (1000 <= abs(a[i + 1]) <= 9999) + (1000 <= abs(a[i + 2]) <= 9999)) == 0:
        if (a[i] + a[i + 1] + a[i + 2]) > max30:
            otvet.append(a[i] + a[i + 1] + a[i + 2])

print(len(otvet))
print(max(otvet))