# Python Challenge - Financial and Voting Analysis

This repository contains Python scripts that analyze financial and voting datasets to generate insightful reports.

# Datasets:
1. Financial Data (budget_data.csv): Contains the financial records of a company, with two columns: "Date" and "Profit/Losses".
2. Election Data (election_data.csv): Consists of vote records, with three columns: "Voter ID", "County", and "Candidate".


PyBank (main.py inside PyBank folder): Analyzes the financial records to provide:

- Total number of months in the dataset.
- Net total amount of "Profit/Losses" over the entire period.
- Average change in "Profit/Losses" over the entire period.
- Greatest increase in profits (date and amount) over the entire period.
- Greatest decrease in profits (date and amount) over the entire period.

Financial Analysis
---------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)




PyPoll (main.py inside PyPoll folder): Analyzes the voting records to determine:

- Total number of votes cast.
- List of candidates who received votes.
- Percentage of votes each candidate won.
- Total number of votes each candidate won.
- Winner of the election based on popular vote.

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
