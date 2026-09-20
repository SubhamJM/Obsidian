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
lines(x, y)
```

# abline()

```r
#adds horizontal or vertical lines:
abline(h=0)
abline(v=0)
abline(model) # regression
```

# Legend

```r
legend(
    "topright",
    legend=c("sin(x)", "cos(x)"),
    lty=c(1,2),
    col=c(1,2)  # deafultsq
)
# lty = line type
1 = solid
2 = dashed
3 = dotted
4 = dotdash
5 = longdash
# col = color

```


# Curve

```r
curve(x^2 - 4*x + 5, from=0, to=6) # forms a curve
```

# Histogram

```r
hist(marks)

breaks <- seq(30, 100, by=10)

h <- hist(
    marks,
    breaks=breaks
)

#this labels the bar graphs with count
text(
    h$mids,
    h$counts,
    labels=h$counts
)
```

# Density

```r
# smoothing out histogram
d <- density(marks)
plot(d)
```