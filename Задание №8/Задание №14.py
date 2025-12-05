# Сколько существует семеричных пятизначных чисел,
# содержащих в своей записи ровно одну цифру
# 6 и не содержащих идущих подряд одинаковых цифр?


from itertools import product

c = 0
for x in product('0123456', repeat=5):
    s = ''.join(x)

    # 00 11 22 33 44 55 66
    if s[0] != '0' and s.count('6') == 1 and '00' not in s and '11' not in s and '22' not in s and '33' not in s and '44' not in s and '55' not in s and '66' not in s:
        c = c + 1
print(c)