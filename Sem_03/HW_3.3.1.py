# 3. Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

from random import randint

def variants_generator(thigs: list) -> dict:
     result_dict = {}    
     for thig in thigs:
        result_dict[thig] = randint(1, 5)
     return result_dict

list_things = ['ключи', 'кошелек', 'телефон', 'зажигалка']

items = variants_generator(list_things)

max_weight = 10
current_weight = 0
backpack = {} 

for item, weight in items.items():
    if current_weight + weight <= max_weight:
        backpack[item] = weight
        current_weight += weight
        
print(f'В рюкзак вместительностью {max_weight} кг вошли следующие вещи:')
for item, weight in backpack.items():
    print(f'- {item} - {weight} кг')