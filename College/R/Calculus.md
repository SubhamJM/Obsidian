# Symbolic derivative:

```r
# 1. Define the expression
expr <- expression(3 * x^2 + 10 * x + 2)

# 2. Compute the symbolic derivative with respect to 'x'
f_prime <- D(expr, "x")

# Print the result
print(f_prime)
# Output: 3 * (2 * x) + 10
```

# Evaluating derivative:

```r
# Define the math expression
expr <- expression(x^3 + 2*x^2 + 5)

# Calculate the first derivative with respect to "x"
df_dx <- D(expr, "x")
print(df_dx)
# Output: 3 * x^2 + 2 * (2 * x)

# Evaluate at a specific value (e.g., x = 3)
x <- 3
eval(df_dx) 
# Output: 39

```


# Integration:

```r
f <- function(x) {
    x^2
}

integrate(f, lower=0, upper=2)
```

# Optimize:

```r
# 1. Define the function
my_function <- function(x) {
  return((x - 3)^2 + 5)
}

# 2. Run the optimization to find the minimum
result <- optimize(my_function, interval = c(0, 10), maximum = FALSE)

# 3. View results
results$minimum
results$objective
```

- objective - value of x for which it is minimum
- objective - minimum value of function