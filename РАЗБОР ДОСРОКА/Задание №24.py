f = open('24.txt').readline()
mx = 0

for l in range(0, len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]

        if s.count('BC') > 180: break
        if s.count('BC') <= 180: mx = max(mx, len(s))

print(mx)
