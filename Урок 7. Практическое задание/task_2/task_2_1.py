"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

# Использована гномья сортировка

def find_mediana(m):
    length = 2 * m + 1
    orig_list = [randint(-100, 100) for _ in range(length)]

    i=1
    size = len(orig_list)
    while i < size:
        if orig_list[i - 1] <= orig_list[i]:
            i += 1
        else:
            orig_list[i - 1], orig_list[i] = orig_list[i], orig_list[i - 1]
            if i > 1:
                i -= 1
    mediana = orig_list[m]

find_mediana(2)

# замеры 10
print(
    timeit(
        "find_mediana(5)",
        globals=globals(),
        number=1000))

# замеры 100
print(
    timeit(
        "find_mediana(50)",
        globals=globals(),
        number=1000))

# замеры 1000
print(
    timeit(
        "find_mediana(500)",
        globals=globals(),
        number=1000))

"""
0.019636500015622005
0.672767100011697
72.56054130001576
"""