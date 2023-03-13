import requests

def data_file(url):
    '''получаем json словарь с сайта'''
    data = requests.get(url)
    return data.json()

def get_filtered_operation(operation):
    result = []
    for item_dict in operation:
        if item_dict['state'] == 'EXECUTED':
            result.append(item_dict)
    print(result)


