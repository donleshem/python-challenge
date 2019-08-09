import os
import csv

candidate_list = []
vote_dic ={}
counter = 0
winner = ""


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
        if (row[2] not in candidate_list):
            candidate_list.append(row[2])
            vote_dic[candidate_name] = 0
        vote_dic[candidate_name] = vote_dic[candidate_name] + 1
   
        
    #vote_dic = {candidate_list[i] for i in range(0, len(candidate_list) ) }
    #print (vote_dic)











