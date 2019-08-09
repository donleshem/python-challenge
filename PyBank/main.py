import os
import csv


revenue_change = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]
total_Profit = 0
print ("Financial Analysis")
print ("--------------------------")

# Set path for file
csvpath = os.path.join("../..", "COLNYC20190716DATA", "02-Homeworks", "03-Python", "Instructions",
 "PyBank", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath,newline = None) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skips the headr line 
    csv_header = next(csvreader)
    rows = [rows for rows in csvreader]

    # counting and prining the number of rows
    total_months = len(rows) 

    print("Total Months: " + str(total_months))

     # The net total amount of "Profit/Losses" over the entire period
    for row in rows:
        
        total_Profit = total_Profit + int(row[1])

        
        # getting the change in profit/loss 
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row[0]]

        # The greatest increase in profits (date and amount) over the entire period 
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change

        # The greatest decrease in profits (date and amount) over the entire period 
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change



 # The average of the changes in "Profit/Losses" over the entire period
    print("Average Change: " + "$" + str(sum(revenue_change_list)/ len(revenue_change_list)))

# print the Greatest Increase in Profits
    print ("Greatest Increase in Profits: " + " (" + "$" + str(greatest_increase)+ ")")

 # print the Greatest Decrease in Profits
    print ("Greatest Decrease in Profits: " + " (" + "$" + str(greatest_decrease)+ ")")


    # exportnig the file 
  #  dframe.to_csv(“budget_data.csv”)



 
