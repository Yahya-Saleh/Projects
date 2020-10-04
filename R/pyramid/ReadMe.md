# Pyramid

Builds a pyramid with the specified height. This simple project relies on dandling for loops and vectors.

## Usage

```R
> height = as.integer(readline("Enter the pyramid's height: "))
Enter the pyramid's height: 10

> # Build the pyramid
> blocks = 1:height

> for (i in blocks){
+   message(strrep(" ", (height - i)), # Spaces
+           strrep("*", i), # Left side
+           strrep("*", (i-1)) # Right si .... [TRUNCATED] 
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
```
