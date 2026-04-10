f = open('Задание №8.txt').readline()

mx = 0
for l in range(len(f)):
    if f[l] == 'T':
        for r in range(l, len(f)):
            s = f[l : r + 1]

            if 'X' in s: break
            if s.count('T') > 1: break

            if s[-1] == 'Z' and ''.join(sorted(s)) == s:
                mx = max(mx, len(s))
print(mx)


