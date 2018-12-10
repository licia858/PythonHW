import os
import csv

pybankCSV = os.path.join('..','..','02-Homework','03-Python','Instructions','PyBank','Resources','budget_data.csv')


print("Financial Analysis")
print("  ---------------------------- ")
 
#read CSV File
with open(pybankCSV, 'r') as csvfile:
#Split data on commas
  csvreader = csv.reader(csvfile, delimiter=',')

#include headers
  header = next(csvreader)
  
  #define to read data as a whole column
  totalmonths = []
  totalpnl = []
  averagechange = []
  months = []
  #read each row
  for row in csvreader:
    #reads 1st column 
     totalmonths.append(row)

#reads 2nd column int because its numbers
     totalpnl.append(int(row[1]))
#The total number of months included in the datase
print(f"Total Months: " + str(len(totalmonths)))
#The total net amount of "Profit/Losses" over the entire period
print(f"Total: " + str(sum(totalpnl)))

  #loop to find change
for i in range(len(totalpnl) - 1):
    #pulls the list of change
    averagechange.append(totalpnl[i+1] - totalpnl[i])
    #find index of max 


  
#print(totalmonths(averagechange.index(max(averagechange))))

        #  to find the Average and print between months over the entire period
print(f"Average Change: " + str(int(sum(averagechange)/ len(averagechange))))
#The greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Profits: " + str(max(averagechange)))
#The greatest decrease in losses (date and amount) over the entire period  
print(f"Greatest Increase in Profits: " + str(min(averagechange)))

    
  
  
  
  #print(f"Greatest Increase in Profits:  + {str(greatest_increase)}")
 # print(f"Greatest Decrease in Profits:  + {str(greatest_decrease)}")

    
      
