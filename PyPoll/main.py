import os
import csv

winner_vote_number = 0
winner_name = ""
candidate_list = []
vote_dic ={}
counter_winner = 0


print ("Election Results")
print ("--------------------------")

# Set path for file
csvpath = os.path.join("../..", "COLNYC20190716DATA", "02-Homeworks", "03-Python",
 "Instructions", "PyPoll", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath,newline = None) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

     # skips the headr line 
    csv_header = next(csvreader)
    rows = [rows for rows in csvreader]

    # counting the Total Votes
    vote_count = sum(1 for row in rows)
    print ("Total Votes: " + str(vote_count))
    print ("--------------------------")
    
    # A complete list of candidates who received votes
    for row in rows:
       
        # setting current_candidate to the col in the data
        current_candidate = row[2]

        if (current_candidate not in candidate_list):
            candidate_list.append(current_candidate)
            vote_dic[current_candidate] = 0

        vote_dic[current_candidate] = vote_dic[current_candidate] + 1
    
   
    # looping indir the dic
    for candidate in vote_dic:
        
        votes_for_candidate = vote_dic.get(candidate)
        

        if (votes_for_candidate > winner_vote_number):
            winner_vote_number = winner_vote_number + votes_for_candidate


        
        print(candidate + ": " + "% " + str(round(float(votes_for_candidate)/float(vote_count)*100,3)) + " (" + str(votes_for_candidate) + ")")
    print ("--------------------------")
    
    for name, vote in vote_dic.items():   
        if vote == winner_vote_number:
            winner_name = name

    # the winner 
    print ("Winner: " + str(winner_name))
    print ("--------------------------")

    # exportnig the file 
    with open("Output_for_PyPoll.txt", "w") as text_file:
        text_file.write ("Election Results")
        text_file.write("\n")
        text_file.write ("--------------------------")
        text_file.write("\n")
        text_file.write ("Total Votes: " + str(vote_count))
        text_file.write("\n")
        text_file.write ("--------------------------")
        text_file.write("\n")
        

        for candidate in vote_dic:
            votes_for_candidate = vote_dic.get(candidate)
            text_file.write(candidate + ": " + "% " + str(round(float(votes_for_candidate)/float(vote_count)*100,3)) + " (" + str(votes_for_candidate) + ")")
            text_file.write("\n")
        text_file.write ("--------------------------")
        text_file.write("\n")
        text_file.write("Winner: " + str(winner_name))
        text_file.close()
















