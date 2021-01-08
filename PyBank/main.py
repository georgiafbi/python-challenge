import os
import csv

bdgt_pth = os.path.join('Resources', 'budget_data.csv')
print(f"Your directory: {os.getcwd()}")
bdgt_txt = os.path.join('Analysis','financial_analysis.csv')
#initalizes two variables to store calculations done on bank records
prft_value = []
t_months=0
t_profit = 0
changes = []
avrge_change=0
dates =[]
change_index=0
greatest_increase_in_profits=[]
greatest_Decrease_in_profits=[]

#returns the greatest increase in profits and prints it to terminal
def grt_incrse():
    cmax_index= changes.index(max(changes))
    greatest_increase_in_profits.extend((dates[cmax_index+1], max(changes)))
    incrse=f"Greatest Increase in Profits: {greatest_increase_in_profits[0]}, (${greatest_increase_in_profits[1]})"
    print(incrse)
    return(incrse)
#returns the greatest decrease in losses and prints it to the terminal 
def grt_dcrse():
    cmin_index= changes.index(min(changes))
    greatest_Decrease_in_profits.extend((dates[cmin_index+1], min(changes)))
    dcrse=f"Greatest Decrease in Profits: {greatest_Decrease_in_profits[0]}, (${greatest_Decrease_in_profits[1]})"
    print(dcrse)
    return dcrse
#returns the numbers of months included in the data set and prints it to terminal
def total_months():
    t_months = len(prft_value)
    output=f"Total Months: {t_months}"
    print(output)
    return output

#returns the total amount of profit and losses from data set and prints it to terminal
def total_amount():
    t_profit = sum(prft_value)
    output= f"Total: ${t_profit}"
    print(output)
    return(output)

#returns the average change in profits and prints it to the terminal
def average_change():
    avrge_change = round(sum(changes)/len(changes),2)
    output=f"Average change: ${avrge_change}"
    print(output)
    return output

#writes a financial analysis data to a text file and in the terminal
def write_txt_file():
    with open(bdgt_txt,"w+") as txt:
        txt.write("'''text\nFinancial Analysis\n----------------------------\n")
        txt.write(total_months()+"\n")
        txt.write(total_amount()+"\n")
        txt.write(average_change()+"\n")
        txt.write(grt_incrse()+"\n")
        txt.write(grt_dcrse()+"\n")
        txt.write("'''")
#opens budget_data.csv
with open(bdgt_pth) as bdgt_file:
    #reads the csv file and separates the data by a ','
    r_bdgt_file = csv.reader(bdgt_file, delimiter=',')
    #extract the first row of the csv
    bdgt_header = next(r_bdgt_file)
    #print(csv_header)
    for row in r_bdgt_file:
        #stores the profit/losses values and date as an int and string, respectively
        #into lists prft_value and date
        prft_value.append(int(row[1]))
        dates.append(row[0])
    #calculates the changes in profit and losses
    for i in range(0,len(prft_value)):
        if i == len(prft_value)-1:
            break
        changes.append(prft_value[i+1]-prft_value[i])
write_txt_file()





    



    
    


    
    