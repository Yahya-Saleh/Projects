# Caesar

Takes in a plaintext and an integer and returns a ciphertext by rotating each character.

## Usage

```bash
$ ./caesar 13
plaintext:  hello, world
ciphertext: uryyb, jbeyq
```

This program takes in the key, a number of characters to shift, as a second argument and asks the user for a plain text returning a ciphertext using the given key.

## Caesar’s algorithm

**Caesar’s algorithm** (i.e., cipher) encrypts messages by “rotating” each letter by k positions. More formally, if p is some **plaintext** (i.e., an unencrypted message), <!-- $p_{i}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=p_%7Bi%7D"> is the <!-- $i^{th}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=i%5E%7Bth%7D"> character in p, and k is a **secret key** (i.e., a non-negative integer), then each letter, <!-- $c_i$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=c_i">, in the **ciphertext**, c, is computed as

> <!-- $c_{i} = (p_i + k)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=c_%7Bi%7D%20%3D%20(p_i%20%2B%20k)"> % 26
