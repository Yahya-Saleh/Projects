# Knights and Knaves

![Knights and Knaves](../../../Snippets/Python/AI/knightsandknave/Knights%20and%20Knaves.png)

A program that represents and solves four knights and knaves puzzles, [Watch it in action](https://youtu.be/W2CIwfBTtzc):

1. puzzle 0:
   - A says “I am both a knight and a knave.”
2. puzzle 1:
   - A says “We are both knaves.”
   - B says nothing.
3. puzzle 2:
   - A says “We are the same kind.”
   - B says “We are of different kinds.”
4. puzzle 3:
   - A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
   - B says “A said ‘I am a knave.’”
   - B then says “C is a knave.”
   - C says “A is a knight.”

## Table of contents

- [Knights and Knaves](#knights-and-knaves)
  - [Table of contents](#table-of-contents)
  - [Background](#background)
  - [Logic.py](#logicpy)
    - [Logical Connectives](#logical-connectives)
    - [Model checking](#model-checking)
  - [Puzzle.py](#puzzlepy)
    - [Game logic](#game-logic)
    - [Statement logic](#statement-logic)
  - [Acknowledgements](#acknowledgements)

---

## Background

In 1978, logician Raymond Smullyan published “What is the name of this book?”, a book of logical puzzles. Among the puzzles in the book were a class of puzzles that Smullyan called “Knights and Knaves” puzzles.

In a Knights and Knaves puzzle, the following information is given:

- Each character is either a knight or a knave.
- A knight will always tell the truth: if knight states a sentence, then that sentence is true.
- A knave will always lie: if a knave states a sentence, then that sentence is false.

The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave!

![Knights and Knaves example](../../../Snippets/Python/AI/knightsandknave/Knights%20and%20Knaves%20example.png)

---

## [Logic.py](logic.py)

### Logical Connectives

This file defines the classes for of the propositional logical connectives. These classes can be composed within each other, so an expression like And(Not(A), Or(B, C)) represents the logical sentence stating that symbol A is not true, and that symbol B or symbol C is true (where “or” here refers to inclusive, not exclusive, or).

### Model checking

The file also defines a model_check function that takes in a knowledge-base and a query and returns true if the knowledge-base entails the query through model_checking. If A entails B, for example, then B will be true whenever A is.

## [Puzzle.py](puzzle.py)

This file represents the knowledge-base for each of the 4 given puzzles and solves them with model checking.

### Game logic

```python
A_logic = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))
B_logic = And(Or(BKnight, BKnave), Not(And(BKnight, BKnave)))
C_logic = And(Or(CKnight, CKnave), Not(And(CKnight, CKnave)))
```

Atop the file, and under the definition of the symbols is three variables that store the game's logic for each character. Ultimately, what's presented there is the logic that each character can either be a knight or a knave, but not both, exclusive or.

### Statement logic

```python
# A says "I am both a knight and a knave."
knowledge0 = And(A_logic, Biconditional(And(AKnave, AKnight), AKnight))
```

Notice how every statement said by each character is formulated into a propositional statement inside a biconditional statement where if the statement is true, then whoever said it is a knight. Since I used a biconditional connective and included the game's logic, if the statement is false then whoever said it has to be a knave.

---

## Acknowledgements

[logic.py](logic.py) was provided by CS50AI.
