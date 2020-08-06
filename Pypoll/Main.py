#Import modules
import csv
import os

# create path to file
resources_path = os.path.join("Resources/" + "election_data.csv")

canidates = []
totals = []
votes = []
percents = []
winner = []
win = 0
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

    for percentage in votes:
        percent = "{:.0%}".format(percentage / len(totals))
        percents.append(percent)

#print to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: " + str(len(totals)))
print("-------------------------")
for x in range(len(canidates)):
    print(f"{canidates[x]}: {percents[x]} ({votes[x]})")
    if votes[x] > win:
        win = votes[x]
        win_can = canidates[x]
print("-------------------------")
print(f"Winner: " + win_can)
print("-------------------------")

#print to analysis
#write to file
with open("analysis/PyPollAnalysis.txt", "w") as analysis:
    analysis.write("Election Results\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Total Votes: " + str(len(totals))+ "\n")
    analysis.write("-------------------------\n")
    for x in range(len(canidates)):
        analysis.write(f"{canidates[x]}: {percents[x]} ({votes[x]})\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Winner: " + win_can + "\n")
    analysis.write("-------------------------\n")
