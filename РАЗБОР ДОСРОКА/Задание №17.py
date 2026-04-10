a = [int(x) for x in open('17.txt')]

min23 = min([x for x in a if abs(x) % 23 == 0])
otvet = []
for i in range(len(a) - 1):
    if a[i] % min23 == 0 or a[i + 1] % min23 == 0:
        otvet.append(a[i] + a[i + 1])
print(len(otvet), max(otvet))
