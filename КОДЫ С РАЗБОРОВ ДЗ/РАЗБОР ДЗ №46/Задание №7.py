a = [int(x) for x in open('Задание №7.txt')]
otvet = []

max3 = max([x for x in a if abs(x) % 10 == 3 and 100 <= abs(x) <= 999])

for i in range(0, len(a) - 2):
    if (abs(a[i]) % 10 == 3 and 100 <= abs(a[i]) <= 999) or (abs(a[i + 1]) % 10 == 3 and 100 <= abs(a[i + 1]) <= 999) or (abs(a[i + 2]) % 10 == 3 and 100 <= abs(a[i + 2]) <= 999):
        if (a[i] + a[i + 1] + a[i + 2]) < max3:
            otvet.append(a[i] + a[i + 1] + a[i + 2])

print(len(otvet))
print(max(otvet))