import os
import csv
 
BUDGET_CSV_DATA_PATH = os.path.join("Resources", "budget_data.csv")
ANALYSIS_PATH = os.path.join("analysis", "results.txt")
 
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(BUDGET_CSV_DATA_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
   
    ##### The Total # of Months included in the dataset
    months = 0
    total_profit = 0
    total_change = 0
    greatest_increase_month = ''
    greatest_decrease_month = ''
    greatest_increase_profit = 0
    greatest_decrease_profit = 0
   
    previous_profit = None
    for row in csvreader:
 
        months += 1
 
        current_month = row[0]
        current_profit = int(row[1])
       
        #### The net total amount of "Profit/Losses" over the entire period
        total_profit = total_profit + current_profit    
     
        #### The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if previous_profit is not None:
            current_change = current_profit - previous_profit
            total_change += current_change
            if current_change > greatest_increase_profit:
                greatest_increase_month = current_month
                greatest_increase_profit = current_change
            elif current_change < greatest_decrease_profit:
                greatest_decrease_month = current_month
                greatest_decrease_profit = current_change
        previous_profit = current_profit
 
   
    average_change = round(total_change / (months-1), 2)
 
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: {total_profit}\n"
    f"Average Change: $ {average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month}  (${greatest_increase_profit})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})"
)
#### Export result to text file
with open(ANALYSIS_PATH, "w") as output_file:
    output_file.write(output)
    print(output)