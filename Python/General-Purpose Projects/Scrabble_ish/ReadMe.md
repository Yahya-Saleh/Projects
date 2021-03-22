# Scrabble_ish

This game is a lot like Scrabble or Words With Friends. Letters are dealt to players, who then construct one or more words out of their letters. Each **valid** word receives a score, based on the length of the word and the letters in that word.

## Usage

Run the program in the same directory as teh [`word.txt`](words.txt) file or alter the `WORDLIST_FILENAME` accordingly.

```bash
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points
Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points
Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points
Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points
Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```

## Table of content

- [Scrabble_ish](#scrabble_ish)
  - [Usage](#usage)
  - [Table of content](#table-of-content)
  - [Background](#background)
    - [Dealing](#dealing)
    - [Scoring](#scoring)
  - [Dealing with hands](#dealing-with-hands)
    - [Representing hands](#representing-hands)
    - [Converting words into dictionary representation](#converting-words-into-dictionary-representation)
    - [Displaying a hand](#displaying-a-hand)
    - [Generating a random hand](#generating-a-random-hand)
    - [Removing letters from a hand](#removing-letters-from-a-hand)
  - [Acknowledgements](#acknowledgements)

## Background

This game is a lot like Scrabble or Words With Friends. Letters are dealt to players, who then construct one or more words out of their letters. Each **valid** word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:

### Dealing

- A player is dealt a hand of `n` letters chosen at random.

- The player arranges the hand into as many words as they want out of the letters, using each letter at most once.

- Some letters may remain unused (these won't be scored).

### Scoring

- The score for the hand is the sum of the scores for each word formed.

- The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

- Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

- For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

- As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).

---

## Dealing with hands

### Representing hands

A hand is the set of letters held by a player during the game. The player is initially dealt a set of random letters. For example, the player could start out with the following hand: `a, q, l, m, u, i, l`. In our program, a hand will be represented as a dictionary: the keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand. For example, the above hand would be represented as:

```python
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
```

Notice how the repeated letter `'l'` is represented.

### Converting words into dictionary representation

When `getFrequencyDict` is given a string of letters as an input, it returns a dictionary where the keys are letters and the values are the number of times that letter is represented in the input string. For example:

``` python
>>> getFrequencyDict("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

As you can see, this is the same kind of dictionary we use to represent hands.

### Displaying a hand

the `displayHand` function displays the letters currently in the hand.For example:

```python
>>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
a x x l l l e
```

### Generating a random hand

The hand a player is dealt is a set of letters chosen at random. The `dealHand` function takes as input a positive integer `n`, and returns a new object, a hand containing `n` lowercase letters.\

### Removing letters from a hand

The player starts with a hand, a set of letters. As the player spells out words, letters from this set are used up. For example, the player could start out with the following hand: `a, q, l, m, u, i, l`. The player could choose to spell the word `quail`. This would leave the following letters in the player's hand: `l, m`. `updateHand` uses letters from the hand to spell the word, and then returns a copy of the hand, containing only the letters remaining. For example:

```python
>>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
>>> displayHand(hand) # Implemented for you
a q l l m u i
>>> hand = updateHand(hand, 'quail') # You implement this function!
>>> hand
{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
>>> displayHand(hand)
l m  
```

---

## Acknowledgements

All the tests in [`test.py`](tests.py) were pre-set with the exception of the `test_calculateHandlen` test. `loadWords`, `getFrequencyDict`, `displayHand`, `dealHand`, and `dealHand` were also pre-implemented.
