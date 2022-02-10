import json

# Data to be written
dictionary ={
         "id": "05",
         "name": "Nancy",
         "department": "Sales"
      }

with open("data.json", "a") as outfile:
   json.dump(dictionary, outfile,indent=4)