import json

employee='{"id":"123","name":"john","age":18}'
# convert json object into python object
emp_dict=json.loads(employee)
print(emp_dict)
print(type(emp_dict))