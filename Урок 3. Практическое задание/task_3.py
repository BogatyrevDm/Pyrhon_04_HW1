"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib


def get_unique_substrings(string_example):
    set_result = set()

    new_string = ''
    for i in range(len(string_example) - 1):
        new_string += string_example[i]
        set_result.add(hashlib.sha256(new_string.encode('utf-8')))
        rest = string_example[i + 1:len(string_example)]
        set_result.add(hashlib.sha256(rest.encode('utf-8')))
    return len(set_result)


print((get_unique_substrings('рара')))



