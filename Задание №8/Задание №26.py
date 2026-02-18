from itertools import product
nomer = 0
for x in product(sorted('МАКС'), repeat=6):
    s = ''.join(x)

    nomer += 1

    if s.count('С') == 0 and s.count('М') == 0 and 'КК' not in s:
        print(nomer)