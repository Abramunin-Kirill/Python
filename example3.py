# Задание № 3: Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Заводим месяца в консоль (Пока писал, забыл, что нужно отобразить время года, а не название месяца,
# но не удалять же, поэтому просто закомментил)

"""
number = int(input("Введите номер месяца (от 1 до 12): "))
if number >= 1 and number <= 12:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентябрь',
                  10: 'Октябрь',
                  11: 'Ноябрь',
                  12: 'Декабрь'}
    month_list = list(month_dict.values())

# Сам метод:
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"(Решение через list) Указанный Вами месяц: {month_list[i]}")
            break
    print(f"(Решение через dict) Указанный Вами месяц: {month_dict[number]}")
else:  # На случай ввода невалидных данных
    print("Извините, но такого месяца не существует")
"""

print("Задание № 3:")

# Запрашиваем в командной строке номер месяца
m = int(input("Пожалуйста, введите номер месяца (от 1 до 12): "))

# Сам метод:
if m == 1 or m == 2 or m == 12:
    print("Данный месяц относится к зиме")
elif m == 3 or m == 4 or m == 5:
    print('Данный месяц относится к весне')
elif m == 6 or m == 7 or m == 8:
    print('Данный месяц относится к лету')
elif m == 9 or m == 10 or m == 11:
    print('Данный месяц относится к осени')
else:
    print('Извините, но такого месяца не существует')
