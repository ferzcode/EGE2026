from itertools import product

c = 0
nomer = 0
for x in product(sorted('ПОБЕДА'), repeat=6):
    s = ''.join(x)
    nomer += 1

    # all(s.count(x) == 1 for x in 'ПОБЕДА'):
    if nomer % 2 == 0 and s[0] == 'О' and len(set(s)) == len(s):
        print(nomer)