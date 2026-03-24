f = open('Задание №2.txt').readline()
mx = 1

for i in '13579': f = f.replace(i, '1')

for l in range(len(f)):
    if f[l] == 'G':
        for r in range(l + mx, len(f)):
            s = f[l : r + 1]
            if s.count('1') > 45 and s.count('G') > 1:
                break
            if s.count('1') == 45 and s.count('G') == 1:
                mx = max(mx, len(s))

print(mx)
