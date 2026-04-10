c = 0
for stroka in open('9.csv'):
    s = sorted([int(x) for x in stroka.split()])

    # мин поб поб макс

    if max(s) < (sum(s) - max(s)):
        if (s[0] + s[3]) != (s[1] + s[2]):
            c += 1
print(c)
