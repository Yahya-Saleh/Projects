def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    # Check if we exhausted the list
    if not aStr:
        return False
    elif len(aStr) == 1:
        return char == aStr

    # Get the middle index
    middle_index = int(len(aStr) / 2)
    middle_char = aStr[middle_index]

    # Evaluate the guess
    if char == middle_char:
        return True
    elif char > middle_char:
        return isIn(char, aStr[middle_index:])
    elif char < middle_char:
        return isIn(char, aStr[:middle_index])