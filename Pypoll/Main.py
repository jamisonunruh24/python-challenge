#Import modules
import csv
import os

# create path to file
resources_path = os.path.join("Resources/" + "election_data.csv")
total = 0
canidate = []
#read csv
with open(resources_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file) 

    for row in csv_reader:
        total += 1
        if row[2] not in canidate:
            canidate.append(row[2])
print(total)
print(canidate)