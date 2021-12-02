# Election-Analysis

## A Colorado Board of Elections employee has given us the following tasks to complete for the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total numner of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Date Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.62

## Summary
The analysis of the results show that:
- There were 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana Degette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
  
 ## Challenge Overview
 
 Tom, our client from the Colorado Board of Elections, has asked us to provide some more data afor their audit.  In addition to what we have already provided, they would like us to also calculate:
 - The voter turnout for each county
 - The percentage of votes from each county out of the total count
 - The county with the highest turnout 
 
 ## Challenge Summary
 
 ### Results of Additional Analysis
 - There were 369,711 votes cast in the election
 - Votes and percentage of votes by county
    - Jefferson County: 38,855 votes, 10.5%
    - Denver County: 306,055 votes, 82.8% 
    - Arapahoe County: 24,801 votes, 6.7%
 - Denver County had the greatest number of votes of the three counties
 - Votes and percentage of votes by candidate
    - Charles Casper Stockham: 85,213 votes, 23.0%
    - Diana Degette: 272,892 votes, 73.8%
    - Raymon Anthony Doane: 11,606 votes,3.1% 
    
#### Screenshot of Terminal/Screen Ouput

#### Screenshot of Text Output File

### Election Audit Summary

Please contact us the next time you are in need of any election audit analysis! The code we developed here can be easily adapted to analyze the outcome of any election.  For local elections, the breakdowns by county could be replaced by voting precinct or county district breakdowns.  For a statewide election, the results could be analyzed based on a county by county basis or even on a regional analysis, defining the state regions in cooperation with you. For primary elections, we could present the results of both party primaries (if both happen in the same year) and show how turnout differs by party and location (whether by county or district, as long as that location data is provided.)
