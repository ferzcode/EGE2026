k111 = [x for x in range(222, 1_000_000, 222) if all(c not in '13579' for c in str(x))]
st5 = [x for x in range(1, 15)] # ПОКАТЕЛИ СТЕПЕНИ

otvet = []
for chislo1 in k111:
    for chislo2 in st5:
        if (chislo1 + 5 ** chislo2) > 1_000_000:
            otvet.append([chislo1 + 5 ** chislo2, chislo2])

for chislo, stepen in sorted(otvet)[:5]:
    print(chislo, stepen)