- AX = B

```r
A <- matrix(
    c(
        3,1,-1,
        1,2,1,
        2,-1,3
    ),
    nrow=3,
    byrow=TRUE
)

B <- c(5,6,9)

#solving:

X <- solve(A,B)

# check
(A %*% X) == B
```

# Dot Product:

```r
A <- c(3,2,4)
B <- c(1,5,2)

crossprod(A, B)


```