# longest substring in alphabetical order

A program that prints the longest substring in which the letters occur in alphabetical order.

## Usage

```bash
$python longest_substring.py
Enter a sentence: abzcboboababegghakl
Longest substring in alphabetical order is: abeggh
```

## Code

The program initiates `i = 0` and then loops until `i` is less than `len(s) - 1`, where `s` is the given string. The condition is `i < len(s) - 1`, because the system checks `s[i + 1]`. In a nested while loop the system checks if the preceding letter is after the $i^{th}$ letter order wise using the built in `ord` function.

If so we add the letter to a `string` variable that is initialized with the $i^{th}$ letter, then `i` is incremented and we check again. This goes on until we reach the end of the string or find a letter that does not follow the pattern. In which case, the system evaluates if `string` is greater than the longest substring found so far and updates teh variable `longest_string` accordingly. Lastly, `i` is incremented and the process repeats.
