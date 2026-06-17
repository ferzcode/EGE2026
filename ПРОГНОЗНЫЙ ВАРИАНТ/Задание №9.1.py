
c = 0
for stroka in open('Задание №9 В1.csv'):
    s = sorted([int(x) for x in stroka.split()])

    if max(s) < (sum(s) - max(s)):
        if (s[0] + s[3]) != (s[1] + s[2]):
            c += 1
print(c)

