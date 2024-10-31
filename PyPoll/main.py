# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

import os
import csv
from unittest import result

# Path to collect data from the Resources folder
electiondata = os.path.join("Resources", "election_data.csv")
# Path to output data into same folder
election_resultscsv = os.path.join("Analysis", "election_results.txt")

#create lists
votes = [] 
candidate = []

#create dictionaries
vote_counts = {}

#initialize variables 
totalvotes = 0
winner = ""

#open and read the .csv file
with open(electiondata) as csvfile: #allow, so it can be prepared to store reference above for processing
    csvreader = csv.reader(csvfile, delimiter=",")
    #the first row is header, use next() to bypass header
    csv_header = next(csvreader)

    #for loop to read data after header for each row 
    for row in csvreader:
        
        # Determine The total number of votes cast
        totalvotes = sum(vote_counts.values())
        candidate = row[2] #candidate is in index 2

        #for each candidate, add votes
        if candidate in vote_counts: 
              vote_counts[candidate] += 1
        else:
              vote_counts[candidate] = 1

    #determine overall winner
    winner = max(vote_counts, key=vote_counts.get) #returns candidate with max vote counts from dictonary 'vote_counts

#display the results according to the format
print("\n")
print("Election Results\n")
print("-------------------------\n")
print(f"Total Votes: " + str(totalvotes))
print("-------------------------\n")
#display the results for each candidate according to the format
for candidate, votes in vote_counts.items():
       vote_percentage = (votes / totalvotes) * 100
       print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
print("-------------------------\n")
#display the overall winner 
print(f"Winner: {winner}")
print("-------------------------\n")

#export a text file with the results 
with open(election_resultscsv, "w") as textfile:
        #variables to hold the output
        output = ""
        output += "\nElection Results\n"
        output += "-------------------------\n"
        output += f"Total Votes: " + str(totalvotes)
        output += "\n-------------------------\n"
        for candidate, votes in vote_counts.items():
              vote_percentage = (votes / totalvotes) * 100
              output +=f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        output += "-------------------------\n"
        output += f"Winner: {winner}\n"
        output += "-------------------------\n"

        #write the data to the output textfile
        textfile.write(output)