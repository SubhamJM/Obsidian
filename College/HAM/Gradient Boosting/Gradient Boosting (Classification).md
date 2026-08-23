# Intuition for this:

- We calculate initial prediction by first calculating log(odds) for yes/no type binary prediction:
  if 4 are yes and 2 are no then log(odds) =  log(4/2) = 0.7
- Then we use this to calculate the initial prediction:
![[Pasted image 20260823095440.png]]

- Now we compare it to a threshold like 0.5 and make predictions that all are yes.

![[Pasted image 20260823095544.png]]

- Now again we calculate the residuals using the predictions and observed value.

