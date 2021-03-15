# Speller

Using the trie data structure this program loads a text file and a dictionary, dictionaries/large by default, and outputs all of the spelling mistakes along with the speed and time of execution.

## Usage

```bash
Usage: speller [dictionary] text
```

where dictionary is assumed to be a file containing a list of lowercase words, one per line, and text is a file to be spell-checked. *As the brackets suggest, provision of dictionary is optional*; if this argument is omitted, speller will use dictionaries/large by default. In other words, running:

```bash
./speller text
```

will be equivalent to running:

```bash
./speller dictionaries/large text
```

where text is the file you wish to spell-check. Suffice it to say, the former is easier to type!

---

## Understanding

Theoretically, on input of size n, an algorithm with a running time of n is "asymptotically equivalent," in terms of O, to an algorithm with a running time of 2n.

Indeed, when describing the running time of an algorithm, we typically focus on the **dominant** (i.e., most impactful) term (i.e., n in this case, since n could be much larger than 2). In the real world, though, the fact of the matter is that 2n feels twice as slow as n.

---

## Breaking down the code

### Dictionary.h

Open up dictionary.h, and you’ll see some new syntax, including a few lines that mention [`DICTIONARY_H`](dictionary.h).

![dictionary's functionality](../../Snippets/C/speller/dictionary's%20functionality.png)

Those lines just ensure that, even though dictionary.c and speller.c (which you’ll see in a moment) `#include` this file, clang will only compile it once.

`#ifndef` checks whether the given token, in this case [`DICTIONARY_H`](dictionary.h), has been `#defined` earlier in the file or in an included file; if not, it includes the code between it and the closing `#endif` statement. So, this way if we have defined [`DICTIONARY_H`](dictionary.h) before `#ifndef` will prevent us from defining it again.

Also notice our use of `#define`, a **"preprocessor directive"** that defines a "constant" called *LENGTH* that has a value of 45. clang will replace any mentions of *LENGTH* in the code with, literally, 45.

### Dictionary.c

Notice how, atop the file, defined a struct called `node` that represents a node in a trie. And we’ve declared a global array, root, that represents the root (i.e., topmost node) of a trie.

![node definition](../../Snippets/C/speller/node%20definition.png)

below those lines some code is written that initializes the trie with just one node at first for its root, each of whose children is initialized to NULL. And I’ve written some code that opens dictionary, which is the file name of a dictionary to load. And also some code that iterates over that dictionary and reads the words therein, one at a time, into a buffer (i.e., string) called `word`. Then each word is inserted into the trie. Thereafter, we do close the file, though, and then return true to indicate success.

### Speller.c

Notice how, by way of a function called getrusage, we’ll be "benchmarking" (i.e., timing the execution of) the implementations of check, load, size, and unload. Ultimately, we report each misspelling in that file along with a bunch of statistics.

## Large Dictionary

Within the default dictionary, mind you, are 143,091 words, all of which must be loaded into memory! In fact, take a peek at that file to get a sense of its structure and size. Notice that every word in that file appears in lowercase (even, for simplicity, proper nouns and acronyms). From top to bottom, the file is sorted lexicographically, with only one word per line (each of which ends with \n). No word is longer than 45 characters, and no word appears more than once.

## text/

This directory holds many scripts including but not limited to the following:

- La La Land.
- The text of the Affordable Care Act.
- Three million bytes from Tolstoy.
- Some excerpts from The Federalist Papers and Shakespeare.
- The entirety of the King James V Bible and the Koran.

you can take a look at the directory yourself to get a sense of the scripts within.

Makefile
Makefile, a configuration file that tells make, in the CS50 IDE, exactly what to do. Open up Makefile, and you should see three lines (not four), telling the computer that every time you type make or make speller the following happens:

- Tells make how to compile speller.c into machine code (i.e., speller.o).
- Tells make how to compile dictionary.c into machine code (i.e., dictionary.o).
- Tells make to link speller.o and dictionary.o in a file called speller.
  
> Note: you can copy all 3 lines into the terminal and they will run correctly
