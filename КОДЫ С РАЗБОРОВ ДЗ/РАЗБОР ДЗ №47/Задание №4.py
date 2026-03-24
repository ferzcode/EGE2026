f = open('Задание №4.txt').readline()
mx = 1

for l in range(len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]
        if s.count('Y') > 80:
            break
        if s.count('Y') == 80 and s.count('2025') >= 90:
            mx = max(mx, len(s))

print(mx)
