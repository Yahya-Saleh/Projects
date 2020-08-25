# Used for testing
def grid(board):
    grid = "\n"
    for i, row in enumerate(board):

        for j, cell in enumerate(row):
            grid += f"\t{cell}\t"

            if j != 2:
                grid += "|"

        if i != 2:
            grid += f"\n{'-'*16}+{'-'*15}+{'-'*16}\n"

    grid += "\n"

    print(grid)
