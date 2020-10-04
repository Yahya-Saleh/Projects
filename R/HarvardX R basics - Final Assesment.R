library(dplyr)
library(dslabs)
data(heights)
options(digits = 3)    # report 3 significant digits for all answers

head(heights)

############################### Question 1 ######################################

# How many individuals in the dataset are above average height?
ind <- heights$height > mean(heights$height)
sum(ind)


############################### Question 2 ######################################

# How many individuals in the dataset are above average height and are female?
class(heights$sex)
sum(ind & heights$sex == "Female")


############################### Question 3 ######################################

# What proportion of individuals in the dataset are female?
mean(heights$sex == "Female")


############################### Question 4 ######################################

heights$sex[which.min(heights$height)]

# Determine the minimum height in the heights dataset.
min_height <- min(heights$height)

# Use the match() function to determine the index of the first individual with
# the minimum height.
min_ind <- match(min_height, heights$height)

# Subset the sex column of the dataset by the index in 4b to determine the
# individual's sex.
heights$sex[min_ind]


############################### Question 5 ######################################

# Determine the maximum height.
max(heights$height)

# Write code to create a vector x that includes the integers between the
# minimum and maximum heights (as numbers)
x <- 50:82

# How many of the integers in x are NOT heights in the dataset?
sum(!x %in% heights$height)


############################### Question 6 ######################################

# Using the heights dataset, create a new column of heights in centimeters named
# ht_cm. Recall that 1 inch = 2.54 centimeters. Save the resulting dataset as
# heights2.
heights2 <- mutate(heights, ht_cm = heights$height * 2.54)

# What is the height in centimeters of the 18th individual (index 18)?
heights2$ht_cm[18]

# What is the mean height in centimeters?
mean(heights2$ht_cm)


############################### Question 7 ######################################

# Create a data frame females by filtering the heights2 data to contain only
# female individuals.
females <- data.frame(filter(heights2, sex == "Female"))

# How many females are in the heights2 dataset?
count(females)

# What is the mean height of the females in centimeters?
mean(females$ht_cm)


############################### Question 8 ######################################

library(dslabs)
data(olive)

head(olive)

# Plot the percent palmitic acid versus palmitoleic acid in a scatterplot.
plot(olive$palmitic, olive$palmitoleic)

# What relationship do you see?
# There is a positive linear relationship between palmitic and palmitoleic.


############################### Question 9 ######################################

# Create a histogram of the percentage of eicosenoic acid in olive.
hist(olive$eicosenoic)

# Which of the following is true?
# The most common value of eicosenoic acid is below 0.05%.


############################### Question 9 ######################################

# Make a boxplot of palmitic acid percentage in olive with separate
# distributions for each region.
boxplot(olive$palmitic~olive$region)

# Which region has the highest median palmitic acid percentage?
# Southern Italy

# Which region has the most variable palmitic acid percentage?
# Southern Italy