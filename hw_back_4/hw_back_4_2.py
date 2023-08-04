# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}
def rev_kwargs(**kwargs) -> dict:
    my_dict = dict()
    for key, value in kwargs.items():
        my_dict[f'{value}'] = key
    return my_dict


print(rev_kwargs(res=1, reverse=[1, 2, 3], i=5))
