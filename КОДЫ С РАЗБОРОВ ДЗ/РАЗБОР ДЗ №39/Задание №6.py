c = 0

for stroka in open('Задание №6.txt'):
    s = [int(x) for x in stroka.split()]

    povt = [x for x in s if s.count(x) > 1]
    if s.count(min(s)) == 1 and len(povt) > 0:
        if (min(s) + max(s)) < sum(povt):
            c += 1
print(c)
