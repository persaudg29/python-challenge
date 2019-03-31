"""
main.py is a program which parses statistical data from election_data.csv
"""
import csv as csv
pollfile = open("election_data.csv", "r") 

total_votes = 0

pollheader, *polldata = pollfile.readlines()  
dict_candidates = {"Khan": 0, 
    "Correy": 0,
    "Li": 0, 
    "O'Tooley": 0,} #empty dictionary for names, each name initially set to 0


for line in polldata:
    parts = line.split(",")
    candid = parts[2]
    total_votes += 1
    dict_candidates[candid[:-1]] += 1

print("Total Votes: " + str(total_votes))

#for key, value in d.items():
for candidname, votesper in dict_candidates.items():
    print(candidname + ": " + str((votesper/total_votes)*100) + "%(" + str(votesper) + ")")

