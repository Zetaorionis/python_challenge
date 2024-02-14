import os
import csv
 
ELECTION_CSV_DATA_PATH = os.path.join("Resources", "election_data.csv")
ANALYSIS_PATH = os.path.join("analysis", "results.txt")
 
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(ELECTION_CSV_DATA_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
 
    total_votes = 0
    candidates = []
    candidates_votes= {}
    first_place_candidate = ''
    first_place_vote_count = 0
 
    for row in csvreader:
        # finding the total number of votes casted
        total_votes += 1
 
        # defining the begining of the csv data for votes and candidates
        current_vote = row[0]
        current_canadate = row[2]
 
         # A complete list of candidates who received votes
        if current_canadate not in candidates:
            candidates.append(current_canadate)
            candidates_votes[current_canadate]= 0
        candidates_votes[current_canadate] += 1
 
# write information to text file        
with open(ANALYSIS_PATH, "w") as output_file:
    output = (
        "Election Results\n"
        "----------------------------\n"
        f"Total votes: {total_votes}\n"
        "----------------------------\n")
    print(output)
    output_file.write(output)
 
    #  finding the percentage of votes each candidate won
    for current_canadate in candidates_votes:
        votes = candidates_votes[current_canadate]
        vote_percentage = float(votes) / float(total_votes)*100
        individual_results = (f"{current_canadate}: {vote_percentage:.3f}% ({votes})\n")
 
        # write information to text file
        print(individual_results)
        output_file.write(individual_results)
       
        # finding winners name
        if votes > first_place_vote_count:
            first_place_vote_count = votes
            first_place_candidate = current_canadate
    # write information to text file        
    winner = (f"Winner : {first_place_candidate}")
    print(winner)
    output_file.write(winner)
