"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import json
import os
import hashlib


def get_hash(salt, url):
    return hashlib.sha256(salt.encode() + url.encode())


def create_cash(salt, url, cash_hash_dict, json, file_name):
    hash = get_hash(salt, url)
    cash_hash_dict[salt] = hash.hexdigest()
    write_cash(json, file_name, cash_hash_dict)


def write_cash(json, file_name, url_hash_dict):
    with open(file_name, 'w', encoding='utf-8') as fw:
        json.dump(url_hash_dict, fw, ensure_ascii=False, indent=2)
        print('Кэш записан!')

def get_file_content(file_name):
    with open(file_name, 'r', encoding='utf-8') as frw:
        result_str = frw.read()
        return result_str


def cash(url: str):
    url_splited = url.split('/')
    # В качестве соли возьмем корень сайта
    salt = url_splited[2]

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_NAME = 'task_3_4_cash.json'
    print(BASE_DIR)

    full_path = os.path.join(BASE_DIR, FILE_NAME)
    # Проверим файл на существование
    if not os.path.exists(full_path):
        # Создадим файл, если не существует
        file = open(full_path, 'w', encoding='utf-8')
        file.close()

    result_str = get_file_content(FILE_NAME)

    if result_str != '':
        result = json.loads(result_str)
        if isinstance(result, dict):
            cash_result = result.get(salt)
            if cash_result == None:
                create_cash(salt, url, result, json, FILE_NAME)
            else:
                print(f'{cash_result}')
    else:
        cash_hash_dict = {}
        create_cash(salt, url, cash_hash_dict, json, FILE_NAME)

# Записываем страницы в кеш
cash('https://vk.com/feed')
cash('https://www.ozon.ru/my/orderlist')
cash('https://mail.rambler.ru/folder/INBOX')

# При повторном обращении - выводим хеш из кеша
cash('https://vk.com/feed')
cash('https://www.ozon.ru/my/orderlist')
cash('https://mail.rambler.ru/folder/INBOX')

