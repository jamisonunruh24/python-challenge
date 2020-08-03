#Import modules
import csv
import os

# create path to file
resources_path = os.path.join("Resources/" + "budget_data.csv")
months = 0
money = 0
#read csv
with open(resources_path) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_file)

    for row in csv_reader:
        months += 1
        money = money + int(row[1])
print(months)
print(money)

