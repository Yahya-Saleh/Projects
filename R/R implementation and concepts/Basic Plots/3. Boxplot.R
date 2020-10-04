# Load the datasets and define some variables
library(dslabs)
data(murders)

# Create a boxplot of state populations by region for the murders dataset
boxplot(population~region, data = murders)