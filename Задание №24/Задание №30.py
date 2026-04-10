f = open('Задание №6.txt').readline()
mx = 10000

for l in range(len(f)):
    for r in range(l + mx, l, - 1):
        s = f[l: r + 1]

        if s.count('W') < 250:
            break
        if s.count('W') == 250:
            mx = min(mx, len(s))

print(mx)