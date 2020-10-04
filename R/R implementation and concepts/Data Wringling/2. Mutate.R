# Loading data
library(dslabs)
data(murders)

# Loading dplyr
library(dplyr)

# Defining rate
rate <-  murders$total/ murders$population * 100000

# Redefine murders to include a column named rank
# with the ranks of rate from highest to lowest
murders <- mutate(murders, rank = rank(-rate))