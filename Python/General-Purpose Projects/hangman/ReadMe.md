# Hangman

A variation of the classic word game Hangman. For those of you who are unfamiliar with the rules, you may read all about it [here](https://en.wikipedia.org/wiki/Hangman_(game)). The second player will always be the computer, who will be picking a word at random.

## Usage

Run [hangman.py](hangman.py) with the command `python hangman.py` in the same directory as [`words.txt`](words.txt) the system will pick a word and tell you its length and you have to try and guess it as shown in the [sample output section](#sample-output).

## Table of content

- [Hangman](#hangman)
  - [Usage](#usage)
  - [Table of content](#table-of-content)
  - [Requirements](#requirements)
  - [Sample Output](#sample-output)
    - [Winning game](#winning-game)
    - [Losing game](#losing-game)

---

## Requirements

Here are the requirements for your game:

1. The computer must select a word at random from the list of available words that was provided in `words.txt`. The functions for loading the word list and selecting a random word have already been provided for you in `ps3_hangman.py`.

1. The game must be interactive; the flow of the game should go as follows:

    - At the start of the game, let the user know how many letters the computer's word contains.

    - Ask the user to supply one guess (i.e. letter) per round.

    - The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.

    - After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.

1. Some additional rules of the game:

    - A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).

    - A user loses a guess only when s/he guesses incorrectly.

    - If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.

    - The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.

---

## Sample Output

### Winning game

```bash
 Loading word list from file...
 55900 words loaded.
 Welcome to the game, Hangman!
 I am thinking of a word that is 4 letters long.
 -------------
 You have 8 guesses left.
 Available letters: abcdefghijklmnopqrstuvwxyz
 Please guess a letter: a
 Good guess: _ a_ _
 ------------
 You have 8 guesses left.
 Available letters: bcdefghijklmnopqrstuvwxyz
 Please guess a letter: a
 Oops! You've already guessed that letter: _ a_ _
 ------------
 You have 8 guesses left.
 Available letters: bcdefghijklmnopqrstuvwxyz
 Please guess a letter: s
 Oops! That letter is not in my word: _ a_ _
 ------------
 You have 7 guesses left.
 Available letters: bcdefghijklmnopqrtuvwxyz
 Please guess a letter: t
 Good guess: ta_ t
 ------------
 You have 7 guesses left.
 Available letters: bcdefghijklmnopqruvwxyz
 Please guess a letter: r
 Oops! That letter is not in my word: ta_ t
 ------------
 You have 6 guesses left.
 Available letters: bcdefghijklmnopquvwxyz
 Please guess a letter: m
 Oops! That letter is not in my word: ta_ t
 ------------
 You have 5 guesses left.
 Available letters: bcdefghijklnopquvwxyz
 Please guess a letter: c
 Good guess: tact
 ------------
 Congratulations, you won!
```

### Losing game

```bash
Loading word list from file...
 55900 words loaded.
 Welcome to the game Hangman!
 I am thinking of a word that is 4 letters long
 -----------
 You have 8 guesses left
 Available Letters: abcdefghijklmnopqrstuvwxyz
 Please guess a letter: a
 Oops! That letter is not in my word: _ _ _ _
 -----------
 You have 7 guesses left
 Available Letters: bcdefghijklmnopqrstuvwxyz
 Please guess a letter: b
 Oops! That letter is not in my word: _ _ _ _
 -----------
 You have 6 guesses left
 Available Letters: cdefghijklmnopqrstuvwxyz
 Please guess a letter: c
 Oops! That letter is not in my word: _ _ _ _
 -----------
 You have 5 guesses left
 Available Letters: defghijklmnopqrstuvwxyz
 Please guess a letter: d
 Oops! That letter is not in my word: _ _ _ _
 -----------
 You have 4 guesses left
 Available Letters: efghijklmnopqrstuvwxyz
 Please guess a letter: e
 Good guess: e_ _ e
 -----------
 You have 4 guesses left
 Available Letters: fghijklmnopqrstuvwxyz
 Please guess a letter: f
 Oops! That letter is not in my word: e_ _ e
 -----------
 You have 3 guesses left
 Available Letters: ghijklmnopqrstuvwxyz
 Please guess a letter: g
 Oops! That letter is not in my word: e_ _ e
 -----------
 You have 2 guesses left
 Available Letters: hijklmnopqrstuvwxyz
 Please guess a letter: h
 Oops! That letter is not in my word: e_ _ e
 -----------
 You have 1 guesses left
 Available Letters: ijklmnopqrstuvwxyz
 Please guess a letter: i
 Oops! That letter is not in my word: e_ _ e
 -----------
 Sorry, you ran out of guesses. The word was else.
```
