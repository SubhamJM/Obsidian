# Cumsum()

```r
production <- c(118,135,92,147)
cumsum(production)
#118
#253
#345
#492
```

- To find at which point the probability reaches 90%

```r
prob <- c(0.1, 0.2, 0.3, 0.4)

which(cumsum(prob) >= 0.90)[1]
```