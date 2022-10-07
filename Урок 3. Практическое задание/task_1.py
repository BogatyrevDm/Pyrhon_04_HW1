"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def time_measurement(message):
    def _time_measurement(func):
        def measure(*args, **kwargs):
            start_val = time.time()
            func(*args, **kwargs)
            end_val = time.time()
            result = end_val - start_val
            print(f'{message} {result}')

        return measure

    return _time_measurement


# O(n)
@time_measurement('list fill')
def list_fill(list_example, n):
    for i in range(n):  # O(n)
        list_example.append(i)  # O(1)


# O(n)
@time_measurement('dict fill')
def dict_fill(dict_example, n):
    for i in range(n):  # O(n)
        dict_example[i] = i  # O(1)

"""
list fill 0.004986286163330078
dict fill 0.008977174758911133
"""
# Операция по заполнению словаря происходит дольше, потому что в процессе происходит создание хеша

# O(n)
@time_measurement('list get')
def list_get(list_example):
    for i in list_example:  # O(n)
        result = list_example[i]  # O(1)


# O(n)
@time_measurement('dict get')
def dict_get(dict_example, n):
    for i in range(n):  # O(n)
        result = dict_example.get(i)  # O(1)
"""
list get 0.0029909610748291016
dict get 0.00534367561340332
"""
# Операция по получению элемента списка происходит быстрее, потому что список упорядочен

# O(n)
@time_measurement('list del')
def list_del(list_example):
    for i in range(len(list_example)):  # O(n)
        list_example.pop()  # O(1)


# O(n)
@time_measurement('dict del')
def dict_del(dict_example, n):
    for i in range(n):  # O(n)
        dict_example.popitem()  # O(1)

"""
list del 0.00498652458190918
dict del 0.0069811344146728516
"""
# Операция по удалению элемента списка происходит быстрее, потому что список упорядочен

list_example = []
dict_example = {}

n = 100000

# заполнение списка
list_fill(list_example, n)

# заполнение словаря
dict_fill(dict_example, n)

# получение элемента списка
list_get(list_example)

# получение элемента словаря
dict_get(dict_example, n)

# удаление элемента списка
list_del(list_example)

# удаление элемента словаря
dict_del(dict_example, n)
