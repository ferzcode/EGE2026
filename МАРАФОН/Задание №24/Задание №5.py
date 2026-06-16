from re import *

f = open('24.txt').readline()

mx = 0
f = f.replace('++', '+ +')
f = f.replace('**', '* *')
f = f.replace('+*', '+ *')
f = f.replace('*+', '* +')

for c in f.split():
    while len(c) > 0 and c[0] in '+*': c = c[1:]
    while len(c) > 0 and c[-1] in '+*': c = c[:-1]

    if len(c) > 0:
        if eval(c) == 1:
            mx = max(len(c), mx)
print(mx)
