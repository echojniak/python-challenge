# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

import os

# Module for reading CSV files
import csv


# Module for reading CSV files
csvpath = os.path.join( 'Resources', 'election_data.csv')
total_votes = 0
candidate_list = []
candidate_name = []
candidate_vote = {}






with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}") 

  

 
        

    # Read each row of data after the header
    for row in csvreader:
         total_votes  += 1
         candidate_name = row[2]
         candidate_list.append(candidate_name)
    
        # print(row)
         
    # votes count for each candidate
         if candidate_name in candidate_vote:
             candidate_vote[candidate_name] += 1
         else: 
              candidate_vote[candidate_name] = 1

    # The winner of the election through the dictionery
    winner = None
    max_votes = 0
    for candidate, votes in candidate_vote.items():
        if votes > max_votes:
            winner = candidate
            max_votes = votes


   
#print(total_votes)

#print("\nList of Candidates:")
for candidate in set(candidate_list):
   # print(candidate)
    for candidate, votes in candidate_vote.items():
     percentage = (votes/total_votes)*100
     
   # print(f"{candidate}: {percentage:.3f}% ({votes} votes)")

for candidate, votes in candidate_vote.items():
    #print(f"{candidate}: {votes} votes")
 
#print("\nWinner of the Election:")
#print(f"{winner}")



 out_text =(
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"Charles Casper Stockham: {candidate_vote.get('Charles Casper Stockham', 0)/total_votes*100:.3f}% ({candidate_vote.get('Charles Casper Stockham', 0)})\n"
    f"Diana DeGette: {candidate_vote.get('Diana DeGette', 0)/total_votes*100:.3f}% ({candidate_vote.get('Diana DeGette', 0)})\n"
    f"Raymon Anthony Doane: {candidate_vote.get('Raymon Anthony Doane', 0)/total_votes*100:.3f}% ({candidate_vote.get('Raymon Anthony Doane', 0)})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n" 

 )

print(out_text)
 # Specify the file to write to
output_path = os.path.join( "analysis", "election_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write(out_text)
    


