- a technique used to prevent [[Overfitting]] by adding a complexity penalty to a model's loss function
- Uses methods like L1 (Lasso) and L2 (Ridge) Regularizations

### Reasons to use Regularization

- **Stops Overfitting:** Keeps the model from fitting too closely to random noise or outliers in your training set.
- **Improves Generalization:** Helps the model make accurate predictions on new, unseen data.
- **Controls Complexity:** Keeps feature weights small and manageable so no single data point or feature dominates.

***

### L1 Regularization

> **L1 Regularization (Lasso):** Adds the absolute values of the coefficients as a penalty. It can shrink some feature weights down to zero, which helps select only the most useful features.

### L2 Regularization

>**L2 Regularization (Ridge):** Adds the squared values of the coefficients as a penalty. It shrinks all weights evenly without driving them completely to zero, making it great for handling correlated features

### Elastic Net

>**Elastic Net:** Combines both L1 and L2 penalties. It balances feature selection and weight shrinkage, which works well for complex datasets.