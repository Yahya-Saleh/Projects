# Questions
Those concepts are essential in developing the WhoDunit.c program

## What's `stdint.h`?

 It provides the user with a set of typedefs that specify exact-width integer types. The naming convention for exact-width integer types is intN_t for signed int and uintN_t for unsigned int where N is the number of bits. Signed int can hold integers from -32767 through 32767 inclusive (INT_MIN and INT_MAX respectively). Where as, unsigned int can hold integers from 0 through 65535 inclusive (UINT_MIN and UINT_MAX respectively). In addition, stdint.h defines limits of integer types capable of holding object pointers such as UINTPTR_MAX, the value of which depends on the processor and its address range

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

 To create a new integer variable type that's either signed or unsigned and limited to a certain number of bits. they indicate whether the variable is signed or unsigned, and how many bits can the variable store.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

8, 32, 32, 16

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

ASCII

## What's the difference between `bfSize` and `biSize`?

BfSize is the size, in bytes, of the bitmap file, where as biSize is the number of bytes required by the bitmap.  

## What does it mean if `biHeight` is negative?

 The bitmap is a top-down DIB (device-independent bitmap) and its origin is the upper-left corner. In a top-down format, the top row of the image is the first row in memory, followed by the next row down. The bottom row of the image is the last row in the buffer. With a top-down DIB, the first byte in memory is the top-left pixel of the image.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in `copy.c`?

 If the infile doesn't exist or is in a different format.

## Why is the third argument to `fread` always `1` in our code?

 Because there's only one bitmapfileheader and one bitmapinfoheader and the third argument is the quantity.

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

 Fseek() function is used to move file pointer position to the given location. In copy.c it offsets the padding bytes if any. It's easier to deal with multiples of 4, so padding indicates if there's any non-multiple of 4 and fseek offsets them by adding 0s until the digits become a multiple of 4.

## What is `SEEK_CUR`?

 It's one of the orgins that specify.
