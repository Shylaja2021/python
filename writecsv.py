import csv
with open("D:\writecsvdemo.csv",'w',newline='') as file:
    writer1=csv.writer(file)
    writer1.writerow(["id","name","age"])
    writer1.writerow(["100", "john", "18"])
    writer1.writerow(["101", "peter", "21"])
