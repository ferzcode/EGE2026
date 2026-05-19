c = 0

for stroka in open('9_27764.csv'):
    s = [int(x) for x in stroka.split()]

    if len(s) == len(set(s)) and (max(s) + min(s)) * 2 == (sum(s) - max(s) - min(s)):
            c += 1
print(c)