# Add dependencies we need

import csv
import os



#Assign a variable for the file to load from a path

file_to_load = os.path.join('Resources','election_results.csv')

#Assign a variable to save the output file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize the vote counter to zero

total_votes = 0

#Initialize the list of candidate names

candidate_options = [] 

#Initialize a dictionary to hold the candidate names (key) and number of votes (value)

candidate_votes = {}

#Initialize variables to store the winning name, count, and percentage of votes

winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file


with open(file_to_load) as election_data:

   
    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader=csv.reader(election_data)

    #Read the header row, advances file to row 2 so header row is not included in our analysis
    headers = next(file_reader)
    
    #Start looping through all the rows of data
    for row in file_reader:
         
         #Increment the total vote counter
         total_votes +=1
         
         #Get the candidate name from each row
         candidate_name = row[2]
         
         #If this candidate name is appearing for the first time
         if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0

         #Add a vote to each candidate's count
         candidate_votes[candidate_name]+=1

    #Loop stops when the indentation stops



#Save the results to our text file
with open(file_to_save,"w") as txt_file:
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")

    #Save the final vote count to the text file
    txt_file.write(election_results)
    
    

    #Determine the percentage of votes for each candidate by looping through the counts
    #Loop through the candidate list
    for candidate_name in candidate_votes:

        #retrieve the number of votes
        votes = candidate_votes[candidate_name]

        #calculate the percentage of votes received
        vote_percentage = (float(votes)/float(total_votes))*100

        #print out each candidate's name and percentage of votes to the terminal
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        #save the candidate results to our output text file
        txt_file.write(candidate_results)

        #Use an if statement to calculate the winner
        if(votes > winning_count) and (vote_percentage>winning_percentage):
            #if true then set winning_count to votes and winning_percentage to vote_percentage
            winning_count=votes
            winning_percentage = vote_percentage
            #Set the winning candidate equal to the candidate's name
            winning_candidate=candidate_name

    #Create output f string to print results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    

    #Print report about who won to the terminal and the output text file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


    #Print out what we've found so far
    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)


    # Using the with statement, open the output file as a text file

    #with open(file_to_save,"w") as txt_file:

        #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson ")
    

    #2)Get the data we need from the .csv file
    #3)Store the names of all the candidates
    #4)Create a variable for the vote count for each candidate
    #5)Count the number of votes for each candidate
    #6)Count the total number of votes




    #Close the file
    election_data.close()

