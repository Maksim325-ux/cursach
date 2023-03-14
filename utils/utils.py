import json

def data_file(path):
    '''получаем  словарь с json файла'''
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtered_operation(file):
    '''фильтруем имеющийся список по наличию значения EXECUTED'''
    result = []
    for item in file:
        if item['state'] == 'EXECUTED':
            result.append(item)
    return result



