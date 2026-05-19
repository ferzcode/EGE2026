from itertools import product

total = 0
for x in product('0123456789ABC', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') == 1:
        c = 0
        for i in range(0, len(s) - 1):
            if s[i] != s[i + 1]:
                c += 1

        if c == 4:
            total += 1
print(total)

