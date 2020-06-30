# First we'll import the os module
# This will allow us to create file paths across operating systems
import os 
# Module for reading CSV files
import csv

budget_data = os.path.join("Resources","budget_data.csv")
#csvpath= "Resources"/"budgetdata"
#Open and read csv
with open(budget_data) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile, delimiter=",")

    #print(csvreader)
    #Read header row first 
    csv_header =next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        print(row)
    #The total number of months included in the dataset
    Total_Months={"Date": 82}







