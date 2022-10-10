"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    num_arr = []
    for i in str(enter_num):
        num_arr.insert(0, str(i))
    return int("".join(num_arr))


enter_num = 12345
print("revers ", timeit(stmt="revers(enter_num)", number=10000, globals=globals()), "seconds")
print("revers_2 ", timeit(stmt="revers_2(enter_num)", number=10000, globals=globals()), "seconds")
print("revers_3 ", timeit(stmt="revers_3(enter_num)", number=10000, globals=globals()), "seconds")
print("revers_4 ", timeit(stmt="revers_4(enter_num)", number=10000, globals=globals()), "seconds")
"""
revers  0.008895300037693232 seconds
revers_2  0.00638430000981316 seconds
revers_3  0.002514399995561689 seconds
revers_4  0.008734599978197366 seconds
Самый эффективный 3-ий вариант, потому что он использует встроенную функцию среза.  
"""