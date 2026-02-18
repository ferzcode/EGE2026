def dev(N):
    new = ''
    while N > 0:
        new = str(N % 9) + new
        N = N // 9
    return new

a = []
for N in range(1, 10000):
    d = dev(N) # Строка

    if d[0] == '7':
        d = d.replace('6', '*')
        d = d.replace('3', '6')
        d = d.replace('*', '3')
        d = '34' + d

    else:
        d = '3' + d[1:] + '45'

    R = int(d, 9)
    #if R < 2876:
    #    a.append(R)
    if R == 2795:
        a.append(N)

print(max(a))