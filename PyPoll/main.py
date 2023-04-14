import os
import csv


def elections_results(input_file, output_file):
    
    
    candidates = {}

    total_number_of_votes = 0
    

    csv_path = os.path.join('PyPoll','Resources', 'election_data.csv') 
    print(csv_path)

    with open (csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) 
         
        
        for row in csv_reader:
            
            candidate = row[2]
            
            total_number_of_votes += 1

            
            if candidate not in candidates:
                candidates[candidate] = 1
            else:
                candidates[candidate] += 1

    
    winner = max(candidates, key=candidates.get)

    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_number_of_votes}")
    print("-------------------------")

    
    with open(output_file, "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_number_of_votes}\n")
        file.write("-------------------------\n")

        
        for candidate, votes in candidates.items():
            percentage_of_votes = (votes / total_number_of_votes) * 100
            print(f"{candidate}: {percentage_of_votes:.3f}% ({votes})")
            file.write(f"{candidate}: {percentage_of_votes:.3f}% ({votes})\n")

        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")


input_file = os.path.join('PyPoll','Resources', 'election_data.csv')
output_file = os.path.join('PyPoll','Analysis','Election_Results.txt')
elections_results(input_file, output_file)

