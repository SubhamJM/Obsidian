## Basic Intuition (Understanding for regression):

- it _starts_ with a _single leaf_ which only _predicts the average value_ of the output values in training set.
- It then calculates ==residuals== = observed value - predicted value.
- It then Expands the tree to _predict_ the ==residuals== using all the feature data.

> **Note:**
> Usually the total number of leaves in the tree is only allowed (set) between 8 and 32 in real world applications.

- 