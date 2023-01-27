def inp_mod():
    mod = 0
    while ((mod != 1) and (mod != 2)):
        mod = int(input('Введите режим работы (импорт(1) или экспорт(2)): '))
    return mod

def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname

def view_import (result):
    print(*result, sep='\n') 

def inp_export():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    sec_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    comment = input('Ведите признак телефона (домашний, рабочий): ')
    return '\n', surname, name, sec_name, phone, comment


def view_import_no (surname):
    print(f'Данных с фамилией {surname} не найдено')
