from itertools import product

c = 0
for x in product('01234567', repeat=5):
    s = ''.join(x)
    povt3 = [c for c in s if s.count(c) == 3]
    povt1 = [c for c in s if s.count(c) == 1]

#   

    if s[0] != '0' and ('000' in s or '111' in s or '222' in s or '333' in s or '444' in s or '555' in s or '666' in s or '777' in s):
        if len(povt3) == 3 and len(povt1) == 2:
            c += 1
print(c)