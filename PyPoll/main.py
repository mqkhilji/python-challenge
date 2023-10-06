import csv
import os

# Set up the path to your data file
file_path = os.path.join("pyPoll", "Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}

# Open and read the CSV file
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    # For each row in the file, count the votes
    for row in reader:
        candidate_name = row[2]
        total_votes += 1

        # If the candidate is not in our candidates dictionary, add them with 1 vote.
        # If they are already in our dictionary, add 1 to their vote count.
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Find the candidate with the most votes
winner = max(candidates, key=candidates.get)

# Print out the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a file
output_file = os.path.join("pyPoll", "Resources", "election_results.txt")
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
