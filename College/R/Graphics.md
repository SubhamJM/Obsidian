```r
x <- 1:10
y <- x^2

plot(x, y)

#labels
plot(
    x,
    y,
    main="My Graph",
    xlab="X",
    ylab="Y"
)

#adds point and line to existing plot:
points(x, y)
```