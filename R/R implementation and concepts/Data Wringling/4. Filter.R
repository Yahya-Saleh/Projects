# Loading data
library(dslabs)
data(murders)

# Loading dplyr
library(dplyr)

# Add the necessary columns
murders <- mutate(murders, rate = total/population * 100000, rank = rank(-rate))

# Filter to show the top 5 states with the highest murder rates
filter(murders, rank <= 5)