import itertools
import random
from copy import deepcopy


class Minesweeper:
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence:
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return self.cells

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if count == 0:
            return self.cells

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI:
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def update_knowledge(self):
        """
        Loops through a deepcopy of the knowledge-base 
        and checks for new conclusions to be inferred 
        and updates the knowledge-base accordingly
        """
        # Loop over a deepcopy so we can alter the original list
        for sentence in deepcopy(self.knowledge):
            # If no mine exists
            if sentence.count == 0:
                # Add all cells to safes
                for cell in sentence.cells:
                    self.mark_safe(cell)

            # If all cells are mines
            elif sentence.count == len(sentence.cells):
                # Add all cells to mines
                for cell in sentence.cells:
                    self.mark_mine(cell)

        # Remove any empty sentences
        for sentence in self.knowledge:
            # If cells is empty
            if not sentence.cells:
                self.knowledge.remove(sentence)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Mark move as safe and made
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # Adding Sentence to the knowledge-base
        cells = set()
        # Loop over neighboring cells
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # If cell is within bound add it
                if 0 <= j < self.height and 0 <= i < self.width:
                    # If the cell is safe we won't include it since we know it's not a mine
                    if (i, j) in self.safes:
                        continue

                    # If we know the cell to be a mine then we remove it and remove one mine from count simplifying the expression
                    elif (i, j) in self.mines:
                        count -= 1
                        continue

                    # Add cell if it is not in safes or mines
                    cells.add((i, j))

        self.knowledge.append(Sentence(cells, count))

        # After adding the sentence update the knowledge-base
        self.update_knowledge()

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Identify all of the possible safe moves
        pos_safe_moves = list(self.safes.difference(self.moves_made))

        # If there's a possible safe moves return one of them, else return none
        if pos_safe_moves:
            return random.choice(pos_safe_moves)

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        no_move = self.moves_made.union(self.mines)
        if len(no_move) == (self.height * self.width):
            return None

        while True:
            move = random.randrange(self.height), random.randrange(self.width)

            if move not in no_move:
                return move


# game = Minesweeper()
# ai = MinesweeperAI()

# game.print()

# cell1 = (1, 3)
# cell2 = (2, 3)
# cell3 = (3, 3)

# ai.add_knowledge(cell1, game.nearby_mines(cell1))
# ai.add_knowledge(cell2, game.nearby_mines(cell2))
# ai.add_knowledge(cell3, game.nearby_mines(cell3))

# for sentence in ai.knowledge:
#     print(str(sentence))

# print(f"Mine: {ai.mines}")
# print(f"safe: {ai.safes}")

# print(ai.make_random_move())
