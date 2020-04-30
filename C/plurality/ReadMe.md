# Plurality
This takes in the names of candidates as part of the terminal argument. It then prompts the user for the number of voters and let's the user input them sequently. Lastly the program outputs the winner(s) of the election.
```
$ ./plurality Alice Bob
Number of voters: 3
Vote: Alice
Vote: Charlie
Invalid vote.
Vote: Alice
Alice
```
```
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