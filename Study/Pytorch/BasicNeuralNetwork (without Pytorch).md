## A very basic implementation of ANN

- We create a python class for our neural network

### Class implementation:

```python
class SimpleNN():
	def __init__(self, x):
		self.weights = torch.rand(x.shape[1], 1, dtype=torch.float64, requires_grad=True) ## creates a 30x1 matrix
		
		self.bias = torch.zeros(1, dtype=torch.float64, requires_grad=True)
		
	
	def forward(self, x):
		z = torch.matmul(x, self.weights) + self.bias
		
		return torch.sigmoid(z)
	
	
	def binary_cross_entropy(self, y_pred, y):
		EPSILON = 1e-10
		
		y_pred = torch.clamp(y_pred, EPSILON, 1-EPSILON)
		
		
		loss = -torch.mean(y * torch.log(y_pred) + (1 - y) * torch.log(1 - y_pred))
		
		return loss
```


### The Training loop:

```python
# define loop
for epoch in range(epochs):
	# forward pass
	y_pred = model.forward(xtrain_tensor)
	
	# loss calculate
	loss = model.binary_cross_entropy(y_pred, ytrain_tensor)
	print(f'epoch: {epoch+1}, loss: {loss.item()}')
	
	# backward pass
	loss.backward()
	
	# parameters update
	with torch.no_grad():
	model.weights -= learning_rate * model.weights.grad
	model.bias -= learning_rate * model.bias.grad
	
	#zero gradients
	model.weights.grad.zero_()
	model.bias.grad.zero_()
```

