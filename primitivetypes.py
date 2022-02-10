# Python program showing that
# json support different primitive
# types
#PYTHON OBJECT TO JSON OBJECT
import json

# list conversion to Array
print(json.dumps(['Welcome', "to", "JSON"]))

# tuple conversion to Array
print(json.dumps(("Welcome", "to", "JSON")))

# string conversion to String
print(json.dumps("Hi"))

# int conversion to Number
print(json.dumps(123))

# float conversion to Number
print(json.dumps(23.572))

# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print(json.dumps(None))