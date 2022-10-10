"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_opt(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


old_arr = list(range(1000))

print("func_1 ", timeit(stmt="func_1(old_arr)", number=10000, globals=globals()), "seconds")
print("func_1_opt ", timeit(stmt="func_1_opt(old_arr)", number=10000, globals=globals()), "seconds")
"""
func_1  0.7263765999814495 seconds
func_1_opt  0.552602699957788 seconds
Вторая функция работает быстрее, потому что там применена встроенная оптимизированная функция List Comprehension
"""