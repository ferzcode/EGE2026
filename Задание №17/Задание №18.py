a = [int(x) for x in open('17_29971.txt')]

max33 = max([x for x in a if abs(x) % 100 == 33])

otvet = []
for i in range(0, len(a) - 2):
    if ((10 <= abs(a[i]) <= 99) + (10 <= abs(a[i + 1]) <= 99) + (10 <= abs(a[i + 2]) <= 99)) == 2:
        if ((a[i] + a[i + 1] + a[i + 2]) ** 2) < max33:
            otvet.append(a[i] + a[i + 1] + a[i + 2])

print(len(otvet))
print(max(otvet))