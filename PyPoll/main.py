
import os
import csv


# set path
csvpath = os.path.join("Resources", "election_data.csv")

# initialize variables

candidates = []
number_votes = 0
vote_counts = []
# open the file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csvheader}")
    line = next(csvreader,None)

    for line in csvreader:
        number_votes = number_votes + 1
        candidate = line[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        
        else:
            candidates.append(candidate)
            vote_counts.append(1)
