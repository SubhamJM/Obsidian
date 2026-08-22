From [[Gradient Boosting (Regression)]], I got the intuition behind the algorithm.

- Now we get the mathemtical "WHY?":

## Maths behind Gradient boosting:

*Few terms:*
1. Prediction Function => F(x) = gives prediction
2. Loss function:
	- L(yi, F(xi)) = 1/2(observed - predicted)^2

### Now:

- Initial Prediction: F(x) = average of all labels
- this is because taking loss over all data points and minimizing the loss 

