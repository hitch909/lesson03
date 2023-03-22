# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(**user_data):
    print(f'Имя: {user_data.get("name")}, фамилия: {user_data.get("surname")},'
          f' год рождения: {user_data.get("birth_year")}, город проживания: {user_data.get("city")},'
          f' email: {user_data.get("email")}, телефон: {user_data.get("phone")}')


user = {'name': 'Ivan', 'surname': 'Ivanov', 'birth_year': '1900', 'city': 'Moscow', 'email': 'jackie@gmail.com',
        'phone': '01005321456', }

user_data(**user)

