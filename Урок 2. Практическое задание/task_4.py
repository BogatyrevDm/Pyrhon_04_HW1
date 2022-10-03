"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def calculate_summ(number, max_count, result, count=0):
    count += 1
    current_number = number / -2
    result += current_number
    if count == max_count:
        return result
    else:
        return calculate_summ(current_number, max_count, result, count)


max_count = int(input('Введите количество чисел ряда:'))
print(calculate_summ(1, max_count - 1, 1))
