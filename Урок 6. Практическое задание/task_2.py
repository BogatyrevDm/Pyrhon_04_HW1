"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


# Для профилирования использована функция из одного из предыдущих заданий
# Проблема с профилированием рекурсивной функции в том, что считается каждый ее вызов отдельно.
@profile
def even_and_uneven_numerics(numeric, even=0, uneven=0):
    remainder = numeric % 10
    division_result = numeric // 10

    if remainder % 2 == 0:
        even += 1
    else:
        uneven += 1
    if division_result == 0:

        print(f'Количество четных и нечетных цифр в числе равно: {even}, {uneven}')
    else:
        even_and_uneven_numerics(division_result, even, uneven)


# even_and_uneven_numerics(34560)

# Решение - обернем ее другой функцией и будем профилировать ее
@profile
def recurtion_wrapper(numeric):
    def even_and_uneven_numerics(numeric, even=0, uneven=0):
        remainder = numeric % 10
        division_result = numeric // 10

        if remainder % 2 == 0:
            even += 1
        else:
            uneven += 1
        if division_result == 0:

            print(f'Количество четных и нечетных цифр в числе равно: {even}, {uneven}')
        else:
            even_and_uneven_numerics(division_result, even, uneven)

    even_and_uneven_numerics(numeric)


recurtion_wrapper(34560)
