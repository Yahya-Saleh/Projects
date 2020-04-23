from cs50 import get_string
from sys import exit


def main():
    card_num = get_string("Number: ")
    n = len(card_num)

    if n == 15:
        if valid(card_num):
            if card_num[0] == "3":
                if card_num[1] == "7" or card_num[1] == "4":
                    print("AMEX\n")
                    exit(0)

    elif n == 16:
        if valid(card_num):
            if card_num[0] == "5":
                print("MASTERCARD\n")
                exit(0)
            elif card_num[0] == "4":
                print("VISA\n")
                exit(0)

    elif n == 13:
        if valid(card_num):
            if card_num[0] == "4":
                print("VISA\n")
                exit(0)

    print("INVALID\n")
    exit(1)


def valid(num):
    total = 0
    second_to_last = False

    for i in reversed(range(len(num))):
        n = int(num[i])

        if second_to_last:
            n *= 2
            for j in str(n):
                total += int(j)
            second_to_last = False

        else:
            total += n
            second_to_last = True

    if total % 10 == 0:
        return True
    else:
        return False


# start of the program
main()
