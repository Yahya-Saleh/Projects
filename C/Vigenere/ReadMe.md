# Vigenere
Vigenère’s cipher improves upon Caesar’s cipher by encrypting messages using a sequence of keys (or, put another way, a keyword). In other words, if p is some plaintext and k is a keyword (i.e., an alphabetical string, whereby A represents 0, B represents 1, C represents 2, …​, and Z represents 25), then each letter, ci, in the cipher text, c, is computed as:
```c
ci = (pi + kj) % 26
```
Note this cipher’s use of kj as opposed to just k. And if k is shorter than p, then the letters in k must be reused cyclically as many times as it takes to encrypt p.

## Usage
This program takes in a keyword, i.e. a string, as a second input. It then prompts the user for a plain text, returning its cipher text.
```
$ ./vigenere bacon
plaintext: Meet me at the park at eleven am
ciphertext: Negh zf av huf pcfx bt gzrwep oz
```