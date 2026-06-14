# ¬ ОТРИЦАНИЕ NOT
# ∧ КОНЪЮНКЦИЯ AND
# ∨ ДИЗЪЮНКЦИЯ OR
# → ИМПЛИКАЦИЯ <=
# ≡ ЭКВИВАЛЕНТНОСТЬ ==


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(w <= (x == y))) and (z <= x)
                if F == 1:
                    print(x, y, z, w)
