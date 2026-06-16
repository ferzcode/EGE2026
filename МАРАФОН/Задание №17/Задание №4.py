otvet = []
a = [int(x) for x in open('17_23276.txt')]
max25 = max([x for x in a if abs(x) % 100 == 25])

for i in range(len(a) - 2):
    if ((1000 <= abs(a[i]) <= 9999) + (1000 <= abs(a[i + 1]) <= 9999) + (1000 <= abs(a[i + 2]) <= 9999)) <= 2:
        if (a[i] + a[i + 1] + a[i + 2]) <= max25:
            otvet.append(a[i] + a[i + 1] + a[i + 2])
print(len(otvet), max(otvet))