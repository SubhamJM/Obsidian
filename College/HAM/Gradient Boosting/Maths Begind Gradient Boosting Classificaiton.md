- We get intuition behind [[Gradient Boosting (Classification)]], but now here's the Mathematical WHY?

# Maths:

*few Terms*:
- F(x) is the prediction model
- L(y, F(x)) is the loss function 

> Here loss function is different from regression because classification has binary labels.

![[Pasted image 20260823100736.png]]

- This is called the negative log likelyhood

> The better the prediction the larger the log likelyhood, so we multiply it by -1 to make it a loss function which we need to minimize.

- Converting the predicted notation to log(odds) notation for convinience.

![[Pasted image 20260823101210.png]]

- The derivative of the loss ultimately becomes the residuals:
![[Pasted image 20260823101335.png]]



# Steps to make the decision trees:

- All the steps are now similar to [[Maths Begind Gradient Boosting Classificaiton]] after defining loss function and residuals for this classification problem.

