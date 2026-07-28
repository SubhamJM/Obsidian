**Q.** What are Tensors?
- Tensors are fast and multidimensional array used for fast computing.
- Tensor can have any number of dimensions
- Tensors use TPU instead of GPU for calculations.

### Dimensions
1. 0-Dimensional ---- Numbers like 5.0, 10, etc
2. 1-Dimensional ---- arrays like {1,2,3,4}
	Similarly 2 and 3..... etc

### Usage in deep learning
1. Data Storage
2. Weights and Biases storing (and tensor operations)
3. Matrix operations
4. Training process

---

### Some Syntax
> torch.manual_seed(42)   // creates a seed so that random always provide same values

```python
torch.empty(2, 3)  #creates an empty space in memory
torch.zeros((2, 3), dtype=torch.int32)  #creates a tensor with 0s
torch.ones(2, 3)  #creates a tensor with 1s
torch.rand(2,3)  #initiates with random values within 0 - 1
torch.tensor({1,2,3}, {2,3,4})  #creates a specific tensor
torch.eye(5)  #creates an identity matrix
torch.full((3,3), 5)  #creates a 3x3 matrix with all values 5
torch.empty_like(x)  #creates a tensor with same shape as x
torch.zeros_like(x)
torch.ones_like(x)
x.dtype
```

### Reshaping tensors
```python
a = torch.ones(4,4)
b = a.reshape(2,2,2,2) ## reshapes
b = a.flatten() ## flattens

b = a.unsqueeze(0) ## adds a 1 dimension in the 0th index
b = a.squeeze(0) ## removes the dimension at 0th index


## convert into numpy array
b = a.numpy()
```

### Some dtypes

![[Dtypes_in_torch.png]]


---

### Mathematical Operations on Tensors

1. **Scalar operations**

```python
x = torch.rand(2, 3)

x + 2 #adds 2 to all elements
x - 2 #subtracts 2 from all elements
x * 2
x / 2 
x ** 2 #.....
```

2. **Element wise operations between matrices**

```python
a = torch.rand(2, 3)
b = torch.rand(2, 3)

a + b
a - b
a * b
a / b
a ** b 

## All of these are element wise operations
```

3. **Stats Operations**

```python
a = tensor.rand(2, 3)

torch.mean(a)
torch.median(a)
torch.std(a)
torch.max(a)
torch.min(a)
torch.var(a)
torch.argmax(a)
```

4. **Matrix Operations**

```python
m1 = torch.rand(2,3)
m2 = torch.rand(3, 2)

m3 = torch.matmul(m1, m2) # Matrix multiplications
dot_product = torch.dot(m1, m2) # Dot product
transpose = torch.transpose(m1, 0, 1) # Transpose
determinant = torch.det(m1)
inverse = torch.inverse(m1)
```


### Tensor operations on GPU

> Do this to make the main device to be the GPU

```python
torch.cuda.is_available() # should return true

device = torch.device('cuda')
torch.rand((2,3), device=device) # now this tensor will run on the GPU
```
