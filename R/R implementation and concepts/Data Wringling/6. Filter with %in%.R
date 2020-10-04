# Loading data
library(dslabs)
data(murders)

# Loading dplyr
library(dplyr)

# Create a new data frame called murders_nw with only the states from the northeast and the west
murders_nw <- data.frame(filter(murders, region %in% c("Northeast", "West")))

# Number of states (rows) in this category 
nrow(murders_nw)