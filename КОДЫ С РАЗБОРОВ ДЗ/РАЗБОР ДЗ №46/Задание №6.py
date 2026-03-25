a = [int(x) for x in open('Задание №6.txt')]
otvet = []

for i in range(0, len(a) - 2):
    if ((str(a[i]).count('0') == 0) + (str(a[i + 1]).count('0') == 0) + (str(a[i + 2]).count('0') == 0)) >= 2:
        if (a[i] + a[i + 1] + a[i + 2]) < max(a) / 2:
            otvet.append(a[i] + a[i + 1] + a[i + 2])

print(len(otvet))
print(max(otvet))