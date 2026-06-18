f = open('Задание №24.txt').readline()

for bukva in 'AEIOUY': f = f.replace(bukva, 'A')
c = ''
minix = 10000
for r in range(len(f)):
    c += f[r]

    if c[-1] == 'A':
        while c.count('20') >= 26:
            if c.count('20') == 26:
                minix = min(minix, len(c))
            c = c[1:]
        c = ''
print(minix)

# minix = 10000
# for l in range(len(f)):
#     for r in range(l + minix, l, -1):
#         if f[r] == 'A':
#             s = f[l: r + 1]
#
#             if s.count('20') >= 26 and s.count('A') == 1:
#                 minix = min(minix, len(s))
#             if s.count('20') < 26 or s.count('A') < 1: break
# print(minix)

f = open('24.txt').readline()

for n in 'OIYUE': f = f.replace(n, 'A')


c = ''
mx = 10000
for r in range(len(f)):
    c += f[r]

    if c[-1] == 'A':
        while c.count('20') > 26 or c.count('A') >= 1:
            c = c[1:]
            if c.count('20') == 26:

                mx = min(mx, len(c))

        c = ''

print(mx)
