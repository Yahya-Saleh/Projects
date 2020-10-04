# Define temp
temp <- c(35, 88, 42, 84, 81, 30)
city <- c("Beijing", "Lagos", "Paris", "Rio de Janeiro", "San Juan", "Toronto")
names(temp) <- city

# temperatures of the first three cities in the list:
temp[1:3]

# Access the temperatures of Paris and San Juan
temp[c("Paris","San Juan")]