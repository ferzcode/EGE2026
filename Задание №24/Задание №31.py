f = open('Задание №7.txt').readline()
mx = 0

for l in range(len(f)):
    for r in range(l + mx, len(f)):
        s = f[l: r + 1]

        if 'XX' in s or s.count('ZUTYW') > 100:
            break

        if s.count('ZUTYW') == 100 and 'XX' not in s:
            mx = max(mx, len(s))

print(mx)