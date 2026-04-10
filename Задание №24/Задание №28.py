f = open('Задание №4.txt').readline()

for c in '02468': f = f.replace(c, '2')

mx = 0
for l in range(len(f)):
    if f[l] == 'L':
        for r in range(l + mx, len(f)):
            s = f[l : r + 1]

            if s.count('2') > 14 or s.count('L') > 1: break
            if s.count('2') == 14 and s.count('L') == 1:
                mx = max(mx , len(s))
print(mx)