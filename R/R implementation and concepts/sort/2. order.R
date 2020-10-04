# importing the data
library(dslabs)
data(murders)

# Access population from the dataset and store it in pop
pop <- murders$population

# Use the command order to find the vector of indexes that order pop and store in object ord
ord <- order(pop)

# Find the index number of the entry with the smallest population size
ord[1]