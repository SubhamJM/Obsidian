```python
import torch
import torch.nn as nn

class Model(nn.Module):
	def __init__(self, num_features):
		super().__init__()
		self.linear1 = nn.Linear(num_features, 3)
		self.relu = nn.ReLU()
		self.linear2 = nn.Linear(3, 1)
		self.sigmoid = nn.Sigmoid()
		
	def forward(self, features):
		out = self.linear1(features)
		out = self.relu(out)
		out = self.linear2(out)
		out = self.sigmoid(out)
		
		return out
		

tensor = torch.rand(10, 5) #10 input 5 features
model = Model(tensor.shape[1])

model(tensor)
```