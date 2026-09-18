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