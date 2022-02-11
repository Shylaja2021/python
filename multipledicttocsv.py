import csv

dict_list=[{"name":"smith","age":22},{"name":"paul","age":24},{"name":"johns","age":21},{"name":"sham","age":20}]

with open("D:\multipledicttocsvfile.csv","w")as file:
    fieldnames=["name","age"]
    writer1=csv.DictWriter(file,fieldnames=fieldnames)
    writer1.writeheader()
    writer1.writerows(dict_list)