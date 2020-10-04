# Apply

m1 <- matrix(C<-(1:10),nrow=5, ncol=6)
m1
a_m1 <- apply(m1, 2, sum)
a_m1

# lapply and sapply For vector slicing

below_ave <- function(x) {  
  ave <- mean(x) 
  return(x[x > ave])
}
dt = 1:100
dt_s<- sapply(dt, below_ave)
dt_l<- lapply(dt, below_ave)
identical(dt_s, dt_l)

# tapply

data(iris)
tapply(iris$Sepal.Width, iris$Species, median)

# mapple

mapply(rep, 1:4, 4:1)
