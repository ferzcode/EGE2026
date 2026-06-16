from math import*

# def f(x, d = 2):
#     for d in range(d, round(x ** 0.5) + 1):
#         if x % d == 0:
#             return [d] + f(x // d, d)
#     return [x]

def f(x):
    d = []
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    return d

c = 0
for x in range(31_991_737, 32_000_000):
    d = f(x)

    p = [i for i in d if i % 2 == 0 and str(i).count('7') == 1]

    flag = False
    m = []
    for i in range(len(p) - 1):
        if p[i] * p[i + 1] == x:
            flag = True
            m.append(max(p[i], p[i + 1]))

    if flag == True:
        print(x, max(m))
        c += 1

    if c == 6:
        break