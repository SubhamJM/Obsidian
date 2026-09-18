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

