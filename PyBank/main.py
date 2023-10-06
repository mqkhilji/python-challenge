import csv  # Required for reading CSV files
import os   # Required for joining paths

# Set the path for the CSV file
file_path = os.path.join("pyBank", "Resources", "budget_data.csv")

# Lists to store data
months = []
profit_losses = []

# Open and read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header

    for row in reader:
        months.append(row[0])  # Store month
        profit_losses.append(int(row[1]))  # Store profit/loss

# Calculate total number of months
total_months = len(months)

# Calculate net total amount of profit/losses
net_total = sum(profit_losses)

# Calculate changes in "Profit/Losses" from month to month
changes = []
for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

# Calculate average change
average_change = sum(changes) / len(changes)

# Determine greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the corresponding months for the greatest increase and decrease
month_greatest_increase = months[changes.index(greatest_increase)+1]
month_greatest_decrease = months[changes.index(greatest_decrease)+1]

# Create a list of results to print
results = [
    "Financial Analysis",
    "---------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})",
    f"Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})"
]

# Print results to the terminal
for line in results:
    print(line)

# Save the results to a text file
output_path = os.path.join("pyBank", "Resources", "pyBank_analysis.txt")
with open(output_path, 'w') as file:
    for line in results:
        file.write(line + "\n")
