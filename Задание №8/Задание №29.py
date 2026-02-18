from itertools import product

otvet = set()
for x in product(sorted('ДГШЯБЖ'), repeat=6):
    s = ''.join(x)

    if s.count('Я') == 1:
        otvet.add(s)
print(len(otvet))

# ДДДГШЯ
# ДДДГШЯ