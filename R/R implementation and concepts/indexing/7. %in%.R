# Load the data
library(dslabs)
data(murders)

# Store the 5 abbreviations in `abbs`. (remember that they are character vectors)
abbs <- c("MA", "ME", "MI", "MO", "MU")

# Use the %in% command to check if the entries of abbs are abbreviations in the murders data frame
abbs %in% murders$abb