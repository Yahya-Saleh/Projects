# Parser

An AI that parses through a given sentence and identifies its structure using **context-free grammar formalism**. [Watch it in action!](https://youtu.be/3vewB8FlIB8)

## Usage

Pass in a text file as a second argument, or manual type in a sentence when prompted.

```bash
python -u parser.py sentences/4.txt
                        S
             ___________|_________________________
            S                            |        |
   _________|___                         |        |
  |             VP                       |        |
  |      _______|___                     |        |
  |     |           PP                   |        |
  |     |    _______|___                 |        |
  |     |   |           NP               |        S
  |     |   |    _______|___             |     ___|_____      
  NP    |   |   |          Nom           |    NP        |
  |     |   |   |        ___|_____       |    |         |
 Nom    VP  |   |       |        Nom     |   Nom        VP
  |     |   |   |       |         |      |    |         |
  N     V   P  Det     Adj        N     Conj  N         V
  |     |   |   |       |         |      |    |         |
holmes sat  in the     red     armchair and   he     chuckled

Noun Phrase Chunks
holmes
the red armchair
he
```

## Table of content

- [Parser](#parser)
  - [Usage](#usage)
  - [Table of content](#table-of-content)
  - [Parsing](#parsing)
  - [Context-free grammar](#context-free-grammar)
  - [Sentences](#sentences)
  - [Acknowledgements](#acknowledgements)

---

## Parsing

A common task in natural language processing is **parsing**, the process of determining the structure of a sentence. This is useful for a number of reasons: knowing the structure of a sentence can help a computer to better understand the meaning of the sentence, and it can also help the computer extract information out of a sentence. In particular, it’s often useful to extract noun phrases out of a sentence to get an understanding for what the sentence is about.

## Context-free grammar

The objective is to start with a *nonterminal symbol* `S` (representing a sentence) and repeatedly apply context-free grammar rules until we generate a complete sentence of *terminal symbols* (i.e., words). The rule `S -> N V`, for example, means that the S symbol can be rewritten as `N` `V` (a noun followed by a verb). If we also have the rule `N -> "Holmes"` and the rule `V -> "sat"`, we can generate the complete sentence "Holmes sat.".

Of course, noun phrases might not always be as simple as a single word like "Holmes". We might have noun phrases like "my companion" or "a country walk" or "the day before Thursday", which require more complex rules to account for. To account for the phrase "my companion", for example, we might imagine a rule like:

> NP -> N | Det N

In this rule, we say that an `NP` (a “noun phrase”) could be either just a noun (`N`) or a determiner (`Det`) followed by a noun, where determiners include words like "a", "the", and "my". The vertical bar (`|`) just indicates that there are multiple possible ways to rewrite an `NP`, with each possible rewrite separated by a bar.

To incorporate this rule into how we parse a sentence (`S`), we’ll also need to modify our `S -> N V` rule to allow for noun phrases (`NP`s) as the subject of our sentence.

---

## Sentences

The `sentences` directory contains 10 text files each containing a sentence. The goal of `[parser.py](parser.py)` is to parse all of those sentences.

---

## Acknowledgements

The `TERMINALS` global variable along with the `main` function were pre-written by teh CS50AI staff.
