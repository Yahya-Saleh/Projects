# Get Height
height = as.integer(readline("Enter the pyramid's height: "))

# Build the pyramid
blocks = 1:height
for (i in blocks){
  message(strrep(" ", (height - i)), # Spaces
          strrep("*", i), # Left side
          strrep("*", (i-1)) # Right side
          ) 
}
