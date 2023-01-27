import datetime


def log_cash(regim, surname, result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{regim} : {surname} : {result}. Время запроса: {str(datetime.datetime.now())}\n')