# Plurality

A program designed to handle plurality voting.

## Usage

```bash
$ ./plurality Alice Bob
Number of voters: 3
Vote: Alice
Vote: Charlie
Invalid vote.
Vote: Alice
Alice
```

This takes in the names of candidates as part of the command-line argument. It then prompts the user for the number of voters and let's the user input them sequently. Lastly the program outputs the winner(s) of the election.

```bash
$ ./plurality Alice Bob Charlie
Number of voters: 5
Vote: Alice
Vote: Charlie
Vote: Bob
Vote: Bob
Vote: Alice
Alice
Bob
```

## Breaking down the code

The #define MAX 9 means that MAX is an unchangeable constant that’s equal to 9, any MAX written in code will be replaced with a 9.

> MAX represents the maximum number of candidates

The file then defines a struct called a `candidate`. Each candidate has two fields:

- a string called name representing the candidate’s name
- an int called votes representing the number of votes the candidate has.
  
Next, the file defines a global array of candidates, where each element is itself a candidate. Now, take a look at the main function itself. See if you can find where the program sets a global variable `candidate_count` representing the number of candidates in the election, copies command-line arguments into the array candidates, and asks the user to type in the number of voters.

Then, the program lets every voter type in a vote, calling the vote function on each candidate voted for. Finally, main makes a call to the print_winner function to print out the winner (or winners) of the election.
