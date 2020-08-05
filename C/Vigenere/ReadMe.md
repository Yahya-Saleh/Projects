# Vigenere

Takes in a plaintext and a keyword, and returns a ciphertext. for better understanding of thos project check the [`Caesar project`](../Caesar).

## Vigenère’s cipher

**Vigenère’s cipher** improves upon Caesar’s cipher by encrypting messages using a sequence of keys (a keyword). In other words, if p is some **plaintext** and k is a keyword (i.e., an alphabetical string, whereby A represents 0, B represents 1, C represents 2, …​, and Z represents 25), then each letter, $c_i$, in the **cipher text**, c, is computed as:

> $c_i = (p_i + k_j)$ % 26

Note this cipher’s use of k_j as opposed to just k. And if k is shorter than p, then the letters in k must be reused cyclically as many times as it takes to encrypt p.

## Usage

```bash
$ ./vigenere bacon
plaintext: Meet me at the park at eleven am
ciphertext: Negh zf av huf pcfx bt gzrwep oz
```

This program takes in a keyword, i.e. a string, as a second input. It then prompts the user for a plain text, returning its ciphertext.
