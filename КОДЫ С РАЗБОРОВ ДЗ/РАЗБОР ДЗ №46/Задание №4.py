a = [int(x) for x in open('Задание №4.txt')]
otvet = []

max5 = max([x for x in a if x % 10 == 5])

for i in range(0, len(a) - 2):
    if ((10000 <= a[i] <= 99999) + (10000 <= a[i + 1] <= 99999) + (10000 <= a[i + 2] <= 99999)) == 2:
        if (a[i] + a[i + 1] + a[i + 2]) > max5:
            otvet.append(a[i] + a[i + 1] + a[i + 2])

print(len(otvet))
print(max(otvet))