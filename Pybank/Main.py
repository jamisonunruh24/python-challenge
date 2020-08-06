#Import modules
import csv
import os

# create path to file
resources_path = os.path.join("Resources/" + "budget_data.csv")
months = []
money = 0
prevmoney = 0
curmoney = 0
change = 0
increase = 0
decrease = 0
#read csv
with open(resources_path) as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_header = next(csv_file)

    for row in csv_reader:
        months.append(row[0])
        money = money + int(row[1])
        curmoney = int(row[1])
        if prevmoney != 0:
            change = change + (prevmoney - curmoney)        
        prevmoney = int(row[1])
        if int(row[1]) > int(increase):
            increase = row[1]
            month_increase = row[0]
        
        if int(row[1]) < int(decrease):
            decrease = row[1]
            month_decrease = row[0]
average_change = "{0:.2f}".format(-(change / (int(len(months)) - 1)))

#print out in terminal
print("Financial Analysis")
print("------------------------------")
print(f"Total months: " +str(len(months)))
print(f"Total: $" + str(money))
print(f"Average Change: $" + str(average_change))
print(f"Greates increase in Profits: " + month_increase + " " + str(increase))
print(f"Greates decrease in Profits: " + month_decrease + " " + str(decrease))

#write to file
with open("analysis/PyBankAnalysis.txt", "w") as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("------------------------------\n")
    analysis.write(f"Total months: " +str(len(months))+"\n")
    analysis.write(f"Total: $" + str(money)+"\n")
    analysis.write(f"Average Change: $" + str(average_change)+"\n")
    analysis.write(f"Greates increase in Profits: " + month_increase + " " + str(increase)+"\n")
    analysis.write(f"Greates decrease in Profits: " + month_decrease + " " + str(decrease)+"\n")