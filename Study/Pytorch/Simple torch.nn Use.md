```python
import torch
import torch.nn as nn

class Model(nn.Module):
	def __init__(self, num_features):
		super().__init__()
		self.linear1 = nn.Linear(num_features, 3)
		self.ReLU
```