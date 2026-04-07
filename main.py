import math_utils
import string_module
import os_utils
import json_utils
import exception_utils

# Math
print(math_utils.square_num(5))
print(math_utils.find_log(10))

# String
print(string_module.to_upper("hello"))
print(string_module.reverse_text("python"))

# OS
print(os_utils.show_files())
print(os_utils.create_folder("demo_folder"))

# JSON
data = {"name": "Jahnavi", "marks": 95}
print(json_utils.write_data(data))
print(json_utils.read_data())

# Exception
print(exception_utils.divide(10, 2))
print(exception_utils.divide(10, 0))