# Caesar

Takes in a plaintext and an integer and returns a ciphertext by rotating each character.

## Caesar’s algorithm

**Caesar’s algorithm** (i.e., cipher) encrypts messages by “rotating” each letter by k positions. More formally, if p is some **plaintext** (i.e., an unencrypted message), <!-- $p_{i}$ --> <img style="transform: translateY(0.1em); background: white;" src="..\..\Snippets\c\caesar\$p_{i}$.svg"> is the <!-- $i^{th}$ --> <img style="transform: translateY(0.1em); background: white;" src="..\..\Snippets\c\caesar\$i^{th}$ .svg"> character in p, and k is a **secret key** (i.e., a non-negative integer), then each letter, <!-- $c_i$ --> <img style="transform: translateY(0.1em); background: white;" src="..\..\Snippets\c\caesar\$c_i$.svg">, in the **ciphertext**, c, is computed as

> <!-- $c_{i} = (p_i + k) % 26$ --> <img style="transform: translateY(0.1em); background: white;" src="..\..\Snippets\c\caesar\ciphertext formula.svg">

## Usage

```bash
$ ./caesar 13
plaintext:  hello, world
ciphertext: uryyb, jbeyq
```

This program takes in the key, a number of characters to shift, as a second argument and asks the user for a plain text returning a ciphertext using the given key.
