a = [int(x) for x in open('Задание №5.txt')]
otvet = []

for i in range(len(a) - 2):
    if abs(a[i] + a[i + 1] + a[i + 2]) % 2022 == 0 and (a[i] >= 0 or a[i + 1] >= 0 or a[i + 2] >= 0):
        otvet.append(a[i] + a[i + 1] + a[i + 2])

print(len(otvet))
print(max(otvet))
