f = open('Задание №8.txt').readline()
mx = 1

for l in range(len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]

        if s.count('CD') > 160:
            break
        if s.count('CD') == 160:
            mx = max(mx, len(s))
print(mx)