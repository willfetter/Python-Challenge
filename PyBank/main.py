# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import os
import csv

# Path to collect data from the Resources folder
budgetdata = os.path.join("Resources", "budget_data.csv")
# Path to output data into 'Analysis'folder
financial_Analysiscsv = os.path.join("Analysis", "financial_analysis.txt")

#create lists
months = [] 
plcount = []
nettotal = []
change = []

#initialize variables 
nettotal = 0

#open and read the .csv file
with open(budgetdata) as csvfile: #allow, so it can be prepared to store reference above for processing
    csvreader = csv.reader(csvfile, delimiter=",")
    #the first row is header, use next() to bypass header
    csv_header = next(csvreader)

    #for loop to read data after header for each row 
    for row in csvreader:
        months.append(row[0]) #adds to month rows
        plcount.append(int(row[1])) #adds to PL rows
        nettotal = nettotal + int(row[1]) #adds to total overal profit / loss

    #create for loop to determine change in profit and loss 
    for i in range (1, len(plcount)):
        change.append((int(plcount[i] - int(plcount[i-1]))))

    #average change is sum of changes 'sum(plchange)' divided by count of changes len(plchange)
    average_change = round(sum(change) / len(change),2) #use 'round' to rounnd number to 2 decimal places
   
    #calculate the total number of months in first column
    totalmonths = len(months)

    #calculate the greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(change)
    greatest_increase_date = str(months[change.index(max(change)) + 1])
    

    #calculate the greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = min(change)
    greatest_decrease_date = str(months[change.index(min(change)) + 1])

#display the results according to the format
print("\n---------------------------------------------------\n")
print("Financial Analysis\n")
print("---------------------------------------------------\n")
print(f"Total Months: " + str(totalmonths))
print(f"Total: $" + str(nettotal))
print(f"Average Change: $" + str(average_change))
print(f"Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")")
print(f"Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")")

#print same data to output file
with open(financial_Analysiscsv, "w") as textfile:
    
        #variable to hold the output
        output = ""
        output += "-----------------------------------------------------------\n"
        output += f"\n\nFinancial Analysis\n"
        output += "-----------------------------------------------------------\n\n"
        output += f"Total Months: " + str(totalmonths) + "\n"
        output += f"Total: $" + str(nettotal) + "\n"
        output += f"Average Change: $" + str(average_change) + "\n"
        output += f"Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")" + "\n"
        output += f"Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")"  + "\n"
        output += "-----------------------------------------------------------\n"

        #write the data to the output textfile
        textfile.write(output)
