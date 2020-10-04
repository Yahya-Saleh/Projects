# Load package and data

library(dslabs)
data(murders)

str(murders)

# Use the function names to extract the variable names 
names(murders)


# To access the population variable from the murders dataset use this code:
p <- murders$population 

# To determine the class of object `p` we use this code:
class(p)

# Use the accessor to extract state abbreviations and assign it to a
a <- murders$abb

# Determine the class of a
class(a)