import os
from utils.utils import get_data_file, get_filtered_operation, get_last_data, get_format_time, operations

OPERATIONS_PATH = os.path.join('operations.json')

data = get_data_file(OPERATIONS_PATH)
data = get_filtered_operation(data)
data = get_last_data(data)

for item in data:
    new_date = get_format_time(item['date'])
    print(f'{new_date} {item["description"]}')
    str_ = operations(item)
    print(str_)
    print(f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}')
    print()


