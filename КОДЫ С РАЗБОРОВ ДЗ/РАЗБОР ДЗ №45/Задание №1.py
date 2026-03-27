a = [int(x) for x in open('Задание №1.txt')]
otvet = []

for i in range(len(a) - 1):
    if abs(a[i] + a[i + 1]) % 3 == 0 and abs(a[i + 1] - a[i]) % 6 != 0 and abs(a[i] * a[i + 1]) % 10 == 8:
        otvet.append(a[i] + a[i + 1])

print(len(otvet))
print(max(otvet))
