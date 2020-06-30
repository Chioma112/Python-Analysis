import os 
import csv
file_to_load=budget_data=os.path.join("Resources","budget_data.csv")

#Open and read csv
with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")


