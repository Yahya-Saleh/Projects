# Credit
 Using some fundementle knoweldge about how credit (or debit) cards like the number's length and structure along with Luhn’s Algorithm, one can devise a program to validate a card's number
 
 Length: 
 * American Express uses 15-digit numbers
 * MasterCard uses 16-digit numbers
 * Visa uses 13- and 16-digit numbers

 structure:
 * All American Express numbers start with 34 or 37
 * Most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which I won’t concern myself with for this problem)
 * All Visa numbers start with 4

## Luhn’s Algorithm
 So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

 1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
 1. Add the sum to the sum of the digits that weren’t multiplied by 2.
 1. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
 
## Usage
 Prompts the user for a credit card number and then reports whether it is a valid American Express, MasterCard, Visa card number, or an invalid card.
```
$ python credit.py
Number: 378282246310005
AMEX
```