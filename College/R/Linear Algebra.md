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
#3(1) + 2(5) + 4(2) = 21
```

# Cross Product:

```r
cross <- c(
    A[2]*B[3] - A[3]*B[2],
    A[3]*B[1] - A[1]*B[3],
    A[1]*B[2] - A[2]*B[1]
)

# verify:
crossprod(cross, A)
crossprod(cross, B)
# both results in 0
```

