import sys

from crossword import *


class CrosswordCreator:
    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy() for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont

        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size, self.crossword.height * cell_size),
            "black",
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border, i * cell_size + cell_border),
                    (
                        (j + 1) * cell_size - cell_border,
                        (i + 1) * cell_size - cell_border,
                    ),
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (
                                rect[0][0] + ((interior_size - w) / 2),
                                rect[0][1] + ((interior_size - h) / 2) - 10,
                            ),
                            letters[i][j],
                            fill="black",
                            font=font,
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable, words in self.domains.items():
            # Loop over a copy of words since the set will be modified
            for word in words.copy():
                # Remove words that can't fit in the sequar sequence
                if len(word) != variable.length:
                    self.domains[variable].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # Intiate a variable to indicate whether a revision was made
        revised = False
        # Get the index of overlap
        lapx, lapy = self.crossword.overlaps[x, y]

        # For every word in x's domain
        for wordx in self.domains[x].copy():
            # Remove the word if its indexed letter cannot match any indexed letter in y
            if wordx[lapx] not in [wordy[lapy] for wordy in self.domains[y]]:
                revised = True
                self.domains[x].remove(wordx)

        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs:
            queue = set(arcs)
        else:
            # Queue will equal to a tuple of Variable instances that have an overlap
            queue = {
                varz for varz, overlap in self.crossword.overlaps.items() if overlap
            }

        while queue:
            x, y = queue.pop()

            if self.revise(x, y):
                # If we have removed all of x's words then there's no solution
                if len(self.domains[x]) == 0:
                    return False
                # Since x was revised we add all of the neighbors for revision
                for z in self.crossword.neighbors(x) - {y}:
                    queue.add((z, x))

        # To indicate that a solution exists
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(self.domains) == len(assignment):
            return True
        return False

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Check if each Variable holds a unique word
        if len(assignment) != len(set(assignment.values())):
            return False

        # Check that each overlapping variables share  the same overlapping character
        for varz, overlap in self.crossword.overlaps.items():
            if overlap:
                x, y = varz
                if x in assignment.keys() and y in assignment.keys():
                    # Check that the word's length matchs the sequar sequence
                    if len(assignment[x]) != x.length or len(assignment[y]) != y.length:
                        return False

                    lapx, lapy = overlap
                    if assignment[x][lapx] != assignment[y][lapy]:
                        return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        counts = {value: 0 for value in self.domains[var]}
        # Least Constraining Values heuristic
        for word in self.domains[var]:
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment.keys():
                    continue

                lapv, lapn = self.crossword.overlaps[var, neighbor]
                for wordn in self.domains[neighbor]:
                    # If the word will cause a neighboring variable to be rolled out, iterate by 1
                    if word[lapv] != wordn[lapn]:
                        counts[word] += 1

        return sorted(self.domains[var], key=lambda word: counts[word])

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Minimum Remaining Values (MRV)
        # Order all of unassigned variables by the length of their domain
        unassigned = sorted(
            self.domains.keys() - assignment.keys(),
            key=lambda var: len(self.domains[var]),
        )

        # Check for ties
        same = []
        for var in unassigned:
            if len(self.domains[var]) == len(self.domains[unassigned[0]]):
                same.append(var)
            # Since the list is ordered once we find one that's not a tie we can break
            else:
                break

        # Degree heuristic
        # In case of a tied pick the one with the greatest neighbors
        highest_degree = unassigned[0]
        for var in same:
            if len(self.crossword.neighbors(var)) > len(
                self.crossword.neighbors(highest_degree)
            ):
                highest_degree = var

        return highest_degree

    def inference(self, assignment):
        arcs = set()
        for varz, overlap in self.crossword.overlaps.items():
            if overlap:
                x, y = varz
                if x not in assignment:
                    arcs.add((x, y))

        self.ac3(arcs)

        for var, domain in self.domains.items():
            if var not in assignment.keys():
                if len(domain) == 1:
                    assignment[var] = domain[0]

        return assignment

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # Base case
        if self.assignment_complete(assignment):
            return assignment

        # Recursive case
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            copy_assignment = assignment.copy()
            copy_assignment[var] = value
            # If adding value will not cause inconsistency
            if self.consistent(copy_assignment):
                # Slower
                # copy_assignment = self.inference(copy_assignment)

                result = self.backtrack(copy_assignment)
                if result:
                    return result


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
