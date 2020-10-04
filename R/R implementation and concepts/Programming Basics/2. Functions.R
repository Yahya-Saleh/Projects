# Create function called `sum_n`that for any given value, say n,
# creates the vector 1:n, and then computes the sum of the integers from 1 to n.
sum_n <- function(n){
  sum(1:n)
}
# Use the function to determine the sum of integers from 1 to 5000
sum_n(5000)

# Create `altman_plot` takes two arguments x and y and plots y-x (on the y-axis)
# against x+y (on the x-axis).
altman_plot <- function(x, y){
  plot(x+y, y-x)
}