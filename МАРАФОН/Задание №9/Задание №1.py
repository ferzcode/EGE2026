c = 0
for stoka in open('9_29341.csv'):
    s = sorted([int(x) for x in stoka.split()])

    if max(s) < (sum(s) - max(s)):
        if s[0] + s[-1] != s[1] + s[2]:
            c += 1
print(c)
            