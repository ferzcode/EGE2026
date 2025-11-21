print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (y <= x) and (not w) and z
                if F == 1:
                    print(x, y, z, w)
                    