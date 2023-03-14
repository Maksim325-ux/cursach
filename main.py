import os
from utils.utils import data_file, get_filtered_operation

OPERATIONS_PATH = os.path.join('operations.json')

user_operation = data_file(OPERATIONS_PATH)
operation_execut = get_filtered_operation(user_operation)

print(operation_execut)


