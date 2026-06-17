# def check(A):
#     for dx in range(-300, 300):
#         for dy in range(-300, 300):
#             x = 486 + dx
#             y = 2430 + dy
#
#             f = (x * y < A) or (5 * x < y) or (486 <= x)
#             if f == 0:
#                 return 0
#
#     return 1
#
# for A in range(1176126, 0, -1):
#     if check(A) == 1:
#         print(A)

def check(A):
    for x in range(1, 78125):
        y = 78125 - 4 * x

        if x >= 1 and y >= 1:
            f = (78125 != y + 4 * x) or (A > x) and (A > y)
            if f == 0:
                return 0
    return 1

for A in range(79000, 0, -1):
    if check(A):
        print(A)