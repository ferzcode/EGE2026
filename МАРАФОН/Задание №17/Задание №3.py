otvet = []
a = [int(x) for x in open('17_23404.txt')]
min152 = abs(min([x for x in a if abs(x) % 1000 == 152]))


for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) < min152:
        otvet.append(abs(a[i]) + abs(a[i + 1]))
print(len(otvet), max(otvet))