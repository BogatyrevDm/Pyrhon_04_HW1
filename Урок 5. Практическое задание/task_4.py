"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

ordinary_dict = {'a': 1, 'b': 2, 'c': 3}
ordinary_dict.keys()
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

def ordinary_dict_add(dict_example, n):
    for i in range(n):
        dict_example[i] = i

def ordered_dict_add(dict_example, n):
    for i in range(n):
        dict_example[i] = i

def ordinary_dict_get(dict_example):
    for i in dict_example.keys():
        result = dict_example[i]

def ordered_dict_get(dict_example):
    for i in dict_example.keys():
        result = dict_example[i]

ordinary_dict = {}
ordered_dict = OrderedDict()
n = 1000
print("ordinary_dict_add ", timeit(stmt="ordinary_dict_add(ordinary_dict, n)", number=10000, globals=globals()), "seconds")
print("ordered_dict_add ", timeit(stmt="ordered_dict_add(ordered_dict, n)", number=10000, globals=globals()), "seconds")

print("ordinary_dict_get ", timeit(stmt="ordinary_dict_get(ordinary_dict)", number=10000, globals=globals()), "seconds")
print("ordered_dict_get ", timeit(stmt="ordered_dict_get(ordered_dict)", number=10000, globals=globals()), "seconds")

"""
ordinary_dict_add  0.4407461000373587 seconds
ordered_dict_add  0.6637801999459043 seconds
ordinary_dict_get  0.2930812000995502 seconds
ordered_dict_get  0.39958670001942664 seconds
Операции с OrderedDict происходят медленее, вероятнее всего из-за процедуры упорядочивания
На мой взгляд особого смысла в использовании OrderedDict в Python 3.6 и более поздних версиях нет
"""