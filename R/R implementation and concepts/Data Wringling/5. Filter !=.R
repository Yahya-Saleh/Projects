# Loading data
library(dslabs)
data(murders)

# Loading dplyr
library(dplyr)

# Use filter to create a new data frame no_south
no_south <- data.frame(filter(murders, region != "South"))

# Use nrow() to calculate the number of rows
nrow(no_south)