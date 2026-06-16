# f = open('24_28765.txt').readline()

# mx = 1
# for l in range(len(f)):
#     for r in range(l + mx, len(f)):
#         s = f[l:r + 1]
#
#         if s.count('BC') > 180:
#             break
#         else:
#             mx = max(mx, len(s))
# print(mx)

f = open('24_28765.txt').readline()
maxi = 0
s = ''

for l in range(len(f)):
    s += f[l]

    while s.count('BC') > 180:
        s = s[1:]

    maxi = max(maxi, len(s))
print(maxi)