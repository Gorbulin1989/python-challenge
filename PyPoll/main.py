# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join("PyPoll/resources/election_data.csv")
# initialize variables
total_votes = 0
candidates = {}

# read csv file
with open(csvpath) as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # skip the header row
    next(reader)

    # Loop through the rows in the CSV file
    for row in reader:
        # Increment the total number of votes
        total_votes += 1
        
        #Get the candidate's name from the row
        candidate = row[2]

      # If the candidate is not in the dictionary, add them with a vote count of 1
        if candidate not in candidates:
            candidates[candidate] = 1
        # Otherwise, increment their vote count
        else:
            candidates[candidate] += 1



# Determine the winner of the election
winner = max(candidates, key=candidates.get)
# Print results
print("Election Results" + "\n")
print("-----------"+ "\n")
print("Total Votes:  " + str(total_votes)+ "\n")
print("-----------"+ "\n")
# Calculate the percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = votes / total_votes * 100
    print(f'{candidate}: {percentage:.3f}% ({votes} votes)' +"\n")
print("------------"+ "\n")
print(f'Winner : {winner}'+"\n")
print("------------"+ "\n")

# open text file in write mode
with open("results.txt", "w") as textfile:
    # write results to the text file
    textfile.write("Election Results" + "\n")
    textfile.write("Total Votes:" + str(total_votes) + "\n")

    for candidate, votes in candidates.items():
        percentage = votes / total_votes * 100
        textfile.write(f'{candidate}: {percentage:.3f}% ({votes} votes)' +"\n")
    textfile.write(f'Winner : {winner}'+"\n")