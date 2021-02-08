s = input("Enter a sentence: ")

longest_string = ""
i = 0
# While i is less than len(s) by 1 (because we access s[i+1])
while i < len(s) - 1:
    # Start a string with the ith letter
    string = s[i]
    # If we're within range and the preciding letter's value is greater than or equal to the letter
    # That is it's order is after the letter (z is after a in order)
    while i < len(s) - 1 and ord(s[i + 1]) >= ord(s[i]):
        # Add it to the string
        string += s[i + 1]
        # Increment and check again
        i += 1

    # Check if the string is longer than the longest string
    if len(string) > len(longest_string):
        longest_string = string

    # Go to the next letter
    i += 1

print(f"Longest substring in alphabetical order is: {longest_string}")