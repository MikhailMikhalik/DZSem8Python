# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм

# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - изменение данных
# 5 - удаление данных
# 6 - выход"""
from work_w_file import write, read_all, get_by_name, alter_line

def choose(choice):
    if choice == '1': write(input("Введите ваши данные пример:(фамилия имя отчество номер телефона) "))
    if choice == "2": read_all()
    if choice == "3": get_by_name(input("Введите имя, фамилию, отчество "))
    if choice == "4": alter_line(input("Какую строку заменить? (имя фамилия) "), True)
    if choice == '5': alter_line(input('Какую строку удалить? (имя фамилия) '), False)
    if choice == "6": exit()

def print_instructions():
    return print('Выберите действие: \n 1 - Записать данные в файл \n 2 - Печать всех данных \n '
                 '3 - Поиск по фамилии \n 4 - замена данных \n'
                 '5 - удаление данных \n 6 - Остановить программу')