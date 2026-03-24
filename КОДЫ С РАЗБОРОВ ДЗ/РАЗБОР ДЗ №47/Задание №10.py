f = open('Задание №10.txt').readline()
mx = 1

for c in '6789': f = f.replace(c, '6')
for b in 'ABC': f = f.replace(b, 'A')

for l in range(len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]

        if s.count('66') > 0 or s.count('AA') > 0:
            break
        if s.count('66') == 0 and s.count('AA') == 0:
            mx = max(mx, len(s))
print(mx)
