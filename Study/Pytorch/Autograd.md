- Basically automatically differentiates a function or [[Tensors]]
- a library inside of pytorch
- Very usefull in back-propagation

### Syntax:

```python
x = torch.tensor(3.0, requires_grad=True)
y = x**2
z = torch.sin(y)
# this whole chain creates a computation graph 
# x -> square -> y -> sin -> z

z.backward()
x.grad # returns the gradient dz/dx
```

**Another Example**:

```python
x = torch.tensor(6.7)
y = torch.tensor(0.0)

w = torch.tensor(1.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

z = w*x + b
y_pred = torch.sigmoid(z)
loss = binary_cross_entropy_loss(y_pred, y) # User defined loss function L = -[yln(y_pred) + (1-y)ln(1-y_pred)]

loss.backward()

w.grad # dL/dw
b.grad # dL/db
```

---

**NOTE**:

> for multiple passes of gradient descent, the gradient accumulates by addition in the w.grad value, so we have to reset it during every pass like this:

```python
w.grad.zero_()
```

## To Turn off Gradient Tracking:

```python
x.requires_grad_(False)

# another method
z = x.detach() ## creates another tensor with detached autograd

# this will also not track gradient while calculating y
with torch.no_grad():
	y = x**2
```

