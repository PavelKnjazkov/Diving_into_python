# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = {"Сергей": ("одежда", "молоток", "еда", "палатка"), "Борис": ("одежда", "мангал", "еда", "компас"),
        "Олег": ("одежда", "посуда", "пила", "топор")}

same_things = None
for item in hike:
    if item == list(hike.keys())[0]:
        same_things = set(hike[item])
    else:
        same_things = same_things & set(hike[item])
print(f'Вещи которые взяли все: {same_things}')

one_things = None
other_things = {1, 2}
other_things.clear()
unique_things = {1, 2}
unique_things.clear()
for i in hike:
    for j in hike:
        if i == j:
            one_things = set(hike[j])
        else:
            other_things |= set(hike[j])
    unique_things = unique_things | (one_things - other_things)
    other_things.clear()
print(f'Уникальные вещи: {unique_things}')

one_things = None
other_things = {1, 2}
other_things.clear()
not_things = {1, 2}
not_things.clear()
for i in hike:
    for j in hike:
        if i == j:
            one_things = set(hike[j])
        else:
            if other_things == set():
                other_things = set(hike[j])
            else:
                other_things &= set(hike[j])
    not_things = other_things - one_things
    if not_things != set():
        print(f'У {i} нет {not_things}, которую взяли все')
    other_things.clear()