f = open('Задание №3.txt').readline()
mx = 0

for l in range(len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]

        if s.count('ZX') > 320:
            break
        if s.count('ZX') <= 320:
            mx = max(mx, len(s))
print(mx)