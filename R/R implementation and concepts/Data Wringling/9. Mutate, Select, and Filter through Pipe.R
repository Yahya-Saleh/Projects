# Loading data
library(dslabs)
data(murders)

# Load library
library(dplyr)

# Create new data frame called my_states (with specifications in the instructions)
my_states <- data.frame(murders) %>% mutate(rate = total / population * 100000, rank = rank(-rate)) %>% filter(region %in% c("Northeast", "West") & rate < 1) %>% select(state, rate, rank)