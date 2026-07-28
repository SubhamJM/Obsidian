> Only used when array is static (That means no update to the array is made in any point of time or in between queries)

## Sum Queries:

-  We can make a prefix sum array:
	Example:

```cpp
{1, 3, 4, 8, 6, 1, 4, 2};

// will be converted into prefix sum array:
{1, 4, 8, 16, 22, 23, 27, 29};
```

- Now if i want to calculate sum(a, b) we do:

```cpp
sum(a, b) = sum(0, b) - sum(0, a-1);
```

> **NOTE**
> we can extend this idea to multi dimensions, with this example:

![[MultiDimension_sumquery.png]]


## Minimum Queries:

- Minimum queries are difficult than sum queries.
- best with static array is O(nlogn) time for processin