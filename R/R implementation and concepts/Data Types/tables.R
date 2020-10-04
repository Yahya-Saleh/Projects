# Load package and data

library(dslabs)
data(murders)

# The "c" in `c()` is short for "concatenate," which is the action of connecting items into a chain
# The function `c()` connects all of the strings within it into a single vector, which we can assign to `x`
x <- c("a", "a", "b", "b", "b", "c")
# Here is an example of what the table function does
table(x)

# Write one line of code to show the number of states per region
table(murders$region)