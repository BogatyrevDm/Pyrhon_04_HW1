"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calculator():
    sign_result = input('Введите операцию (+, -, *, / или 0 для выхода):')
    if not sign_result == '0':
        if not (sign_result == '+' or sign_result == '-' or sign_result == '*' or sign_result == '/'):
            print('Вы ввели не верный знак!')
            calculator()
        else:
            first_numeric_result = input('Введите первое число:')
            if not first_numeric_result.isdigit():
                print('Вы ввели не число! Исправьтесь!')
                calculator()
            else:
                second_numeric_result = input('Введите второе число:')
                if not second_numeric_result.isdigit():
                    print('Вы ввели не число! Исправьтесь!')
                    calculator()
                else:
                    if sign_result == '+':
                        result = int(first_numeric_result) + int(second_numeric_result)
                    elif sign_result == '-':
                        result = int(first_numeric_result) - int(second_numeric_result)

                    elif sign_result == '*':
                        result = int(first_numeric_result) * int(second_numeric_result)

                    else:
                        if int(second_numeric_result) == 0:
                            print('На ноль делить нельзя! Исправьтесь!')
                            calculator()
                        result = int(first_numeric_result) / int(second_numeric_result)
                    print(f'Ваш результат {result}')
                    calculator()
    else:
        print('Расчет окончен!')


calculator()
