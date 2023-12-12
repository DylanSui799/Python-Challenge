# import modules
import os
import csv

# path to file
csvpath = os.path.join(".","Resources", "budget_data.csv")

# variable lists
total_months = []
total_amount = []

# Open budget file and read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # this will skip the first line for iteration, which is the header

    # Go through the file, line by line to populate the values from the columns
    for row in csvreader:
        total_months.append(row[0])  
        total_amount.append(int(row[1]))  

# The total number of months in the dataset
number_of_months = len(total_months)

# Total number of amount
net_total = sum(total_amount)

# Calculate the changes in "Profit/Losses" over the entire period
profit_changes = [total_amount[i + 1] - total_amount[i] for i in range(len(total_amount) - 1)]

# The average of the changes in "Profit/Losses"
average_changes = sum(profit_changes) / len(profit_changes)

# The greatest increase in profits over the entire period
largest_increase_amount = max(profit_changes)
largest_increase_index = profit_changes.index(largest_increase_amount)
largest_increase_date = total_months[largest_increase_index + 1]  # Adding 1 to get the next month

# The greatest decrease in profits over the entire period
largest_decrease_amount = min(profit_changes)
largest_decrease_index = profit_changes.index(largest_decrease_amount)
largest_decrease_date = total_months[largest_decrease_index + 1]  # Adding 1 to get the next month

# Print the analysis results
print_to_file = (f"Financial Analysis\n"
                 f"---------------------\n"
                 f"Total Months: {number_of_months}\n"
                 f"Total: ${net_total}\n"
                 f"Average Change: ${'{:.2f}'.format(average_changes)}\n"
                 f"Greatest Increase in Profits: {largest_increase_date} (${largest_increase_amount})\n"
                 f"Greatest Decrease in Profits: {largest_decrease_date} (${largest_decrease_amount})\n")

print(print_to_file)

# Create output file for the analysis report
output_file = os.path.join("PyBank_Output.txt")
with open(output_file, "w") as the_file:
    the_file.write(print_to_file)
