f = open('Задание №2.txt').readline()

mx = 1
k = 1
for i in range(0, len(f) - 1):
    if f[i] in 'ABCDE':
        if f[i] != f[i + 1]:
            k = k + 1
            mx = max(mx, k)
        else:
            k = 1
    else:
        k = 1
print(mx)