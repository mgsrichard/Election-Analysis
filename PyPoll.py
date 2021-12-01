# Add dependencies we need

import csv
import os



#Assign a variable for the file to load from a path

file_to_load = os.path.join('Resources','election_results.csv')

#Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file


with open(file_to_load) as election_data:

   
    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader=csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement, open the output file as a text file

with open(file_to_save,"w") as txt_file:

    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson ")
   

#2)Get the data we need from the .csv file
#3)Store the names of all the candidates
#4)Create a variable for the vote count for each candidate
#5)Count the number of votes for each candidate
#6)Count the total number of votes




#Close the file
election_data.close()

