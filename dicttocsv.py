import csv

with open("D:\dicttocsvfile.csv","w",newline='')as file:
    fieldnames=['name','age']
    writer1=csv.DictWriter(file,fieldnames=fieldnames)
    writer1.writeheader()
    writer1.writerow({'name':'ramu',"age":18})
    writer1.writerow({'name': 'raju', "age": 21})