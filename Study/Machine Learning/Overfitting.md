### What is Overfitting?

- When the model learns the training data too well into its weights that the model performs poorly on the validation data.
- this majorly happens two times:
	1. when the model is trained for way too long (too many epochs)
	2. when the model parameters are to complex so they learn the input data too well.


![[underfitting_vs_overfitting.png]]


### Fixing Overfitting

- Using [[Regularization]] (L1/L2)
- Using [[Cross-Validation]]
- Reduce Model Complexity
- Getting more training data

***

#### Note:
> There is a concept called Double descent, where the model is trained for way too long and the model now starts to get good results with validation set too (that means the overfitting phase gets over)

Reading more at: [Wikipedia- Double Descent in Machine Learning](https://en.wikipedia.org/wiki/Double_descent)


![[Double_descent.png]]