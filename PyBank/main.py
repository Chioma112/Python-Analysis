import os 
import csv

budget_data = os.path.join("Resources","budget_data.csv")

    
    #Iniatialize the variable
dates = []
profit_losses = []
amount = []

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)
    #print(f"CSV Header: {csvheader}")
    
    for i in csvreader:
        dates.append(i[0])
        profit_losses.append(i[1]) 
        #print(i[0],i[1])
       
 #The total number of months included in the dataset
total_months=len(dates)
#print (f"Total Months: {total_months}")

#The net total amount of "Profit/Losses" over the entire period
net_total = 0 
for Total in profit_losses:
    net_total= net_total + int(Total)
#print(f"Total: {net_total}") 

#The average of the changes in "Profit/Losses" over the entire period
changes=[]
for i in range(len(profit_losses)-1):
    amount= int(profit_losses[i+1])- int(profit_losses[i])
    #averge_change += changes
    changes.append(amount)
Average_change = round (sum(changes)/len(changes),2)

#The greatest increaese in profits (date and amount) over the entire period

greatest_profit_value=max(changes)
greatest_profit_increase=dates[changes.index(max(changes))+1]
#print(f'Greatest Increase in profits: {greatest_profit_increase} (${greatest_profit_value})')

#The greatest decrease in losses (date and amount) over the entire perio
lowest_profit_value=min(changes)
greatest_profit_decrease=dates[changes.index(min(changes))+1]
#print(f'Greatest Decrease in profits: {greatest_profit_decrease} (${lowest_profit_value})')

#   print the results

print('Financial Analysis')
print('----------------------------')
print (f"Total Months: {total_months}")
print(f"Total: {net_total}") 
print(f'Average Change: ${Average_change}')
print(f'Greatest Increase in profits: {greatest_profit_increase} (${greatest_profit_value})')
print(f'Greatest Decrease in profits: {greatest_profit_decrease} (${lowest_profit_value})')

#write results out to output file
output_file = 'output.txt'

with open(output_file,'w') as text:

    # add line break at the end of each line so that each write writes to a new line
    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {total_months}\n')
    text.write(f'Total: ${net_total}\n')
    text.write(f'Average Change: ${Average_change}\n')
    text.write(f'Greatest Increase in profit: {greatest_profit_increase} (${greatest_profit_value})\n')
    text.write(f'Greatest Decrease in profit: {greatest_profit_decrease} (${lowest_profit_value})\n')