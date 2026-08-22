From [[Gradient Boosting (Regression)]], I got the intuition behind the algorithm.

- Now we get the mathemtical "WHY?":

## Maths behind Gradient boosting:

*Few terms:*
1. Prediction Function => F(x) = gives prediction
2. Loss function:
	- L(yi, F(xi)) = 1/2(observed - predicted)^2

### Now Steps:

1.  Initialization:
	- Initial Prediction: F(x) = average of all labels
	- this is because taking loss over all data points and minimizing the loss gets us F(x) as average of all labels

2. make a loop for m = 1 to M:
	- compute residuals:
		![[Pasted image 20260823000606.png]]

	- Fit a regression decision tree to input as the features and output as the residuals.
	- Now if a leaf has multiple values ending up there, we use this minimization of loss formula to determine the value at the leaf:
		![[Pasted image 20260823001022.png]]
