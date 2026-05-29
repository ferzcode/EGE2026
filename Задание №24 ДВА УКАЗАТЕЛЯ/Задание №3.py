f = open('Задание №3.txt').readline()

m = 0
c = ''
for r in range(len(f)):
    c += f[r]

    while c.count('C') > 2 and c.count('D') > 2:
        c = c[1:]

    m = max(m, len(c))
print(m)