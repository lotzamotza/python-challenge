import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidate_set = set()
candidate_list = list()
candidate_dict = dict()

with open(csvpath, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = (next(csvreader))

    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        total_votes += 1
        candidate_set.add(candidate)
        candidate_list.append(candidate)
    
with open("election_data.txt", "w") as file:
    print("Election Results")
    file.write("Election Results \n")
    print("------------------------------------")
    file.write("------------------------------------\n")
    print("Total Votes:", total_votes)
    file.write(f"Total Votes: , {total_votes} \n")
    print("------------------------------------")
    file.write("------------------------------------ \n")
    
    for i in candidate_set:
        print(f"{i}: {round((candidate_list.count(i) / len(candidate_list))*100,3)}%, ({candidate_list.count(i)})")
        file.write(f"{i}: {round((candidate_list.count(i) / len(candidate_list))*100,3)}%, ({candidate_list.count(i)}) \n")
        candidate_dict[i] = candidate_list.count(i)
    print("------------------------------------")
    file.write("------------------------------------ \n")
    print(f"Winner: {max(candidate_dict, key=candidate_dict.get)}")
    file.write(f"Winner: {max(candidate_dict, key=candidate_dict.get)} \n")
    print("------------------------------------")
    file.write("------------------------------------\n")