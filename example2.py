# Задание № 2: Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

print("Задание № 2. Функция, описывающая данные пользователя:")


def person_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Личная карточка. Имя: {name}. Фамилия: {lastname}. Год рождения: {year_of_birth}.'
                 f'Город проживания: {city}. E-mail: {email},  телефон: {phone}')


person_data(
    name=input('Пожалуйста, укажите Ваше имя: '),
    lastname=input('Вашу фамилию: '),
    year_of_birth=input('Год рождения: '),
    city=input('Укажите город проживания: '),
    email=input('Введите Ваш email: '),
    phone=input('Добавьте номер телефона: '),
)
