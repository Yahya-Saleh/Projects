# Crack

A program that brute forces a given hash, and returns the text used to generate the hash.

## Linux shadow

On most systems running Linux these days is a file called `/etc/shadow`, which contains usernames and passwords. Fortunately, the passwords therein aren’t stored "in the clear" but are instead encrypted using a "one-way hash function." When a user logs into these systems by typing a username and password, the latter is encrypted with the very same hash function, and the result is compared against the username’s entry in `/etc/shadow`. If the two hashes match, the user is allowed in.

Even though passwords in `/etc/shadow` are hashed, the hash function is not always that strong. Quite often are adversaries, upon obtaining that file somehow, able to guess (and check) users' passwords or crack them using brute force (i.e., trying all possible passwords).

Inside [`Hashes.txt`](Hashes.txt) is what `/etc/shadow` might look like, albeit simplified, wherein each line is formatted as username:hash. The first 2 characters of any hash is the **salt**.

## Salt

Salt is a code used along side the word when generating the hash. the first two characters of a hash is the salt used to generate it. This knowledge is used when constructing [`crack.c`](crack.c) to reconstruct the hashes using the salt.

> 50EAWV4miFscA

In this hash, for example, the salt is 50.

## Usage of crack.c

```bash
$ ./crack 50fkUxYHbnXGw
rofl
```

The program takes in a hash as a second argument and prints out the word after trying every possible word against it with length 5 or less.

## Crypter.c

This program was developed to generate simple hashes to test [`crack.c`](crack.c).

### Usage

```bash
$ ./crypter YY yahya
YYl9roZ.RJCtg
```

Takes in salt and a word as arguments and returns a crypted message.
