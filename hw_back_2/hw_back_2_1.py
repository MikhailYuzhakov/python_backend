# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.  Программа должна
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

a = input("Введите первую дробь (/): ")
b = input("Введите вторую дробь (/): ")
m = 1

a_1 = a.split(sep='/')[0]
a_2 = a.split(sep='/')[1]
b_1 = b.split(sep='/')[0]
b_2 = b.split(sep='/')[1]
f1 = fractions.Fraction(a)
f2 = fractions.Fraction(b)

operation = input("Введите операцию (+, *): ")
if operation == "+":
    if int(a_2) != int(b_2):
        m = int(a_2) * int(b_2)
    res = str(int(a_1)*int(m/int(a_2)) + int(b_1)*m/int(b_2)) + "/" + str(m)
    f3 = f1 + f2
    print(a + " + " + b + " = " + res + " fract_res = " + str(f3))
elif operation == "*":
    res = str(int(a_1) * int(b_1)) + "/" + str(int(a_2) * int(b_2))
    f3 = f1 * f2
    print(a + " * " + b + " = " + res + " fract_res = " + str(f3))
else:
    print("Недопустимая операция")
