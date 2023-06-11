# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
# Делим десятичное число на 16 и записываем остаток от деления.
# Результат деления вновь делим на 16 и опять записываем остаток.
# Повторяем операцию до тех пор пока результат деления не будет равен нулю.
# Запишем полученные остатки в обратном порядке и получим искомое число.

#num = int(input('Введите число в десятичной системе: '))
# print(f'Шестнадцатеричное число hex -> {hex(num)}')
#
#
# def self_hex(number: int) -> str:
#     if not number:
#         return '0x0'
#     result = ''
#     hex_letters = list('0123456789abcdef')
#     while number > 0:
#         result = hex_letters[number % 16] + result
#         number //= 16
#     return '0x' + result
#
#
# print(f'Шестнадцатеричное число self_hex -> {self_hex(num)}')

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

print("Запишите два числа в такой форме 'a/b' и вам вернется \nсумма и произведение данных чисел")

first_number = input("")
second_number = input("")
count  = 0
a_1 = ""
a_2 = ""
b_1 = ""
b_2 = ""

while count < len(first_number):
    a_1 += first_number[count]
    count += 1
    if first_number[count] == "/":
        count += 1
        while count < len(first_number):
            a_2 += first_number[count]
            count += 1
count = 0

while count < len(second_number):
    b_1 += second_number[count]
    count += 1
    if second_number[count] == "/":
        count += 1
        while count < len(second_number):
            b_2 += second_number[count]
            count += 1

print("Произведение дробей равно :", int(a_1)*int(b_2), "/", int(a_2)*int(b_1))

a1 = ""
b1 = ""
a2 = ""
b2 = ""
if a_2 != b_2:
    a1 = int(a_1)*int(b_2)
    b1 = int(b_1)*int(a_2)
    a2 = int(a_2)*int(b_2)
    b2 = int(b_2)*int(a_2)
    print("Сумма дробей равна :", a1 + b1, "/", a2)

if a_2 == b_2:
    if int(a_1) + int(b_1) == int(a_2):
        print("Сумма дробей равна единице")
    else:
        print("Сумма дробей равна :", int(a_1) + int(b_1), "/", int(a_2))
