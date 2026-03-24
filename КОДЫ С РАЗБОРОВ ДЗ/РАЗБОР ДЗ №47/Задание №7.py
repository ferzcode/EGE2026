f = open('Задание №7.txt').readline()
mx = 1

for l in range(len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]

        if s.count('WWF') > 120 or s.count('WSFWW') > 0:
            break
        if s.count('WWF') <= 120 or s.count('WSFWW') == 0:
            mx = max(mx, len(s))
print(mx)