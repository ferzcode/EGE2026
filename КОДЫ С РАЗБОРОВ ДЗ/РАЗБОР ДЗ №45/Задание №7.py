a = [int(x) for x in open('Задание №7.txt')]
otvet = []

min5 = min([x for x in a if 100 <= x <= 999 and x % 10 == 5])


for i in range(len(a) - 1):
    if ((100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999)) == 1 and (a[i] + a[i + 1]) % min5 == 0:
        otvet.append(a[i] + a[i + 1])


print(len(otvet))
print(min(otvet))
