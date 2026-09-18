```r
product_info <- data.frame(
    product_name = c("Pen", "Book", "Bag"),
    price = c(20, 100, 500),
    available = c(TRUE, TRUE, FALSE)
)
```

# Inspecting data frame:

```r
# structure
str(product_info)

# summary stats
summary(product_info)
```

# Selecting columns

```r
product_info$product_name

product_info[, "product_name"]

# multiple cols
product_info[, c("product_name", "price")]
```

# Filtering rows

```r
product_info[product_info$available == TRUE, ]

product_info[product_info$price > 100, ]
```