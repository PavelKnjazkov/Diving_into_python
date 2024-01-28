# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:  
#     from random import randint  
#     num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint 

LOWER_LIMIT = 0
UPPER_LIMIT = 1_000
NUMBER_OF_ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(1, NUMBER_OF_ATTEMPTS+1):
    user_num = int(input(f'Угадайте число (попытка {i}): '))
    if num > user_num:
        print('Надо больше')
    elif num < user_num:
        print('Надо меньше')
    else:
        print('Ура! Вы угадали')
        break
else:
    print(f'Попытки исчерпаны. Число было {num}')