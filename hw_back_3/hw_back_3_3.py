# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи  влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
things_dict = {'зубная щетка': 60, 'зубная паста': 150, 'футболка': 200, 'штаны': 500, 'шорты': 200, 'ноутбук': 1500,
               'смартфон': 130, 'палатка': 2300, 'спальник': 1200, 'котелов': 300, 'газ': 500}
max_weight = 3000

key_list = list(things_dict.keys())
decrement = things_dict.get(key_list.__getitem__(0))
my_things = list()
my_things.append(key_list.__getitem__(0))

i = 1

while max_weight - decrement > 0:
    decrement = things_dict.get(key_list.__getitem__(i))
    max_weight = max_weight - decrement
    my_things.append(key_list.__getitem__(i))
    i += 1
print(f'С собой можно взять: {my_things}')
