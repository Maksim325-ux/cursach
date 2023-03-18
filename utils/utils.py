import json
from datetime import datetime
def get_data_file(path):
    '''
    получаем  словарь с json файла
    :param path: заданный json файл
    :return: список data
    '''
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def get_filtered_operation(data):
    '''
    фильтруем имеющийся список по наличию значения EXECUTED
    :param data: первоначальный список
    :return: список отсортированный по операции EXECUTED
    '''
    result = []
    for item in data:
        if 'state' in item and item['state'] == 'EXECUTED':
            result.append(item)
    return result
def get_last_data(data):
    """
    Сортировка списков по дате выполнения опреаций от новых к старым
    :param data:
    :return: возвращает список операций по убыванию даты
    """
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data [:5]

def get_format_time(old_data):
    """
    Функция форматирования даты из списка согласно требуемого формата
    :param old_data: дата до форматирования
    :return: возвращает дату согласно задания
    """
    form_data = datetime.strptime(old_data, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    return form_data

def operations(item):
    str_to = item['to'].split(' ')
    to_ = f'Счет **{str_to[1][-4:]}'
    if item["description"] == "Открытие вклада":
        return to_
    str_from = item['from'].split(' ')
    if item['description'] == 'Перевод со счета на счет':
        return f'{str_from[0]} **{str_from[1][-4:]} -> {to_}'
    if len(str_from) > 2:
        from_ = f'{str_from[0]} {str_from[1]} {str_from[2][:4]} {str_from[2][4:6]}** **** {str_from[2][-4:]}'
    else:
        from_ = f'{str_from[0]} {str_from[1][:4]} {str_from[1][4:6]}** **** {str_from[1][-4:]}'
    return f'{from_} -> {to_}'





