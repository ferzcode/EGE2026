c = 0

for stroka in open('9_24347.csv'):
    s = [int(x) for x in stroka.split()]

    usl1 = s.count(max(s)) == 1
    usl2 = (s[0] != min(s) and s[0] != max(s) and s[-1] != min(s) and s[-1] != max(s))
    a = sorted(s)

    usl3 = (a[-1] * a[-2] * a[-3]) % min(s) == 0

    if ((usl1) + (usl2) + (usl3)) == 1:
        c += 1
print(c)