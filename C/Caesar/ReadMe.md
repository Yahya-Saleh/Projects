# Caesar
Caesar’s algorithm (i.e., cipher) encrypts messages by “rotating” each letter by k positions. More formally, if p is some plaintext (i.e., an unencrypted message), pi is the ith character in p, and k is a secret key (i.e., a non-negative integer), then each letter, ci, in the ciphertext, c, is computed as
```c
ci = (pi + k) % 26
```

## Functionality
This program takes in the key, a number of characters to shift, as a second argument and the asks the user for a plain text- returning a cipher text using the given key.
```
$ ./caesar 13
plaintext:  hello, world
ciphertext: uryyb, jbeyq
```