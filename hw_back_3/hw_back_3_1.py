# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно
# быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

my_list_1 = list((1, 2, 5, 3, 1, 2, 4, 9, 9, 9, 9, 5))
my_list_2 = list()
repeated_elements = list()

my_list_2.extend(my_list_1)  # сохраним список
for element in my_list_1:
    n = my_list_1.count(element)
    if n > 1:
        repeated_elements.append(element)
        for _ in range(n):
            my_list_1.remove(element)

print(my_list_2)
print(repeated_elements)
