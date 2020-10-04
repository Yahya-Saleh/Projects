# Loading data
library(dslabs)
data(murders)

# Load dplyr
library(dplyr)

# Use select to only show state names and abbreviations from murders
select(murders, state, abb)