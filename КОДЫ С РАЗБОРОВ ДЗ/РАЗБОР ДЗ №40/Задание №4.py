c = 0
for stroka in open('Задание №4.txt'):
    s = [int(x) for x in stroka.split()]

    if (all(x == 18 for x in s)) + (sum(s) % 18 == 0) >= 1:
        c += 1
print(c)
