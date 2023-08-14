# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibbonachi(n: int) -> list[int]:
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for number in fibbonachi(10):
    print(f'{number}', end=" ")
