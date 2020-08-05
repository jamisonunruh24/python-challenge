#Import modules
import csv
import os

# create path to file
resources_path = os.path.join("Resources/" + "election_data.csv")

canidates = []
totals = []
votes = []
#read csv
with open(resources_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file) 

    for row in csv_reader:

        totals.append(row[2])

        if row[2] not in canidates:
            canidates.append(row[2])    
        
    for canidate in canidates:
        tally = 0
        for vote in totals:
            if canidate == vote:
                tally += 1
        votes.append(tally)
        
          
print(canidates)    
print(len(totals))
print(votes)