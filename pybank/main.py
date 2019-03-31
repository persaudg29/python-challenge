"""
main.py is a program which parses statistical data from budget_data.csv
"""
import csv 
budgetfile = open("budget_data.csv", "r") 

budgetheader, *budgetdata = budgetfile.readlines() 
dict_month = {"Jan": 0, 
    "Feb": 0,
    "Mar": 0, 
    "Apr": 0, 
    "May": 0, 
    "Jun": 0, 
    "Jul": 0, 
    "Aug": 0, 
    "Sep": 0, 
    "Oct": 0,
    "Nov": 0,
    "Dec": 0} #empty dictionary for months, months initially set to 0

total_months = 0
total_profit = 0.00 #need to save as 0.00 so that the variable is a float()
average_change = 0
monthly_change = []
prev = 867884
maxchange = 0.0
minchange = 0.0

def parsemonth(date): 
    return date.split('-')[0]
    #print(month)

#first = True
for line in budgetdata: 
    parts = line.split(',')
    date = parts[0] #isolates the month
    profit = float(parts[1]) #isolates the profit string - float() converts string to number
    month = parsemonth(date) #function which parses out the month
    dict_month[month] = dict_month[month]+1 
    #Line below does the actual counting of lines in the portion of csv defined as budgetdata 
    #can use total_months += 1 (equivalent to total_months = total_months + 1 )
    total_months = total_months + 1 
    total_profit += profit 
    difference = profit - prev
    monthly_change += [difference]

    minchange = min(minchange, difference)
    maxchange = max(maxchange, difference)
    prev = profit

#average_change = average_change/total_months
#average_change = (int(Last) - int(First)) /total_months
print("Total Months: " + str(total_months))
print("Total Profits: " + str(total_profit)) 
print("Average Change:" + str(sum(monthly_change)/len(monthly_change)))
print("Maximum Change: " + str(maxchange))
print("Minimum Change: " + str(minchange))