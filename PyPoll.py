import os
import csv

election_csv = os.path.join(r"C:\Users\jimmy\Downloads\Module_3\PyPoll\Resources\election_data.csv")

ballot_list = []
unique_candidates = []

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        # Assigning column values to a new variable
        candidate = row[2]
        # Append each unique candidate to an array
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
            ballot_list.append(0)
        # Counting the number of votes for each candidate
        ballot_list[unique_candidates.index(candidate)] +=1

#    The total number of votes cast
total_votes = ballot_list[0] + ballot_list[1] + ballot_list[2]

#    The number of votes each candidate won
candidate1_votes = ballot_list[0]
candidate2_votes = ballot_list[1]
candidate3_votes = ballot_list[2]

#    The percentage of votes each candidate won
candidate1_percent = format(candidate1_votes / total_votes * 100, '.3f')
candidate2_percent = format(candidate2_votes / total_votes * 100, '.3f')
candidate3_percent = format(candidate3_votes / total_votes * 100, '.3f')

#    Identifying the winner based on popular vote
max_votes = max(ballot_list)
index_winner = ballot_list.index(max_votes)
winner_name = unique_candidates[index_winner]

#Election Analysis Output
print("")
print("----------------------------------------------------------------------------------------------------")
print("Election Results [PyPoll]")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
print(f'{unique_candidates[0]}: {candidate1_percent}% ({candidate1_votes})')
print(f'{unique_candidates[1]}: {candidate2_percent}% ({candidate2_votes})')
print(f'{unique_candidates[2]}: {candidate3_percent}% ({candidate3_votes})')
print("-------------------------")
print(f'Winner: {winner_name}')