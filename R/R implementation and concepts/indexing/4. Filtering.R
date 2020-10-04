# Load the data
library(dslabs)
data(murders)

# Store the murder rate per 100,000 for each state, in `murder_rate`
murder_rate <- murders$total/murders$population*100000

# Store the `murder_rate < 1` in `low` 
low <- murder_rate < 1

# Create a vector ind for states in the Northeast and with murder rates lower than 1. 
ind <- low & murders$region == "Northeast"

# Names of states in `ind` 
murders$state[ind]