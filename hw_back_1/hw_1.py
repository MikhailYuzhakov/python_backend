# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник
# разносторонним, равнобедренным или равносторонним.

a = int(input("Введите длину стороны треугольника a = "))
b = int(input("Введите длину стороны треугольника b = "))
c = int(input("Введите длину стороны треугольника c = "))

if a > b + c or b > a + c or c > b + a:
    print("Такого треугольника не существует")
else:
    if a != b and c != b:
        print("Треугольник разносторонний")
    elif (a == b or b == c) and c != a:
        print("Треугольник равнобедренный")
    elif a == b and b == c:
        print("Треугольник равносторонний")

