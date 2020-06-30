import os
import csv

# set path
csvpath = os.path.join("election_data.csv")

# initialize variables

candidates = {}
number_votes = 0
candidate_options = []
winning_candidate = "" 
winning_count = 0

# open the file


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    for line in csvreader:
        number_votes = number_votes + 1
        candidate = line[2]

        if candidate in candidate_options:
            candidates[candidate] = candidates[candidate] + 1
        
        else:
            candidate_options.append(candidate)
            candidates[candidate]= 1
    
#print(candidates)
output_file = 'output.txt'

# open the output file for writing
with open(output_file, 'w') as text:
   
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {number_votes}')
    print('-------------------------')
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write(f'Total Votes: {number_votes}\n')
    text.write(f'-------------------------\n')
    # iterate through all of the winners to see if their number of votes is the highest
    winner = ''
    for possible_winner in candidates:
        final_votes = candidates[possible_winner]
        percentage =float(final_votes) / float(number_votes) * 100 # calculate the candidates percentage of votes
        #print(percentage)
        print (type(percentage))
        percentage_str = f'{percentage:.3f}'   # format the percentage with three decimal points
        print(f'{possible_winner}: {percentage_str}% ({final_votes})')
        text.write(f'{possible_winner}: {percentage_str}% ({final_votes})\n')
        if winner == '':
            winner = possible_winner    # default to the first candidate if there is no winner yet
        elif final_votes > candidates[possible_winner]:
            winner = possible_winner
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
    text.write(f'-------------------------\n')
    text.write(f'Winner: {winner}\n')
    text.write(f'-------------------------\n')
