1. **\_\_buitin_clz(x):** The number of leading zeros
2. **\_\_builtin_ctz(x):** The number of trailing zeros
3. **\_\_builtin_popcount(x):** The number of one's in the bitstring
4. **\_\_builtin_parity(x):** the parity of number of one's in the bitstring

```cpp
int x = 5328; // 00000000000000000001010011010000
cout << __builtin_clz(x) << "\n"; // 19
cout << __builtin_ctz(x) << "\n"; // 4
cout << __builtin_popcount(x) << "\n"; // 5
cout << __builtin_parity(x) << "\n"; // 1
```

