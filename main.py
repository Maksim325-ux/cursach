import os
from utils.utils import get_data_file, get_filtered_operation, get_last_data, get_format_time

OPERATIONS_PATH = os.path.join('operations.json')

data = get_data_file(OPERATIONS_PATH)
data = get_filtered_operation(data)
print(data)
data = get_last_data(data)
print(data)
data = get_format_time(data)


#print(data)


