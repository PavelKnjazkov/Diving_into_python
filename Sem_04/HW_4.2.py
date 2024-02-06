# 2. Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def key_params(**kwargs) -> dict:
    """
    Функция принимает ключи, а возвращает словарь, где ключ — значение
    переданного аргумента, а значение — имя аргумента. Если
    ключ не хешируем, использует его строковое представление.

    :param kwargs: именованные аргументы
    :return: словарь где все на оборот
    """
    return_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            return_dict[str(value)] = key
        else:
            return_dict[value] = key

    return return_dict


result = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(result)


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

# def create_dictionary(**kvargs):
#     '''Возвращает словарь, где ключ — значение переданного в функцию аргумента, а значение — имя аргумента'''

#     result_dict = {}
#     for values, key in kvargs.items():
#         result_dict[str(key)] = values
#     return result_dict    
    
# print(create_dictionary(first=100500, second='Ковер на стене', third=True))