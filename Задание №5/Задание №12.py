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
        b = b + b[-2:]
    else:
        ostatok = (n % 3) * 5
        b = b + f(ostatok)

    R = int(b, 3)
    if R > 150:
        a.append(R)
print(min(a))