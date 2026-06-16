c = 0

for stroka in open('9_27764.csv'):
    s = [int(x) for x in stroka.split()]

    if len(s) == len(set(s)):
        if 2 * (max(s) + min(s)) == (sum(s) - min(s) - max(s)):
            c += 1
print(c)