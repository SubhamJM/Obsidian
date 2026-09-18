# Binomial Distribution:

- dbinom → probability of exactly x
- pbinom → cumulative probability
- qbinom → quantile / percentile
- rbinom → random simulation

```r
#Probability of exactly 2 successes:
dbinom(2, size=10, prob=0.3)

# Probability of at most x: P(X <= 2)  
pbinom(2, 10, 0.3)

# 95th percentile:
qbinom(0.95, 10, 0.3)

# simulates 1000 random experiment to find number of success:
x <- rbinom( 1000, size=10, prob=0.3 )
```

# Poisson Distribution:

```r
# exactly x events occur
dpois(x, lambda=4)
#eg
dpois(3, 4)

# at most x P(X <= 3)
ppois(3, 4)

# 95th percentile:
qpois(0.95, 4)
```

# Normal Distribution:

```r
dnorm → density
pnorm → cumulative probability
qnorm → percentile
rnorm → random values



```