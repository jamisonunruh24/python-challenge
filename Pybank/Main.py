#Import modules
import csv
import os

# create path to file
resources_path = os.path.join("Resources/" + "budget_data.csv")

#read csv
with open(resources_path) as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)


