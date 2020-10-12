from sys import argv, exit
import csv


def main():
    # check for correct input
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # open the give file and store its sequence in seq
    with open(argv[2]) as file:
        seq = file.read()

    # open the csv file and get from it (1)the database and store it in a dictionary, and (2) the list of STRs recorded
    with open(argv[1]) as csv_file:
        readcsv = csv.DictReader(csv_file)

        data = []
        for row in readcsv:
            data.append(row)

        STRs = []
        # could be any index of data since the keys are the same for each dictionary
        for key in data[0]:
            STRs.append(key)
        STRs.remove("name")

    # for every STR in our STRs list we check for how many times it repeats in the sequence
    for STR in STRs:
        rep = repetition(STR, seq)

        # any dictionary that doesn't have the same number of the repetition for the specific STR is added to  the out list
        out = []
        for dic in data:
            if dic[STR] != str(rep):
                out.append(dic)
        # and then removed to make the next checking much faster
        for rm in out:
            data.remove(rm)

    # after checking for each STR we will either have one or none remaining
    if len(data) == 1:
        print(data[0]["name"])
        exit(0)
    elif len(data) == 0:
        print("No match")
        exit(0)


def repetition(STR, seq):
    start = repeated = highest = 0
    end = len(STR)
    # as long as our end index is inside the sequence
    while end < len(seq):
        # if this portion of sequence is equal to STR the we look at the portion next to it
        if seq[start:end] == STR:
            repeated += 1
            start += len(STR)
            end += len(STR)

        # otherwise we store the highest number of repetition, move one step and check again
        else:
            if repeated > highest:
                highest = repeated
            repeated = 0
            start += 1
            end += 1

    # once the loop is done we retun the highest number of repetition
    return highest


# start
if __name__ == "__main__":
    main()