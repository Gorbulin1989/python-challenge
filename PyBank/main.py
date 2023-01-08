# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join("PyBank/resources/budget_data.csv")
# Set & Initialize variables
total_months = 0
total_profit = 0
previous_profit = 0
profit_change = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# read csv file
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    
    # skip the header row
    next(reader)

    # iterate through rows
    for row in reader:
        # get the values from the row
        month = row[0]
        profit = int(row[1])

        # update total months
        total_months += 1

        # update total profit
        total_profit += profit

        # update profit change
        profit_change = profit - previous_profit
        previous_profit = profit
        profit_changes.append(profit_change)

        # update greatest increase
        if profit_change > greatest_increase[1]:
            greatest_increase[0] = month
            greatest_increase[1] = profit_change

        # update greatest decrease
        if profit_change < greatest_decrease[1]:
            greatest_decrease[0] = month
            greatest_decrease[1] = profit_change

# calculate average profit change
average_change = sum(profit_changes[1:]) / (total_months - 1)

# print results
print("Financial Analysis")
print("-------------------------" +"\n")
print("Total months: " + str(total_months))
print("Total profit: " + "$" + str(total_profit))
print("Average change: " + "$" + str(round(average_change, 2)))
print("Greatest increase: " + str(greatest_increase[0]) + " " + "$" + str(greatest_increase[1]))
print("Greatest decrease: " + str(greatest_decrease[0]) + " " + "$" + str(greatest_decrease[1]))

# open text file in write mode
with open("results_PyBank.txt", "w") as textfile:
    # write results to the text file
    textfile.write( "Financial Analysis " +"\n",)
    textfile.write("Total months:" + str(total_months) + "\n")
    textfile.write("Total profit: " + "$" + str(total_profit) + "\n")
    textfile.write("Average change: " + "$" + str(round(average_change, 2)) + "\n")
    textfile.write("Greatest increase: " + str(greatest_increase[0]) + " " + "$" + str(greatest_increase[1]) + "\n")
    textfile.write("Greatest decrease: " + str(greatest_decrease[0]) + " " + "$" + str(greatest_decrease[1]) + "\n")
