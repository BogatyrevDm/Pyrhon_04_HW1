"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from collections import defaultdict

def make_multiplication(first_list_reversed, second_list_reversed):
    max_length = max(len(first_list_reversed), len(second_list_reversed))

    if len(first_list_reversed) > len(second_list_reversed):
        bigger_list = first_list_reversed
        smaller_list = second_list_reversed
    else:
        bigger_list = second_list_reversed
        smaller_list = first_list_reversed
    # Алгоритм имитирует умножение в столбик
    list_result = []
    # Здесь будем хранить нули для сдвига разрядов
    list_shift = []
    ch = 0
    for i in smaller_list:
        ch += 1
        list_mult = []
        rest = '0'
        for j in bigger_list:
            mult_hex = hex(int(i, 16) * int(j, 16) + int(rest, 16))[2:]
            if len(mult_hex) > 1:
                rest = mult_hex[:-1]
                mult_hex = mult_hex[-1]
            else:
                rest = '0'
            list_mult.append(mult_hex)
        if rest != '0':
            list_rest = list(rest)
            list_rest.reverse()
            list_mult.extend(list_rest)
        if ch > 1:
            list_shift.append('0')
        list_result.append(list_shift + list_mult)
    list_sum = []
    for i in list_result:
        list_sum.reverse()
        list_sum = make_sum(list_sum, i)
    return list_sum

def make_sum(first_list_reversed, second_list_reversed):
    max_length = max(len(first_list_reversed), len(second_list_reversed))
    rest = '0'
    # Алгоритм имитирует сложение в столбик
    list_sum = []
    for i in range(max_length):

        if i >= len(first_list_reversed):
            first_number = '0'
        else:
            first_number = first_list_reversed[i]
        if i >= len(second_list_reversed):
            second_number = '0'
        else:
            second_number = second_list_reversed[i]

        sum_hex = hex(int(first_number, 16) + int(second_number, 16) + int(rest, 16))[2:]

        # Если длина больше одного - отрезаем все, что перед последним символом и оставляем для следующей иттерации
        if len(sum_hex) > 1:
            rest = sum_hex[:-1]
            sum_hex = sum_hex[-1]
        else:
            rest = '0'
        list_sum.append(sum_hex)

    if rest != '0':
        list_rest = list(rest)
        list_rest.reverse()
        list_sum.extend(list_rest)
    list_sum.reverse()
    return list_sum

first_list = list("A2")
second_list = list("C4F")

sum_dict = defaultdict(list)
sum_dict["first"] = first_list
sum_dict["second"] = second_list
first_list_reversed = list(reversed(first_list))
second_list_reversed = list(reversed(second_list))
list_sum = make_sum(first_list_reversed, second_list_reversed)
sum_dict["sum"] = list_sum
list_mult = make_multiplication(first_list_reversed, second_list_reversed)
sum_dict["mult"] = list_mult
print(sum_dict)


