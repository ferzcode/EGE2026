f = open('Задание №1.txt').readline()

c = ''
m = 0
for r in range(len(f)):
    c += f[r]

    while c.count('Y') > 150:
        c = c[1:]

    m = max(m, len(c))
print(m)