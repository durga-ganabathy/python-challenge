# Create file paths across operating system
import os
# Module to read csv file
import csv

# Path to collect the data from the Resource folder
pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

count_votes = 0
candidate_list = []
candidates = []
candidate_votes = []
percentage_votes = []

with open(pypoll_csv, encoding='UTF-8') as csvfile:
    # Split data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    # To read the header row first
    csv_header = next(csvreader)

    for row in csvreader:
        # Total number of votes cast
        count_votes = count_votes + 1
        candidate_list.append(row[2])
    
    # Complete list of candidates who received votes
    for name in candidate_list:
        if name not in candidates:
            candidates.append(name)

          # Total number of votes each candidate won
            vote_count = candidate_list.count(name)
            candidate_votes.append(vote_count)

          # Percentage of votes each candidate won
            percent_votes = (vote_count/count_votes) * 100
            percentage_votes.append(percent_votes)
          # Rounding the value to three decimals 
            percentage_votes = [round(value,3) for value in percentage_votes]

          # The winner of the election based on popular vote
            winner_votes = max(candidate_votes)
            winner = candidates[candidate_votes.index(winner_votes)]   

# To print the results in the terminal
print('Election Results')

print('----------------------------')

print(f'Total Votes: {count_votes}')
print('----------------------------')
# print(f'candidate list: {candidate_list}')
# print(f'candidates names {candidates}')
# print(f'candidate votes {candidate_votes}')
# print(f'percentage votes {percentage_votes}')

for i in range(len(candidates)):
    print(f'{candidates[i]}: {str(percentage_votes[i])}% ({str(candidate_votes[i])})')
          
print('----------------------------')
print(f'Winner: {winner}')
print('----------------------------')

#  To export a text file with results printed 
output_file = os.path.join("..", "analysis", "pypoll.txt")

with open(output_file, 'w', newline='') as text:

  text.write('Election Results \n')

  text.write('---------------------------- \n')

  text.write(f'Total Votes: {count_votes} \n')

  text.write('---------------------------- \n')

  for i in range(len(candidates)):
    text.write(f'{candidates[i]}: {str(percentage_votes[i])}% ({str(candidate_votes[i])}) \n')
  text.write('---------------------------- \n')
    
  text.write(f'Winner: {winner} \n')

  text.write('---------------------------- \n')