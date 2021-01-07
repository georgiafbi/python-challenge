import os
import csv

csvpath = os.path.join('..','Resources', 'budget_data.csv')
#initalizes two variables to store calculations done on bank records
p_value = []
number_months=0
total_profit = 0
changes = []
average_change=0
date =[]
change_index=0
greatest_increase_in_profits=[]
greatest_Decrease_in_profits=[]
#opens budget_data.csv
with open(csvpath) as csvfile:
    #reads the csv file and separates the data by a ','
    csvreader = csv.reader(csvfile, delimiter=',')
    #extract the first row of the csv
    csv_header = next(csvreader)
    #print(csv_header)
    for row in csvreader:
        p_value.append(int(row[1]))
        date.append(row[0])
        #number_months+=1
        #total_profit += int(row[1]) """
        #changes.append(int(row[1])-) 
    number_months = len(p_value)
    total_profit = sum(p_value)
    print(f"Total Months: {number_months}")
    print(f"Total: ${total_profit}")
    #print(p_value)
    for i in range(0,len(p_value)):
        if i == len(p_value)-1:
            break
        changes.append(p_value[i+1]-p_value[i])
    average_change = round(sum(changes)/len(changes),2)
    print(f"Average change: {average_change}")
    cmax_index= changes.index(max(changes))
    cmin_index=changes.index(min(changes))
    #print(max(changes))
    greatest_increase_in_profits.extend((date[cmax_index+1], max(changes)))
    print(f"Greatest Increase in Profits: {greatest_increase_in_profits[0]}, ${greatest_increase_in_profits[1]}")
    greatest_Decrease_in_profits.extend((date[cmin_index+1], min(changes)))
    print(f"Greatest Decrease in Profits: {greatest_Decrease_in_profits[0]}, ${greatest_Decrease_in_profits[1]}")