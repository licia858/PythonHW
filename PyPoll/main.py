import os
import csv

#example of data
#Voter ID,County,Candidate
#12864552,Marsh,Khal
pypollcsv = os.path.join('..','..','02-Homework','03-Python','Instructions','PyPoll','Resources','election_data.csv')



#def election(cannames):
   
  # print(cannames.count)
   #print(set(cannames))

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

with open(pypollcsv, 'r') as csvfile:
#Split data on commas
  csvreader = csv.reader(csvfile, delimiter=',')

#include headers
  header = next(csvreader)

  totalnumvotes = [] 
  candidateslist = []
  
  count1 = 0

  for row in csvreader:
    #create the list of voters ID use to count the num of voters by ID
    totalnumvotes.append(row)
    tnv=len(totalnumvotes)
    #creat row with candidates
     
    candidateslist.append(row[2])
    khan = candidateslist.count('Khan')
    correy = candidateslist.count('Correy')

  
    #for can in candidateslist:
    #election(candidateslist)
            
print("Election Results")
print("------------------------- ")
print(f"Total Votes: " + str(tnv))
print("-------------------------")
print("Khan: " + str(int(khan)/int(tnv)*100))
#print(candidateslist.count('Correy'))
print(candidateslist.count('Li'))
print(candidateslist.count("O'Tooley"))
print(set(candidateslist))
#print(set(candidateslist('Khan')))




    
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.



 # Print("Election Results")
 # Print("------------------------- ")
 # Print(f"Total Votes: " {})
 # Print("-------------------------")
 # Print(f"Khan: " {})              # 63.000% (2218231)
 # Print(f"Correy: " {})            #20.000% (704200)
 # Print(f"Li: " {})                #14.000% (492940)
 # Print(f"O'Tooley: " {})          #3.000% (105630)
 # Print("-------------------------")
 # Print(f"Winner: " {})           #Khan
 # Print("-------------------------")
 
