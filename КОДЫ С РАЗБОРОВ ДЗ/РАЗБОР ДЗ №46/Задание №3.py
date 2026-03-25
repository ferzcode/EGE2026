a = [int(x) for x in open('Задание №3.txt')]
otvet = []

for i in range(0, len(a) - 2):
    otric = [x for x in [a[i], a[i + 1], a[i + 2]] if x < 0]
    poloj = [x for x in [a[i], a[i + 1], a[i + 2]] if x > 0]

    if abs(sum(otric)) <= sum(poloj):
        if abs(a[i] * a[i + 1] * a[i + 2]) % 10 == abs(max(a)) % 10:
            otvet.append(abs(a[i] * a[i + 1] * a[i + 2]))

print(len(otvet))
print(max(otvet))