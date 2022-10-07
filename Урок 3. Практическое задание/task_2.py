"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import json
import os
import hashlib


def get_hash(login, password):
    return hashlib.sha256(login.encode() + password.encode())


def check_hash(login, password, password_check, login_hash_dict):
    password_hash = get_hash(login, password)
    password_hash_check = get_hash(login, password_check)
    if password_hash.hexdigest() == password_hash_check.hexdigest():
        print("Авторизация успешна!")
        login_hash_dict[login] = password_hash.hexdigest()
        return True
    else:
        print("Пароли не совпадают!")
        return False


def create_write_user(login, password, login_hash_dict, json, file_name):
    registration_success = create_user(login, password, login_hash_dict)
    if registration_success:
        write_users(json, file_name, login_hash_dict)


def check_user(login, password, hash_check, login_hash_dict):
    password_hash = get_hash(login, password)
    if password_hash.hexdigest() == hash_check:
        print("Авторизация успешна!")
    else:
        print("Пароли не совпадают!")


def create_user(login, password, login_hash_dict):
    password_check = input("Введите второй раз пароль:\n")
    return check_hash(login, password, password_check, login_hash_dict)


def write_users(json, file_name, login_hash_dict):
    with open(file_name, 'w', encoding='utf-8') as fw:
        json.dump(login_hash_dict, fw, ensure_ascii=False, indent=2)


def get_file_content(file_name):
    with open(file_name, 'r', encoding='utf-8') as frw:
        result_str = frw.read()
        return result_str


login = input("Введите логин:\n")
password = input("Введите пароль:\n")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = 'task_3_2_users.json'
print(BASE_DIR)

full_path = os.path.join(BASE_DIR, FILE_NAME)
# Проверим файл на существование
if not os.path.exists(full_path):
    # Создадим файл, если не существует
    file = open(full_path, 'w', encoding='utf-8')
    file.close()

result_str = get_file_content(FILE_NAME)

if result_str != '':
    print(result_str)
    result = json.loads(result_str)
    if isinstance(result, dict):
        user_result = result.get(login)
        if user_result == None:
            create_write_user(login, password, result, json, FILE_NAME)
        else:
            check_user(login, password, user_result, result)
else:
    login_hash_dict = {}
    create_write_user(login, password, login_hash_dict, json, FILE_NAME)
