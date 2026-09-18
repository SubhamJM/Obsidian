```r
A <- array(
    201:224,
    dim = c(3, 4, 2)
)

# 3 rows 4 cols 2 layers
```

# naming dimensions:

```r
dimnames(A) <- list(
    Branch = c("B1", "B2", "B3"),
    Product = c("P1", "P2", "P3", "P4"),
    Month = c("Jan", "Feb")
)
```



