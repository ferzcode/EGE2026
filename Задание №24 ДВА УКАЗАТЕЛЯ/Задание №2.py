f = open('Задание №2.txt').readline()

c = ''
m = 0

for r in range(len(f)):
    c += f[r]

    while c.count('.') > 5 or c.count('Y') > 0:
        c = c[1:]

    m = max(m, len(c))

print(m)