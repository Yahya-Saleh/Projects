# Loading data
library(dslabs)
data(murders)

# Loading dplyr
library(dplyr)

# add the rate column
murders <- mutate(murders, rate =  total / population * 100000, rank = rank(-rate))

# Create a table, call it my_states, that satisfies both the conditions 
my_states <- data.frame(filter(murders, region %in% c("Northeast", "West") & rate < 1))

# Use select to show only the state name, the murder rate and the rank
select(my_states, state, rate,rank)