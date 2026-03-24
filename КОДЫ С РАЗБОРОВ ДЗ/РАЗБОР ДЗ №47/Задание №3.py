f = open('Задание №3.txt').readline()
mx = 1

for i in '02468': f = f.replace(i, '2')

for l in range(len(f)):
    if f[l] == '2':
        for r in range(l + mx, len(f)):
            s = f[l : r + 1]
            if s.count('F') > 76 and s.count('2') > 1:
                break
            if s.count('F') == 76 and s.count('2') == 1:
                mx = max(mx, len(s))

print(mx)
