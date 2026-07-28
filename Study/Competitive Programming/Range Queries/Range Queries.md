### Some Common Queries are:

- In the range [a, b]
1. Sum(a, b)
2. min(a, b)
3. max(a, b)

### Example:

```cpp
vector<int> array = {1,3,8,4,6,1,3,4};

sum(3,6) = 14
min(3,6) = 1
max(3,6) = 6
```


- We can do it in O(n) using simple loops.
- But we can optimize the algorithm for consequtive queries like 3 to 6

## Two methods of doing range queries:

1. [[Static Array Queries]]
2. [[Binary Indexed Tree]]