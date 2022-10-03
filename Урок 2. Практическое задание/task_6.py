"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def try_to_guess(number, max_try, try_count=0):
    try_count += 1

    user_guess = int(input('Попробуйте угадать число от 1 до 100:'))

    if user_guess == number:
        print('Вы угадали!')
    elif try_count == max_try:
        print('Закончились попытки!')
        print(f'Загаданное число {number}!')
    else:
        if number < user_guess:
            print('Загаданное число меньше!')
        else:
            print('Загаданное число больше!')
        try_to_guess(number, max_try, try_count)


number = random.randint(1, 100)

try_to_guess(number, 10)
