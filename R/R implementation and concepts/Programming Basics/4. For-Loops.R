# Write a function compute_s_n with argument n that for any given n computes the sum of 1 + 2^2 + ...+ n^2
compute_s_n <- function(n){
  sum((1:n)^2)
}

# Report the value of the sum when n=10
compute_s_n(10)

# Create a vector for storing results
s_n <- vector("numeric", 25)

# write a for-loop to store the results in s_n
for (i in 1:25){
  s_n[i] <- compute_s_n(i)
}