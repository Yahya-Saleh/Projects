# Load data
library(dslabs)
data("murders")

# Assign the state abbreviation when the state name is longer than 8 characters 
new_names <- ifelse(nchar(murders$state) <= 8, murders$state, murders$abb)
