import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0
net_total = 0
profit_loss_list = []
month_list = []

with open(csvpath, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        month = row[0]
        try:
           profit_loss = int(row[1].strip())
        except ValueError:
           continue

        total_months +=1
        net_total +=profit_loss
        month_list.append(month)
        profit_loss_list.append(profit_loss)
    changes = {month_list[i]: profit_loss_list[i] - profit_loss_list[i-1] for i in range(1, len(profit_loss_list))}
    average_change = sum(changes.values())/len(changes)

with open("financial_data.txt", "w") as file:
    print("Financial Analysis")
    file.write("Financial Analysis\n")
    print("--------------------------------------------------------")
    file.write("--------------------------------------------------------\n")
    print(f"Total Months: {total_months}")
    file.write(f"Total Months: {total_months}\n")
    print(f"Total: ${net_total}")
    file.write(f"Total: ${net_total}\n")
    print(f"Average Change: ${average_change}")
    file.write(f"Average Change: ${average_change}\n")
    print(f"Greatest Increase in Profits: {max(changes, key=changes.get)} (${max(changes.values())})")
    file.write(f"Greatest Increase in Profits: {max(changes, key=changes.get)} (${max(changes.values())})\n")
    print(f"Greatest Decrease in Profits: {min(changes, key=changes.get)} (${min(changes.values())})")
    file.write(f"Greatest Decrease in Profits: {min(changes, key=changes.get)} (${min(changes.values())})\n")