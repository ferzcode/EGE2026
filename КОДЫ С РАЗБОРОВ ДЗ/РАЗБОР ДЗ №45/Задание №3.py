a = [int(x) for x in open('Задание №3.txt')]
otvet = []

for i in range(len(a) - 2):
    if a[i] < a[i + 1] < a[i + 2]:
        otvet.append(max(a[i], a[i + 1], a[i + 2]) - min(a[i], a[i + 1], a[i + 2]))

print(len(otvet))
print(min(otvet))
