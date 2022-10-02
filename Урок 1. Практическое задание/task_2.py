"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

"""
O(n^2)
"""

def sort_quadratic(list_to_check):
    min_value = 0
    for i in range(len(list_to_check)): # O(len(list_to_check))
        value_to_check = list_to_check[i] # O(1)
        if (i == 1): # O(1)
            min_value = value_to_check # O(1)
        for j in range(len(list_to_check)): # O(len(list_to_check))
            if (value_to_check < list_to_check[j] and list_to_check[j] < min_value): # O(1)
                min_value = value_to_check # O(1)
    return min_value # O(1)

"""
O(n)
"""

def sort_linear(list_to_check):
    min_value = 0 # O(1)
    for i in range(len(list_to_check)): # O(len(list_to_check))
        current_value = list_to_check[i] # O(1)
        if (i == 1) or (min_value > current_value): # O(1)
            min_value = current_value # O(1)
    return min_value # O(1)


list_to_check = [10, 3, 16, 20]

print(sort_linear(list_to_check))
print(sort_quadratic(list_to_check))
