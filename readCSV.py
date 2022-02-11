import csv

with open("D:\details1.csv") as file:
    data=csv.reader(file,delimiter=' ')
    for row in data:
        print(' '.join(row))