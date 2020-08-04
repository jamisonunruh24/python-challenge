#Import modules
import csv
import os

# create path to file
resources_path = os.path.join("Resources/" + "budget_data.csv")
months = 0
money = 0
increase = 0
decrease = 0
#read csv
with open(resources_path) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_file)

    for row in csv_reader:
        months += 1
        money = money + int(row[1])
        if int(row[1]) > int(increase):
            increase = row[1]
            month_increase = row[0]
        
        if int(row[1]) < int(decrease):
            decrease = row[1]
            month_decrease = row[0]
print(months)
print(money)
print(increase)
print(month_increase)
print(decrease)
print(month_decrease)

