c = 0
for stroka in open('9_7697.txt'):
    s = [int(x) for x in stroka.split()]

    c18 = [x for x in s if x == 18] # len(c18) == 5

    # if (len(c18) == 5) or (sum(s) % 18 == 0):
    if ((len(c18) == 5) + (sum(s) % 18 == 0)) == 1:
        c += 1
print(c)