c = 0

for stroka in open('Задание №3.txt'):
    s = [int(x) for x in stroka.split()]

    perv = s[0]
    posl = s[-1]
    s = sorted(s)
    if ((s.count(max(s)) == 1) + (perv != min(s) and perv != max(s) and posl != min(s) and posl != max(s)) + ((s[-1] * s[-2] * s[-3]) % min(s) == 0)) == 1:
        c += 1
print(c)
