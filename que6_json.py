student= {
    "a": 1,
    "a": 2,
    "a": 3,
    "a": 4,
    "b": 1,
    "b": 2
}
# import json
# print("orignal python object")
# print(student)
# students1=json.dumps(student)
# # students2=json.loads(students1)
# print("\nUnique key in a json object:")
# print(students1)

import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# print("Original Python object:")
json_obj = json.loads(python_obj)
# print("\nUnique Key in a JSON object:")
print(json_obj) 
