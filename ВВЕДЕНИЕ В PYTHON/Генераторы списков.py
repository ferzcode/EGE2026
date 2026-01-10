a = []
for i in range(1, 1000):
    a.append(i)

b = [i for i in range(1, 1000)]

spisok_kvadratov = [i ** 2 for i in range(1, 11)]

nechetnie = [i for i in spisok_kvadratov if i % 2 == 0]

def tri(N):
    new = ''
    while N > 0:
        new = str(N % 3) + new
        N = N // 3
    return new


dvoichki = [bin(i)[2:] for i in range(1, 11)]
# print(dvoichki)

troichki = [tri(i) for i in range(1, 11)]
# print(troichki)



spisok = [125, 125, 37, 61, 22, 22, 30]
povtorki = [i for i in spisok if spisok.count(i) == 2]
# print(povtorki)




# ПРОВЕРКА ЧТО ВСЕ ЧИСЛА РАЗЛИЧНЫ
# spisok = [1, 10, 10, 11, 19, 21]
# if len(spisok) == len(set(spisok)):
#     print("ДА!")
# else:
#     print('НЕТ')


# Есть ли в этом списке число, которое оканчивается на 2?

spisok = [65, -72, 85, 78, 91, 67]
if any(abs(i) % 10 == 2 for i in spisok):
    print('True')
else:
    print('False')
    
    # - 78 % 10 = (10 - 8) = 2
    # - 63 % 10 = (10 - 3) = 7
















