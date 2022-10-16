"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from timeit import timeit
from collections import deque

"""1) сравнить операции append, pop, extend"""


def list_append(list_example, n):
    for i in range(n):
        list_example.append(i)


def deque_append(deque_example, n):
    for i in range(n):
        deque_example.append(i)


def list_extend(list_example, n):
    for i in range(n):
        list_example.extend([i])


def deque_extend(deque_example, n):
    for i in range(n):
        deque_example.extend([i])


def list_pop(list_example):
    for i in range(len(list_example)):
        list_example.pop()


def deque_pop(deque_example):
    for i in range(len(deque_example)):
        deque_example.pop()


list_example = []
deque_example = deque([])
n = 100
# print("list_append ", timeit(stmt="list_append(list_example, n)", number=10000, globals=globals()), "seconds")
# print("deque_append ", timeit(stmt="deque_append(deque_example, n)", number=10000, globals=globals()), "seconds")
#
# print("list_extend ", timeit(stmt="list_extend(list_example, n)", number=10000, globals=globals()), "seconds")
# print("deque_extend ", timeit(stmt="deque_extend(deque_example, n)", number=10000, globals=globals()), "seconds")
#
# print("list_pop ", timeit(stmt="list_pop(list_example)", number=1, globals=globals()), "seconds")
# print("deque_pop ", timeit(stmt="deque_pop(deque_example)", number=1, globals=globals()), "seconds")
"""
list_append  0.1914340000366792 seconds
deque_append  0.07778389996383339 seconds
list_extend  0.13354129996150732 seconds
deque_extend  0.146182999946177 seconds
list_pop  0.13132210006006062 seconds
deque_pop  0.21725740004330873 seconds
Операция append проходит для deque быстрее
Операции pop и extand для deque проходят медленнее
"""

"""
2) сравнить операции appendleft, popleft, extendleft 
"""


def list_insert(list_example, n):
    for i in range(n):
        list_example.insert(0, i)


def deque_appendleft(deque_example, n):
    for i in range(n):
        deque_example.appendleft(i)


def list_extendleft(list_example, n):
    for i in range(n):
        list_example = [i] + list_example


def deque_extendleft(deque_example, n):
    for i in range(n):
        deque_example.extendleft([i])


def list_popleft(list_example):
    for i in range(len(list_example)):
        list_example.pop(0)


def deque_popleft(deque_example):
    for i in range(len(deque_example)):
        deque_example.popleft()


list_example = []
deque_example = deque([])

print("list_insert ", timeit(stmt="list_insert(list_example, n)", number=100, globals=globals()), "seconds")
print("deque_appendleft ", timeit(stmt="deque_appendleft(deque_example, n)", number=100, globals=globals()), "seconds")

print("list_extendleft ", timeit(stmt="list_extendleft(list_example, n)", number=100, globals=globals()), "seconds")
print("deque_extendleft ", timeit(stmt="deque_extendleft(deque_example, n)", number=100, globals=globals()), "seconds")

print("list_popleft ", timeit(stmt="list_popleft(list_example)", number=1, globals=globals()), "seconds")
print("deque_popleft ", timeit(stmt="deque_popleft(deque_example)", number=1, globals=globals()), "seconds")

"""
list_insert  0.04005500010680407 seconds
deque_appendleft  0.0006433000089600682 seconds
list_extendleft  0.2237765999743715 seconds
deque_extendleft  0.0013547999551519752 seconds
list_popleft  0.012876400025561452 seconds
deque_popleft  0.001496099983341992 seconds
Операции appendleft, popleft и extendleft для deque проходят быстрее чем аналогичные по смыслу операции для list
"""

"""
3) сравнить операции получения элемента списка и дека
"""


def list_get(list_example):
    for i in list_example:
        result = list_example[i]


def deque_get(deque_example):
    for i in deque_example:
        result = deque_example[i]


list_example = []
deque_example = deque([])
list_append(list_example, n)
deque_append(deque_example, n)
print("list_get ", timeit(stmt="list_get(list_example)", number=100000, globals=globals()), "seconds")
print("deque_get ", timeit(stmt="deque_get(deque_example)", number=100000, globals=globals()), "seconds")
"""
list_get  0.23103839997202158 seconds
deque_get  0.32046609988901764 seconds
Получение элемента для deque происходит медленнее
"""