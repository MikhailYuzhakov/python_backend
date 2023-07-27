# Строки - работает как со списками list
text = 'Hello world'
print(text[6])
print(text[3:7])  # выводит от и до

new_txt = text.replace('l', 'L', 2)  # 2 замены символа сделает
print(text, new_txt, sep='\n')

print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))

print(text[::-1])  # развернуть список
# форматирование строк (%, format(), f-строка)
# через % - устаревший способ, не стоит использовать
name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)  # передаем кортеж
print(text)

# format() - явно не указываем тип данных в фигурных скобках
# начиная с python 3.7 метод заменили f-строки
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)

# f-строки, отдать предпочтение f-строкам
text = f'Меня зовут {name} и мне {age} лет'
print(text)
print(f'{{Фигурные скобки}} и {{name}}')

# форматирование строк
pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')
# указываем отступ вправо на 10 символов (> < ^)
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')
# учитывает пробелы до и после равно, _ знак разделения
num = 2 * pi * data[1]
print(f'{num = :_}')

# строковые методы split(), join(), upper(), lower(), title(), capitalize()
link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
# print(urls)
# a, b, c = input('Введите 3 числа через пробел: ').split()
# print(c, b, a)
# a, b, c, *_ = input('Введите не менее трёх чисел через пробел: ').split()
# print(a, b, c)

# join() добавит символ после каждого элемента списка
data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts']
url = '/'.join(data)
print(url)

# изменение регистра
text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

text = 'Однажды в студеную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))

# кортежи tuple - неизменяемая версия списка list()
# методы модификации не работают
# работают index(), срезыб len(), count() и обращение по индексу []
# f(a, b, c) - вызов функции с тремя аругментами
# f((a, b, c)) - вызов функции с одним аругментов в виде кортежа
d = tuple(range(3))
print(f'{d = }')
print(type('text',))

# Словари dict, ключ неизменяемое значение, а значения изменяемые
# Создание словаря
a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
# передаем в словрь список состоящий из кортежей по два объекта
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c)

# добавить новый элемент
x = 10
a['four'] = x
print(a)

# доступ к значения словаря
# dict[key] - обращение по ключу
# dict.get(key[, default]) - доступ через метод get()
TEN = 'ten'  # константа
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

print(my_dict['two'])
print(my_dict[TEN])

print(my_dict.get('two'))
print(my_dict.get('five', 5))  # вернет значение по указаному ключу, а при отсутствии вернет 5

# методы работы со словарем
# setdefault() - возвращает значение и добавляет ключ в словарь
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam = }\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs = }\t{my_dict=}')
# keys() - возвращает объект итератор dict_keys
# vapolues() - возвращает объект итератор dict_values
# items() - возвращает объект итератор dict_items
# popitem() - удаляет последнюю пару ключ-значение
# pop() - удаляет пару ключ-значение по ключу
# update() - расширяет исходный словарь новыми парами

