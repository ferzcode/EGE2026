f = open('Задание №9.txt').readline()
k = 0
m = 0

for i in range(len(f)):
    if k == 0:
        if f[i] in 'KLMN':
            k = 1

    else:
        if (f[i - 1] == 'K' and f[i] == 'L') or \
                (f[i - 1] == 'L' and f[i] == 'M') or \
                (f[i - 1] == 'M' and f[i] == 'N') or \
                (f[i - 1] == 'N' and f[i] == 'K'):
            k += 1
        elif f[i] in 'KLMN':
            k = 1
        else:
            k = 0

    m = max(m, k)
print(m)            