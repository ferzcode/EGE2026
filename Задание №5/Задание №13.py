def f(n):
    new = ''
    while n > 0:
        new = str(n % 3) + new
        n = n // 3
    return new


a = []
for n in range(1, 100000):
    b = f(n)

    if n % 3 == 0:
        b = b + b[:3]
    else:
        summa = (b.count('2') * 2 + b.count('1') * 1) * 5
        b = b + f(summa)
    
    R = int(b, 3)
    if R > 2500 and R % 2 != 0:
        a.append(R)
print(min(a))
