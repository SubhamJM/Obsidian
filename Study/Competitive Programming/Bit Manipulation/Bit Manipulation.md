### Types of bits

- Signed
- Unsigned

#### Signed Bit Representation:

- for int, there are 32 bits for binary representation, one of which is used only for +ve or -ve sign
- Remaining Accounts for the numbers from -2<sup>31</sup> to 2<sup>31</sup>-1 numbers

 **Some Properties**:
 1. ~x + 1 = -x
	- eg. 29's negation is -30

```cpp
~x = -x - 1
```

2. x + (-x) = 0 (due to bits overflowing)
3. For going from signed to unsigned: -x = 2<sup>n</sup> - x

```cpp
-x = power(2, n) - x
```

- Learn more about bit operations in [[Bit Operations]]
