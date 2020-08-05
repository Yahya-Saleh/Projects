# Caesar

Caesar’s algorithm (i.e., cipher) encrypts messages by “rotating” each letter by k positions. More formally, if p is some **plaintext** (i.e., an unencrypted message), $p_{i}$ is the $i^{th}$ character in p, and k is a **secret key** (i.e., a non-negative integer), then each letter, $c_i$, in the **ciphertext**, c, is computed as

> $c_i = (p_i + k)$ % 26

## Usage

This program takes in the key, a number of characters to shift, as a second argument and asks the user for a plain text returning a ciphertext using the given key.

```bash
$ ./caesar 13
plaintext:  hello, world
ciphertext: uryyb, jbeyq
```
