# Задание №7
# 📌 Пользователь вводит число от 1 до 999. Используя операции с числами
#    сообщите что введено: цифра, двузначное число или трёхзначное число.
# 📌 Для цифры верните её квадрат, например 5 - 25
# 📌 Для двузначного числа произведение цифр, например 30 - 0
# 📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
# 📌 Если число не из диапазона, запросите новое число
# 📌 Откажитесь от магических чисел
# 📌 В коде должны быть один input и один print

MIN_NUMBER = 1
MAX_NUMBER = 999
SQUARE = 1
MULTIPLICATION = 2

while True:
    user_number_str = input(f'Введите число от {MIN_NUMBER} до {MAX_NUMBER}: ')
    if MIN_NUMBER <= int(user_number_str) <= MAX_NUMBER:
        break

if len(user_number_str) == SQUARE:
    result_value = f'Квадрат числа {user_number_str} = {int(user_number_str)**2}'
elif len(user_number_str) == MULTIPLICATION:
    result_value = f'Произведение цифр числа {user_number_str} = {int(user_number_str[0])*int(user_number_str[1])}'
else:
    new_number = ''
    new_number += user_number_str[2]
    new_number += user_number_str[1]
    new_number += user_number_str[0]
    result_value = f'Зеркальное отображение числа {user_number_str} = {new_number}'
print(result_value)