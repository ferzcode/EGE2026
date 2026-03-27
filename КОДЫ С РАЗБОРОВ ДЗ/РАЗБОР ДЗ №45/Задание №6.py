a = [int(x) for x in open('Задание №6.txt')]
otvet = []

for i in range(len(a) - 1):
    if a[i] % 111 == min(a) or a[i + 1] % 111 == min(a):
        otvet.append(a[i] + a[i + 1])

print(len(otvet))
print(min(otvet))
