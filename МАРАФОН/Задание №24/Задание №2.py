f = open('24_26549.txt').readline()

mx = 1
for l in range(len(f)):
    for r in range(l + mx, len(f)):
        s = f[l : r + 1]

        if s.count('2025') > 50: break

        if s.count('2025') == 50 and s.count('Y') >= 140 and s[-4:] == '2025':
            m = max(mx, len(s))
print(mx)