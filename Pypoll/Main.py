#Import modules
import csv
import os

# create path to file
resources_path = os.path.join("Resources/" + "election_data.csv")
total = 0
votes = 0
canidates = []
totals = []
#read csv
with open(resources_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file) 

    for row in csv_reader:
        total += 1
        if row[2] not in canidates:
            canidates.append(row[2])
        
        for canidate in canidates:
            if row[2] == "Khan":
                votes += 1
            #totals.append(votes)
        
    
print(total)
print(canidates)
print(votes)