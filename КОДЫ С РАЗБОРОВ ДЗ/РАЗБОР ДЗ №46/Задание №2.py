a = [int(x) for x in open('Задание №2.txt')]

max37= max([x for x in a if 10000 <= abs(x) <= 99999 and abs(x) % 100 == 37])
otvet = []

for i in range(0, len(a) - 1):
    if ((10000 <= abs(a[i]) <= 99999) + (10000 <= abs(a[i + 1]) <= 99999)) == 1:
        if (a[i] + a[i + 1]) ** 2 > max37 ** 2:
            otvet.append(a[i] + a[i + 1])


print(len(otvet))
print(max(otvet))