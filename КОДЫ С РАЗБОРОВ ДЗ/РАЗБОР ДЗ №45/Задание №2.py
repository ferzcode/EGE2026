a = [int(x) for x in open('Задание №2.txt')]
otvet = []

for i in range(len(a) - 1):
    if (a[i] * a[i + 1]) > 0 and abs(a[i] + a[i + 1]) % 7 == 0:
        otvet.append(a[i] * a[i + 1])

print(len(otvet))
print(min(otvet))
