# a = []
# summa_min = 0
# summa_max = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#
#     a.append(num)
#
# a = sorted(a)
# summa_min = a[0] + a[1]
# summa_max = a[-2] + a[-1]
#
# print(summa_max)
# print(summa_min)

N = int(input())
maxi = 0
flag = 0
for i in range(N):
    speed = int(input())

    if speed > maxi:
        maxi = speed

    if speed < 30:
        flag = 1

print(maxi)
if flag == 0:
    print("NO")
else:
    print("YES")











