# Sorting:

```r
names <- c("S1","S2","S3","S4")
marks <- c(78,88,69,94)

sort(marks)

sort(marks, decreasing=TRUE)
```

# Order:

- Order gives the index order which will bring the array into sorted form

```r
idx <- order(marks, decreasing=TRUE)

names[idx]
marks[idx]
```

# Rank:

- Gives a vector with rank of each element

```r
x <- c(40, 10, 30, 20)
rank(x)
# Output: 4 1 3 2
```