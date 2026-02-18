k113 = [x for x in range(113, 1_000_000, 113) if x % 2 != 0]
st3 = [x for x in range(1, 15)]

otvet = []
for chislo1 in k113:
    for chislo2 in st3: # ПОКАЗАТЕЛЬ СТЕПЕНИ
        if 100_000 <= (chislo1 + 3 ** chislo2) <= 1_000_000 and str(chislo1 + 3 ** chislo2).count('0') == 0:
            otvet.append([chislo1 + 3 ** chislo2, chislo2])

for chislo, stepen in sorted(otvet)[:5]:
    print(chislo, stepen)

print(sorted(otvet)[:5])