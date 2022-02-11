import csv
data=[["id","name","age"],["100", "john", "18"],["101", "peter", "21"]]
with open("D:\writemultipledemo.csv",'w',newline='') as file:
    writer1=csv.writer(file)
    writer1.writerows(data)
