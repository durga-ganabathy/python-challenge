# Create file paths across operating system
import os
# Module to read csv file
import csv

# from datetime import date

# Path to collect the data from the Resource folder
csvpath = os.path.join("..", "Resources", "budget_data.csv")

count_months = 0
total_amount = 0
change = 0
profit_loss_change = []
average_change = []
dates = []

with open(csvpath, encoding='UTF-8') as csvfile:
     # Split data on commas
     csvreader = csv.reader(csvfile, delimiter= ",")
     # To read the header row first
     csv_header = next(csvreader)

     for row in csvreader:
        #  Financial calculations
        # Total number of months included in the dataset    
         count_months = count_months + 1

        # The net total amount of Profit/Losses over the entire period    
         total_amount = total_amount + int(row[1])

        # Appending the Date column from the dataset to a list for calculations    
         dates.append(row[0])
         

        #  profit_loss_final = 0
        #  profit_loss_change = int(row[1])
         
        # The changes in Profit/Losses over the entire period calculated by subracting the current month value from previous month value and excluding the first value of profit/loss change
         
         profit_loss_final = int(row[1]) - change
         change = int(row[1])
        #  print(f'profit_loss_final {profit_loss_final}')
        #  print(f'change {change}')
         profit_loss_change.append(profit_loss_final)
        #  print(f'profit_loss_change {profit_loss_change}')
         
         
         
profit_loss_change[0] = 0

# To calculate average of changes in Profit/Losses
average_change = sum(profit_loss_change)/(len(profit_loss_change)-1)

# The given csv file has Date column(row 0) in year-month format so to convert it to month-year format to match the financial analysis report provided (reference from 'stackoverflow')

# If I run my code directly from the provided CSV file there is no need for the below Dateformat since I used SaveAs CSV the Date column was in year-month format I used the below line of code
dates = ['{}-{}'.format(m,y) for y, m in map(lambda x: str(x).split('-'), dates)]

# The greatest increase in Profits (date and amount) over the entire period
greatest_increase_profit = max(profit_loss_change)
greatest_increase_date = dates[profit_loss_change.index(greatest_increase_profit)]

# The greatest decrease in Profits (date and amount) over the entire period
greatest_decrease_profit = min(profit_loss_change)
greatest_decrease_date = dates[profit_loss_change.index(greatest_decrease_profit)]

# To print the results in the terminal

print('Financial Analysis')

print("----------------------------")

# print(f'dates {dates}')
print(f'Total Months : {count_months}')
print(f'Total: ${total_amount}')
# Rounding the value to 2 decimals
print(f'Average Change: ${round(average_change,2)}')
# print(round(average_change,2))
# print(f'greatest increase in profit {greatest_increase_profit}')
# print(f'greatest decrease in profits: {greatest_increase_date}  (${greatest_decrease_profit})')
print(f'Greatest Increase in Profits: {greatest_increase_date}  (${greatest_increase_profit})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date}  (${greatest_decrease_profit})')


# To export a text file with results printed

output_file = os.path.join("..","analysis", "pybank.txt")
with open(output_file, 'w', newline='') as text:
     text.write('Financial Analysis \n')

     text.write("----------------------------\n")

     text.write(f'Total Months : {count_months}\n')
     text.write(f'Total: ${total_amount}\n')
     text.write(f'Average Change: ${round(average_change,2)}\n')
     text.write(f'Greatest Increase in Profits: {greatest_increase_date}  (${greatest_increase_profit})\n')
     text.write(f'Greatest Decrease in Profits: {greatest_decrease_date}  (${greatest_decrease_profit})\n')


 