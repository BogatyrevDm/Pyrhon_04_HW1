"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

users = {'Sergey':{'password':123, 'active':True}, 'Vasily':{'password':321, 'active':False}}

# Везде будет O(1)

def check_user(name, password):
    user = users.get(name)
    if user == None:
        print('User not found!')
        user_answer = input('Do you want to register? y - yes, n - now')
        if user_answer == 'y':
            user_password = input('Type your password');
            users[name] = {{'password':user_password, 'active':False}}
            print('User registered!')
    else:
        if not user.get('password') == password:
            print('Your password is wrong!')
        elif not user.get('active'):
            print('User inactive!')
            user_answer = input('Do you want to active? y - yes, n - now')
            if user_answer == 'y':
                user['active'] = True
                print('User activated')
        else:
            print('Authorization succeed!')


check_user('Sergey', 321)
check_user('Sergey', 123)
check_user('Vasily', 321)
check_user('Maria', 321)