# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
# препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку. Translate
# из модуля string
import string

f = open('text.txt', 'r')
words = list()
my_dict = dict()
symbols = '!@#$%^&*()_+|-=,./;:'

try:
    my_text = f.readlines()  # читаем строки из файла
    for text in my_text:  # удаляем символы, переносы строки и переводим в нижний регистр
        for word in text.split(' '):
            for removed_symbol in symbols:
                word = word.replace(removed_symbol, '').rstrip('\n').lower()
            words.append(word)  # слова разделенные пробелом добавляем в список words
finally:
    f.close()

# считаем кол-во повторений каждого слова и создаем словарь [слово:кол-во повторений]
for word in words:
    n = words.count(word)
    my_dict[word] = n

my_dict.pop('')  # удаляем из словаря пустые символы, если остались

# выделяем список ключей и значений из словоря, сортируем по убыванию список с кол-вом повторений слов
key_list = list(my_dict.keys())
values_list = list(my_dict.values())
sorted_value_list = sorted(values_list, reverse=True)

# выводим 10 самых частых слов и кол-во повторений
print('10 наиболее частых слов в тексте: ')
for i in range(10):
    item = key_list.__getitem__(values_list.index(sorted_value_list.__getitem__(i)))
    key_list.remove(item)
    values_list.remove(sorted_value_list.__getitem__(i))
    print(f'{i + 1} - {item} = {sorted_value_list.__getitem__(i)}')



