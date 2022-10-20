"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit


def bubble_sort_desc(lst_obj):
    n = 1

    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_desc_opt(lst_obj):
    n = 1

    while n < len(lst_obj):
        sort_is_success = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                sort_is_success = True
        if not sort_is_success:
            break
        n += 1
    return lst_obj


orig_list = [randint(-100, -100) for _ in range(10)]
print(bubble_sort_desc(orig_list[:]))
print(bubble_sort_desc_opt(orig_list[:]))

# замеры 10
print(
    timeit(
        "bubble_sort_desc(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "bubble_sort_desc(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "bubble_sort_desc(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, -100) for _ in range(10)]

# замеры 10
print(
    timeit(
        "bubble_sort_desc_opt(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "bubble_sort_desc_opt(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "bubble_sort_desc_opt(orig_list[:])",
        globals=globals(),
        number=1000))
"""
bubble_sort_desc
0.005714400002034381
0.5031054000137374
57.4198395999847

bubble_sort_desc_opt
0.0010658999963197857
0.5726118000166025
62.57835339999292

Для неотсортированных массивов разницы нет. 
Разница будет, если будет передан уже отсортированный массив. 
В таком случае bubble_sort_desc_opt выполнится быстрее
"""
