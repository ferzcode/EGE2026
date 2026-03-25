a = [int(x) for x in open('Задание №5.txt')]
otvet = []

min123 = min([x for x in a if abs(x) % 1000 == 123 and x > 0])

for i in range(0, len(a) - 1):
    if abs(a[i] - a[i + 1]) <= min123:
        otvet.append(abs(a[i] - a[i + 1]))

print(len(otvet))
print(max(otvet))


