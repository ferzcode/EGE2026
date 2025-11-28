def f(n):
    new = ''
    while n > 0:
        new = str(n % 4) + new
        n = n // 4
    return new


a = []
for N in range(1, 100000):
    b = f(N)  # Четверичная запись
    if N % 4 == 0:
        b = b + b[-2:]
        # b = b + b[-2] + b[-1]
    else:
        ostatok = (N % 4) * 2
        b = b + f(ostatok)
    R = int(b, 4)

    if R < 261:
        a.append(N)
print(max(a))