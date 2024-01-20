# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
total_months = 0
profit_losses = 0
change_list = []
months_list = []



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    

    # Read each row of data after the headert
    for row in csvreader:
        # print(row)
        total_months += 1
        months_list.append(row[0])
        profit_losses += int(row[1])
        if total_months > 1:
            change = int(row[1]) - prev_value
            change_list.append(change)
        prev_value =  int(row[1])
#print(total_months)
#print(profit_losses)
avg_ch = round (sum (change_list)/len(change_list),2)
#print(avg_ch)
max_pl = max(change_list)
min_pl = min(change_list)
#print(max_pl,min_pl)
max_index = change_list.index(max_pl)
min_index = change_list.index(min_pl)
max_month = months_list[max_index + 1]
min_month = months_list[min_index + 1]
#print(max_month,min_month)



out_text = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${profit_losses}\n"
f"Average Change: ${avg_ch}\n"
f"Greatest Increase in Profits: {max_month} (${max_pl})\n"
f"Greatest Decrease in Profits: {min_month} (${min_pl})"
)
print(out_text)

# Specify the file to write to
output_path = os.path.join( "analysis", "budget_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write(out_text)
