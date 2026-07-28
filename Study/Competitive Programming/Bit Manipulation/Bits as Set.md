- It is an application of bit manipulation
- using bit sequences as sets is much more efficient than storing numbers in memory
- representing numebrs based on their value to position mapping

**Example**:
{1, 3, 4, 8} set can be represented as 10001101 as an 8 bit string

> So in integers we can store a total of 32 bits inside of a set

- to get the bitstring from the numbers:

```cpp
for (int i = 31; i >= 0; i--) {
	if (x&(1<<i)) cout << "1";
	else cout << "0";
}
```

This uses the formula from [[Bit Formulas]]

### Set Operations:

- Intersection:        a&b
- Union:      a|b
- Complement:        ~a
- difference:      a&(~b)

[[InBuilt Bit Functions]] (Reference)
> **Note:**
> using \_\_builtin_popcount(x) gives the number of elements in the set x

## Important:

- This loop goes through all the subsets of length k
```cpp
for (int i = 0; i < (1<<k); i++){
	// code block
}
```



