

import os
import csv

def pybank_analysis(input_file, output_file):
    

    changes = []
    total_months = 0
    total_profit_loss = 0
    former_profit_loss = None
    maximum_increase = [None, float('-inf')]
    maximum_decrease = [None, float('inf')]

    csv_path = os.path.join('PyBank','Resources','budget_data.csv')
    print(csv_path)

    
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        next(csv_reader)  
        
        
        for line in csv_reader:
            
            
            date = line[0]
            profit_loss = line[1]
            profit_loss = int(profit_loss)

            
            total_months += 1

            
            total_profit_loss += profit_loss

            
            if former_profit_loss is not None:
                change = profit_loss - former_profit_loss
                changes.append(change)

                
                if change > maximum_increase[1]:
                    maximum_increase = [date, change]

                
                if change < maximum_decrease[1]:
                    maximum_decrease = [date, change]

            
            former_profit_loss = profit_loss

    
    average_change = sum(changes) / len(changes)

    
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {maximum_increase[0]} (${maximum_increase[1]})")
    print(f"Greatest Decrease in Profits: {maximum_decrease[0]} (${maximum_decrease[1]})")

    output_file = os.path.join(r'analysis','financial_analysis.txt')
    
    with open(output_file, "w") as file:
        file.write("Financial Analysis\n")
        file.write("------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${total_profit_loss}\n")
        file.write(f"Average Change: ${average_change:.2f}\n")
        file.write(f"Greatest Increase in Profits: {maximum_increase[0]} (${maximum_increase[1]})\n")
        file.write(f"Greatest Decrease in Profits: {maximum_decrease[0]} (${maximum_decrease[1]})\n")



input_file = os.path.join('PyBank','Resources','budget_data.csv')
output_file = os.path.join('PyBank','analysis','financial_analysis.txt')
pybank_analysis(input_file, output_file)
