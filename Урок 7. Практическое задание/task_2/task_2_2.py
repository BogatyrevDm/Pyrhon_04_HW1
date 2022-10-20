"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit


def find_mediana(m):
    length = 2 * m + 1
    orig_list = [randint(-100, 100) for _ in range(length)]
    # print(f'Массив {orig_list}')
    for i in range(m + 1):

        max = -100
        for j in orig_list:
            if j > max:
                max = j
        mediana = orig_list.pop(orig_list.index(max))
    # print(f'Медиана {mediana}')


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
0.011868100002175197
0.18644760001916438
11.85983619999024
"""