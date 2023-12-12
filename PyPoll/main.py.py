# import modules
import os
import csv

# path to file
csvpath = os.path.join(".", "Resources", "election_data.csv")

# variable lists
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Open election file and read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # this will skip the first line for iteration, which is the header

    # Go through the file, line by line to populate the values from the columns
    for row in csvreader:
        total_votes += 1

        # Count votes for each candidate
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

            # Check if the current candidate has more votes than the current winner
            if candidates[candidate_name] > winner["votes"]:
                winner["name"] = candidate_name
                winner["votes"] = candidates[candidate_name]

# Print the analysis results
print_file = (f"Election Results\n"
                 f"---------------------\n"
                 f"Total Votes: {total_votes}\n"
                 f"---------------------\n")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print_file += f"{candidate}: {'{:.3f}%'.format(percentage)} ({votes})\n"

print_file += (f"---------------------\n"
                  f"Winner: {winner['name']}\n"
                  f"---------------------\n")

print(print_file)

# Create output file for the analysis report
output_file = os.path.join("PyPoll_Output.txt")
with open(output_file, "w") as the_file:
    the_file.write(print_file)
