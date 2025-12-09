for x in range(0, 42):
    num1 = 19 * 42 ** 4 + 5 * 42 ** 3 + 6 * 42 ** 2 + 9 * 42 ** 1 + x * 42 ** 0
    num2 = 1 * 42 ** 3 + x * 42 ** 2 + 18 * 42 ** 1 + 10 * 42 ** 0

    if (num1 + num2) % 155 == 0:
        print((num1 + num2) // 155)




# from string import *
# print(printable)