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

# Evaluating