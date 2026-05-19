a = [int(x) for x in open('17_23376.txt')]

otvet = []
max37 = max([x for x in a if abs(x) % 100 == 37 and 10000 <= abs(x) <= 99999])

for i in range(0, len(a) - 1):
    if ((10000 <= abs(a[i]) <= 99999) + (10000 <= abs(a[i + 1]) <= 99999)) == 1:
        if ((a[i] + a[i + 1]) ** 2) > max37 ** 2:
            otvet.append(a[i] + a[i + 1])
print(len(otvet))
print(max(otvet))