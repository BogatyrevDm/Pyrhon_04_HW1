"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple


def calculate_profit(firms_count):
    average = 0
    all_profits = 0
    firms_list = []
    for i in range(firms_count):
        firms_name = input('Введите название предприятия:\n')
        firms_profits = list(map(float, input(
            'через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):\n').split()))

        RES = namedtuple(firms_name, 'name, first second third fourth annual_profit')
        annual_profit = sum(firms_profits)
        all_profits += annual_profit
        FIRMS = RES(name=firms_name, first=firms_profits[0], second=firms_profits[1], third=firms_profits[2],
                    fourth=firms_profits[3],
                    annual_profit=annual_profit)
        firms_list.append(FIRMS)

    average_profit = all_profits / firms_count
    above_average = []
    below_average = []

    for i in firms_list:
        if i.annual_profit <= average_profit:
            below_average.append(i.name)
        else:
            above_average.append(i.name)
    print(f'Предприятия, с прибылью выше среднего значения: {",".join(above_average)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {",".join(below_average)}')


firms_count = int(input('Введите количество предприятий для расчета прибыли:\n'))
calculate_profit(firms_count)
