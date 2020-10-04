# importing the data
library(dslabs)
data(murders)

# Access the `state` variable and store it in an object 
states <- murders$state 

# Sort the object alphabetically and redefine the object 
states <- sort(states) 

# Report the first alphabetical value  
states[1]

# Access population values from the dataset and store it in pop
# Sort the object and save it in the same object 
pop <- sort(murders$population)

# Report the smallest population size 
pop[1]
