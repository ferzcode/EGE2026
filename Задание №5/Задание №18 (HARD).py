c = 0
for N in range(300, 401):
    s = str(N)
    pair = [int(s[0] + s[1]), int(s[1] + s[2]), int(s[0] + s[2]), int(s[2] + s[0]), int(s[2] + s[1]), int(s[1] + s[0])]

    maxi = max(pair)
    mini = min(pair)

    razn = maxi - mini
    if razn == 20:
        c += 1
print(c)