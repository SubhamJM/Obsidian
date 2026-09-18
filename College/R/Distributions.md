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
```