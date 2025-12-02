# Петя составляет слова путём перестановки букв в слове ПРОСТО.
# Сколько он сможет составить слов, если запрещено ставить рядом две одинаковые буквы?

from itertools import permutations

otvet = set()
for x in permutations('ПРОСТО', r=6):
    s = ''.join(x)

    if 'ОО' not in s:
        otvet.add(s) # add - добавить в множество

print(len(otvet)) # len - узнать сколько слов в множестве