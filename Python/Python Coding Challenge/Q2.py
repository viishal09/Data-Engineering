# Lambda function to square a number
square = lambda x: x**2

# Using the lambda function
result = square(5)
print("Output of Lambda Function :")
print(result)  # Output: 25

import json

# JSON string
json_string = '{"name": "John", "age": 25, "city": "New York"}'

# Parsing JSON string to a Python dictionary
data_dict = json.loads(json_string)

# Displaying the Python dictionary
print("Displaying Python Dictionary :")
print(data_dict)


# JSON array string
json_array_string = '[1, 2, 3, 4, 5]'

# Parsing JSON array string to a Python list
data_list = json.loads(json_array_string)

# Displaying the Python list
print("Displaying Python List :")
print(data_list)
