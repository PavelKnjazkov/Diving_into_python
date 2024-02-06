# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

user_str = input('Введите строку текста: ')
user_dict = {}
for item in user_str:
    if not user_dict.get(item):
        user_dict[item] = 1
    else:
        user_dict[item] += 1
print(user_dict)

print('')