import json

employee={"id":"123","name":"john","age":18}
# convert python object into json object
emp=json.dumps(employee)
print(emp)
print(type(emp))