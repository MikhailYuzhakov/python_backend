# функции - фрагмент кода, черный ящик
# Функция высшего порядка - такая функция, которая принимает фнукциб-лбъеккт как аргумент или возвращает
# функцию-объект в виде выходного значения. Например:
print(sum(range(10)))
# можно передать функцию как объект, но это плохой вариант
very_bad_programming_style = sum
print(very_bad_programming_style([1, 2, 3]))


#
# определение собственной функции
def my_func():
    pass  # зарезервированное слово ничего не делает


# при написании функции в круглых скобках - параметры, при вызове функции - аргументы
# в функции можно возвращать множество объектов кортежем return n, a, c, list
# если ничего не возвращать то ЯП верент автоматические None
def qudratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | str | None:
    d = b ** 2 - 4 * a
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return None


print(qudratic_equations(2, -3, -9))


# можно указать значения по умолчанию
def qudratic_equations1(a, b=0, c=0) -> tuple[float, float] | float | str | None:
    d = b ** 2 - 4 * a
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return None


print(qudratic_equations1(2))


# Изменяемые и неизменяемые аргументы
# неизменяемыей аргумент - при изменении внутри функции остаётся прежним вне функции
# при изменении внутри функции изменяется и за её пределами
# в питон аругменты передаются внутри функции по ссылке на объект
# изменяемый - передаем ссылку на объект и внутри массива изменяем внешний объект
# всё что хранится в куче с ссылка в хипе
def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }')
    return data


my_list = [2, 4, 6, 8]
print(f'In func {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')


# т.к. в качестве аргумента передаем ссылку, а в теле функции append элементы
# поэтому по ссылке будем добавлять в тот же список элементы
def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')


# Позиционные и ключевые параметры
# косая черта / и звездочка * разделяют позиционные и ключевые параметры
def func(positional_only_parameters, /, pos_of_keyword_parameters, *, keyword_only_parameter):
    pass


def kwd_only_arg(*, arg):
    """Пример только ключевой функции"""
    print(arg)


def standart_arg(arg):
    """Пример обычной функции"""
    print(arg)


standart_arg(42)  # позиционное значение здесь используется стандартный аргумент
standart_arg(arg=42)  # стандартный аргумент можно применять как с клчюе, так и без

# kwd_only_arg(42)  # ошибка
kwd_only_arg(arg=42)  # только можно передавать ключевые 


def combined_example(pos_only, /, standart, *, kwd_only):
    """Пример функции со всеми вариантами параметров"""
    print(pos_only, standart, kwd_only)


# combined_example(1, 2, 3)  # ошибка
combined_example(1, 2, kwd_only=3)
combined_example(1, standart=2, kwd_only=3)


# combined_example(kwd_only=1, standart=2, kwd_only=3)  # ошибка
#
# *args и **kwargs принимают несколько аргументов позиционных или ключевых аргументов
# это общепринятое соглашение
# def func(*args): - принимает любое число позиционных аргументов
# def func(**kwargs): - принимает любое число ключеавых аргументов
# def func(*args, **kwargs): - принимает любое число позиционных и ключевых аргументов
def mean(*args):
    return sum(args) / len(args)


print("args, kwargs")
print(mean(*[1, 2, 3]))  # args со звездочкой превращается в кортеж
print(mean(1, 2, 3))


def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')


school_print(химия=5, физика=4, математика=5, физра=5)
# области видимости
# Локальная - код внутри функции, т.е. переменные заданные в функции
# Глобальная, global - код модуля, т.е. переменные заданные в файле py содержащим функцию
# Не локальная nonlocal - код внешней функции, исключащий доступ к глобальным переменным
# доступ к глобальной КОНСТАНТЕ из тела функции - нормально!
"""Глобальная переменная"""


def func(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }')
    return y + 1


print("global")
x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')

"""Не локальная переменная"""


# её не видно из основного кода, но видно во внешней функции

def main(a):
    x1 = 1

    def func2(y):
        nonlocal x1
        x1 += 100
        print(f'In func {x1 = }')
        return y + 1

    return x1 + func2(a)


print("nonlocal")
x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')

# внешнюю константу видно внутри функций
LIMIT = 1_000


def func2(x, y):
    """
    Таким образом комментируется функция
    :param x: основание
    :param y: степень
    :return: результат возведения в степень
    """
    result = x ** y % LIMIT
    return result


print(func2(42, 73))

# анонимная функция lambda

# add_two_lambda = lambda a, b: a + b  # анонимную функцию нельзя так присваивать
# print(add_two_lambda(42, 3.14))

# так с анонимной функцией работать можно
my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x3: x3[1])
print(f'{s_key = }\n{s_value = }')

# документация к функции пишется сразу после определения функции в """вот так"""
# встроенные функции map(), filter(), zip()
texts = ['Привет', 'ЗДОРОВА', 'ПриВетствую']
res = map(lambda x1: x1.lower(), texts)
print(*res)

numbers = [42, -73, 1024]
res = tuple(filter(lambda x1: x1 > 0, numbers))
print(res)

names = ['Иван', 'Николай', 'Пётр']
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

# функции max(), min(), sum()
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(max(lst_1, default='empty'))  # или min()
print(max(*lst_2))
print(max(lst_3, key=lambda x1: x1[1]))

my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))

# функции all() - если все элементы True, any() - если хотя бы 1 элемент True
# chr() - символ по коду возвращется, ord() - наоборот
# locals() - возвращает список локальных переменных
# globals() - возвращает список глобальных переменных
# vars() - без аргументов работает как locals(), с аргументом возвращает атрибут __dict__
print(globals())

data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data)))
print(max(data, key=lambda x1: -x1))
print(*filter(lambda x1: not x1[0].startswith('__'), globals().items()))
