#import dependencies
import csv
import os
import operator

#get path of PayPoll.csv
PyPoll_Path = os.path.join("Resources","election_data.csv" )
#create path for to export data to a text file
PyPoll_Results = os.path.join("Analysis","election_results.csv")

#lists and variables to store election_data.csv column data
Voter_ID=[]
County = []
Candidate=[]
election_county={}
election_voter={}
percentages={}
winner=""
num_votes ={}
#get unique candidate name

def candidate_name(name):
    #if candidate is no in list append list
    if not name in Candidate:
        Candidate.append(name)
#get voter_id and county for candidate

#updates dictionaries that store each candidates vote and county won
def voter_and_county(voter,county,name):
    #for each candidate get the vote and county they got and store it a dictionary
    election_voter.setdefault(name,[]).append(voter)
    election_county.setdefault(name,[]).append(county)

#winning candidate 
def winner_chicken_dinner():
    #loops through each candidates votes to find the one with most votes
    for name in election_voter:
        num_votes.update({name:len(election_voter[name])})
    return max(num_votes.items(), key=operator.itemgetter(1))[0]
    
#calculates percentages of votes each candidate won
def vote_percentages():
    for name in Candidate:
        percent = round((float(len(election_voter[name])/len(Voter_ID))*100),3)
        print(percent)
        percentages.setdefault(name,[]).append(percent)
        
#writes a financial analysis data to a text file and in the terminal
def write_txt_file():
    winner=winner_chicken_dinner()
    vote_percentages()
    with open(PyPoll_Results,"w+") as txt:
        txt.write("'''text\nElection Results\n----------------------------\n")
        txt.write(f"Total Votes: {len(Voter_ID)}\n")
        txt.write('----------------------------\n')
        for name in Candidate:
            txt.write(f"{name}: {percentages[name][0]}% ({num_votes[name]})\n")
        txt.write('----------------------------\n')
        txt.write(f"Winner: {winner}\n")
        txt.write('----------------------------\n')
        txt.write("'''")

#open PyPoll_Path
with open(PyPoll_Path) as PyPoll_File:
    #read file and separate items by comma
    PyPoll_Reader = csv.reader(PyPoll_File, delimiter=',')
    
   

    #remove header
    PyPoll_Header = next(PyPoll_Reader)
    PyPoll_Header

    #loop through each row of the PyPoll data
    for row in PyPoll_Reader:
        #store row data into its corresponding lists
        Voter_ID.append(row[0])
        candidate_name(row[2])
        voter_and_county(row[0],row[1],row[2])

write_txt_file()