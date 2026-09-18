```r
# forming a matrix
vect <- c(1,2,3,4,5,6,7,8,9)
mat <- matrix(vect, nrow=3, ncol=3, byrow=TRUE/FALSE)
```

- nrow(A)
- ncol(A)
- dim(A)

# Matrix indexing:

```r
A[2,3]
#2nd row, 3rd column
# 1 based indexing

A[2, ]
# select entire 2nd row

A[,3]
# select entire 3rd column
```

# Matrix arithematic:

```r
# All do element wise operations
A + B
A / B
A * B 
```

# Matrix Multiplication:

```r
A %*% B
```

# rbind() and cbind()

```r
rbind(A, B) # row-wise binding 
cbind(A, B) # column wise binding
```

# conditional matrix replacement

```r
A[A < 30] <- 0
# sets all elements less than 30 to 0
```