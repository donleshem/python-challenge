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


# The net total amount of "Profit/Losses" over the entire perio
    print("Total: "+ str(total_Profit))

 # The average of the changes in "Profit/Losses" over the entire period
    print("Average Change: " + "$" + str(round(sum(revenue_change_list[1:])/ len(revenue_change_list),3)))


# print the Greatest Increase in Profits
    print ("Greatest Increase in Profits: " + str(greatest_increase[0])+ " ($" + str(greatest_increase[1])+ ")")

 # print the Greatest Decrease in Profits
    print ("Greatest Decrease in Profits: " + str(greatest_decrease[0])+ " ($"+ str(greatest_decrease[1])+  ")")


    # exportnig the file 
    with open("Output_for_PyBank.txt", "w") as text_file:
        text_file.write ("Financial Analysis")
        text_file.write("\n")
        text_file.write ("--------------------------")
        text_file.write("\n")
        text_file.write ("Total Months: " + str(total_months))
        text_file.write("\n")
        text_file.write ("Total: "+ str(total_Profit))
        text_file.write("\n")
        text_file.write("Average Change: " + "$" + str(round(sum(revenue_change_list[1:])/ len(revenue_change_list),3)))
        text_file.write("\n")
        text_file.write ("Greatest Increase in Profits: " + str(greatest_increase[0])+ " ($" + str(greatest_increase[1])+ ")")
        text_file.write("\n")
        text_file.write ("Greatest Decrease in Profits: " + str(greatest_decrease[0])+ " ($"+ str(greatest_decrease[1])+  ")")
        text_file.close()

