```r
# represented by:
vec <- c(1,2,3,4,5)
```

- Vectors can store only one kind of datatype

> 1 based indexing in vectors

# Vector methods:

```r
length(x)
sum(x)
min(x)
max(x)
mean(x)
median(x)
sort(x)
unique(x)
rev(x)
```

# Logical Indexing:

```r
marks <- c(1,2,3,4,5)
marks[marks>=3] # gives c(3,4,5)
```

# Which

```r
x <- c(10,20,30,40,50)
which(x > 20) # returns 3 4 5 as they satisfy

which.max(x)
which.min(x)
# returns max and min index of array
```

