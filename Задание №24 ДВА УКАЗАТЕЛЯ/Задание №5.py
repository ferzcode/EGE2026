f = open('Задание №5.txt').readline()

c = ''
m = 10000000

for a in 'AEIOUY':
    f = f.replace(a, 'A')

for r in range(len(f)):
    c += f[r]

    if c[-1] == 'A':
        while c.count('20') >= 26 or c.count('A') > 1:
            c = c[1:]

            if c.count('20') == 26 and c.count('A') == 1:
                m = min(m, len(c))
        c = ''
print(m)