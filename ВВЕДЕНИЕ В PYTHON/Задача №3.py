time = 4000

chas = 4000 // 3600
ostatok = 4000 % 3600
minutes = ostatok // 60
secundes = ostatok  % 60


# 4000 - 3600
# 400

# 400 // 60 = 6 минут
# 400 % 60 = 40 cекунд


print(f'{time} секунд = {chas} час, {minutes} минут, {secundes} секунд')