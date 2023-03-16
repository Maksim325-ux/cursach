import json
from datetime import datetime
def get_data_file(path):
    '''получаем  словарь с json файла'''
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def get_filtered_operation(data):
    '''фильтруем имеющийся список по наличию значения EXECUTED'''
    result = []
    for item in data:
        if 'state' in item and item['state'] == 'EXECUTED':
            result.append(item)
    return result
def get_last_data(data):
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data [:5]

def get_format_time(old_data):
    form_data = datetime.strptime(old_data, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    return form_data




