- Factors are used for categorical data

```r
category <- factor(
    c(
        "Electronics",
        "Clothing",
        "Furniture",
        "Electronics",
        "Books"
    )
)
```

# Some important:

```r
levels(category)

table(category)

summary(category)
```