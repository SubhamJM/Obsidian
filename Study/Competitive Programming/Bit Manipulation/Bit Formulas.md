**Some Important bit formulas:**

```cpp
~x = -x - 1

x & (1 << k) // returns the kth bit from right of x
x | (1 << k) // makes the kth bit = 1 in x
x & ~(1 << k) // makes the kth bit = 0 in x
x ^ (1 << k) // inverts the kth bit in x

x & (x-1) //sets the last 1 bit to 0 in x
x | (x-1) // inverts all the bits after the last 1 in x
x & -x // sets all bits to 0 except the first one from the right

if (x & (x-1) == 0) // means x is a power of 2
```

