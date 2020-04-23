from cs50 import get_string


def main():
    text = get_string("Text: ")

    letter = 0
    sentence = 0
    word = 1  # this accounts for the fact that the last word doesn't have a space after it
    for i in text:
        if i.isalpha():
            letter += 1

        elif i == "." or i == "!" or i == "?":
            sentence += 1

        elif i.isspace():
            word += 1

    calc(letter, sentence, word)


def calc(l, s, w):
    # getting letters and sentences' average per 100 words
    l = l / w * 100
    s = s / w * 100

    # the formula rounded to the nearest whole number
    cli = round(0.0588 * l - 0.296 * s - 15.8)

    if cli > 16:
        print("Grade 16+")

    elif cli < 1:
        print("Before Grade 1")

    else:
        print(f"Grade {cli}")


# start
main()