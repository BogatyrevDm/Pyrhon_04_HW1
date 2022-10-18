"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""
from memory_profiler import memory_usage

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

# Практическое задание из 1 урока курса по основам.
def percent_declension(percent: int) -> str:
    last_numeric = percent % 10
    if last_numeric == 1 and percent != 11:
        return f'{percent} процент'
    elif (last_numeric == 2 or last_numeric == 3 or last_numeric == 4) and percent != 12 and percent != 13 and percent != 14:
        return f'{percent} процента'
    else:
        return f'{percent} процентов'



@decor
def print_result():
    for i in range(1, 101):
        result = percent_declension(i)
        print(result)
res, mem_diff = print_result()
print(f"Выполнение заняло {mem_diff} Mib")
# Выполнение заняло 0.01171875 Mib

def gen_opt(a, b):
    numbers = range(a, b)
    for i in numbers:
        yield i

@decor
def print_result_opt():
    gen = gen_opt(1, 101)
    for i in gen:
        result = percent_declension(i)
        print(result)

res, mem_diff = print_result_opt()
print(f"Выполнение заняло {mem_diff} Mib")
# Выполнение заняло 0.0 Mib
# Для оптимизации использовал генератор. Произошло значительное сокращение объема занимаемой памяти
