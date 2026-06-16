otvet = []
a = [int(x) for x in open('17_29349.txt')]

min123 = min([x for x in a if x > 0 and x % 123 == 0])

for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) < min123:
        otvet.append(a[i] + a[i + 1])
print(len(otvet), abs(max(otvet)))