f = open('Задание №5.txt').readline().strip()
mx = 0

f = f.replace('++', '+ +')
f = f.replace('**', '* *')
f = f.replace('+*', '+ *')
f = f.replace('*+', '* +')

for c in f.split():
    while len(c) > 0 and c[0] in '+*': c = c[1:]
    while len(c) > 0 and c[-1] in '*+': c = c[:-1]

    if '+' in c or '*' in c:
        if eval(c) == 0:
            mx = max(mx, len(c))
print(mx)