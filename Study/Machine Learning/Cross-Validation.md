- a data testing method used to check how well a machine learning model works on new data.

### How it works:

- **Splitting:** The total dataset is split into ==k equal-sized pieces==, called folds.
- **Training:** The model learns from ==k-1 folds== combined.
- **Testing:** The remaining single fold is used to test the model's accuracy.
- **Repeating:** The process runs k times so every fold acts as the test set once.
- **Averaging:** Final scores from all tests are combined to give a single performance metric.

### Importance

1. Prevents [[Overfitting]].
2. Uses Data well - every single data points get a chance to be the training data
3. Fair comparison - no bias towards a particular part of the dataset.