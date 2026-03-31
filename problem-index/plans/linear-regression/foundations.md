# Foundations — Linear Regression

## What Linear Regression Does

You have data. Each row is an observation (a building, a restaurant, a county). Each column is a feature (square footage, year built, number of floors). One column is special — it's what you want to predict. That's the **target**.

Linear regression finds the best straight-line relationship between the features and the target. "Best" means the line that makes the smallest errors across all your data.

---

## The Equation

```
ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

| Symbol | Name | What it means |
|--------|------|--------------|
| `ŷ` | y-hat | The model's prediction (e.g., predicted energy use) |
| `x₁, x₂, ... xₙ` | Features | The input values for one observation (e.g., sqft=50000, floors=3, year_built=1985) |
| `w₁, w₂, ... wₙ` | Weights (coefficients) | How much each feature matters. A weight of 0.5 on sqft means "for every 1 sqft increase, the prediction goes up by 0.5 units." These are what the model LEARNS. |
| `b` | Bias (intercept) | The prediction when all features are zero. A starting point. |
| `n` | Number of features | How many input columns you have |

With one feature, this is `y = mx + b` — a line. You learned this in school. With multiple features, it's a hyperplane (a flat surface in higher dimensions), but the idea is identical.

---

## How the Model Learns: The Loss Function

The model starts with random weights. It makes predictions. Those predictions are wrong. How wrong? We measure with a **loss function**.

### Mean Squared Error (MSE)

```
MSE = (1/m) × Σᵢ (yᵢ - ŷᵢ)²
```

| Symbol | Meaning |
|--------|---------|
| `m` | Number of observations (rows in your data) |
| `yᵢ` | The actual value for observation i (the truth) |
| `ŷᵢ` | The predicted value for observation i (your model's guess) |
| `(yᵢ - ŷᵢ)` | The error (residual) for one observation |
| `(yᵢ - ŷᵢ)²` | Squared error — squaring makes all errors positive and penalizes large errors more |
| `Σᵢ` | Sum over all observations |

**In English:** For every data point, calculate how far off the prediction is. Square it (so negatives become positive and big misses get amplified). Average all the squared errors. That's your loss.

The model's job: find the weights `w₁, w₂, ... wₙ` and bias `b` that make MSE as small as possible.

### Mean Absolute Error (MAE)

```
MAE = (1/m) × Σᵢ |yᵢ - ŷᵢ|
```

Same idea, but instead of squaring, you take the absolute value. MAE is more interpretable: "on average, the prediction is off by X units." MSE is more mathematically convenient (smooth, differentiable everywhere). You'll use both.

---

## How the Model Finds the Best Weights

### Method 1: The Normal Equation (Closed-Form Solution)

For linear regression specifically, there's a formula that gives you the exact best weights in one step:

```
w = (XᵀX)⁻¹Xᵀy
```

| Symbol | Meaning |
|--------|---------|
| `X` | The feature matrix — all your data arranged as rows (observations) × columns (features) |
| `Xᵀ` | X transposed — rows become columns and vice versa |
| `(XᵀX)⁻¹` | The inverse of (Xᵀ times X) — a matrix operation |
| `y` | The vector of all target values |
| `w` | The vector of optimal weights |

You don't need to understand matrix algebra to use this. Scikit-learn does it for you. But know that this exists — it's why linear regression is fast.

**When it breaks:** if features are perfectly correlated (multicollinearity), `XᵀX` can't be inverted. This is when regularization helps (see below).

### Method 2: Gradient Descent (The General Method)

Gradient descent works for linear regression AND every other model (neural networks, deep learning). It's the universal optimization algorithm.

**Intuition:** Imagine you're standing on a hilly landscape in fog. You can't see the bottom of the valley. But you can feel which way the ground slopes under your feet. You take a step downhill. Feel the slope again. Step again. Eventually you reach the bottom.

**The update rule:**

```
wⱼ ← wⱼ - α × (∂MSE/∂wⱼ)
```

| Symbol | Meaning |
|--------|---------|
| `wⱼ` | The weight for feature j |
| `←` | "gets updated to" |
| `α` | Learning rate — how big each step is. Too big = overshoot. Too small = takes forever. Typical: 0.01, 0.001 |
| `∂MSE/∂wⱼ` | Partial derivative of MSE with respect to wⱼ — "how much does the loss change if I nudge this weight slightly?" This is the slope. |

**The partial derivative for linear regression is:**

```
∂MSE/∂wⱼ = (2/m) × Σᵢ (ŷᵢ - yᵢ) × xᵢⱼ
```

**In English:** For each data point, multiply the error by the feature value. Average across all points. That tells you which direction to move the weight and by how much.

You repeat this for every weight, hundreds or thousands of times, and the loss shrinks. That's training.

---

## Train/Test Split: Why You Can't Grade Your Own Homework

If you train a model on all your data and then evaluate it on the same data, you're cheating. The model might have memorized the data rather than learned the pattern.

**Solution:** Split your data before training:
- **Training set (70-80%):** The model learns from this
- **Test set (20-30%):** You evaluate on this. The model has never seen these rows.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

If the model performs well on training data but poorly on test data → **overfitting** (memorized, didn't learn).
If the model performs poorly on both → **underfitting** (too simple to capture the pattern).

---

## Evaluation Metrics

### R² (R-Squared, Coefficient of Determination)

```
R² = 1 - (Σᵢ (yᵢ - ŷᵢ)²) / (Σᵢ (yᵢ - ȳ)²)
```

| Symbol | Meaning |
|--------|---------|
| `ȳ` | The mean (average) of all actual target values |
| Numerator | Sum of squared errors of your model |
| Denominator | Sum of squared errors of a "dumb" model that always predicts the mean |

**In English:** R² measures how much better your model is than just guessing the average every time.
- R² = 1.0: perfect predictions
- R² = 0.0: your model is no better than guessing the average
- R² < 0: your model is worse than guessing the average (something is very wrong)
- R² = 0.7: your model explains 70% of the variance in the target

### RMSE (Root Mean Squared Error)

```
RMSE = √MSE = √((1/m) × Σᵢ (yᵢ - ŷᵢ)²)
```

RMSE is in the same units as your target. If you're predicting energy in kBTU/sqft, RMSE is in kBTU/sqft. "On average, the prediction is off by about RMSE units" (roughly — it's actually a bit more nuanced because squaring penalizes large errors).

---

## Feature Engineering: Where 80% of ML Happens

Raw data is rarely the best input. Transforming features often matters more than the model you choose.

**Common transforms for linear regression:**
- **Log transform:** If your target is skewed (many small values, few huge ones), predicting `log(y)` instead of `y` helps. Energy use, dollar amounts, and fire sizes are often log-normal.
- **Interaction terms:** `sqft × floors` captures something neither feature captures alone (a 10-story building at 50K sqft is very different from a 1-story building at 50K sqft).
- **Polynomial features:** `sqft²` captures non-linear relationships. A building twice as big doesn't always use twice the energy.
- **One-hot encoding:** Convert categorical features (building_type = "office" / "retail" / "hospital") into binary columns (is_office=1, is_retail=0, is_hospital=0).
- **Temporal features:** From a date, extract year, month, day_of_week, season. From a sequence, compute rolling averages and rates of change.

---

## Regularization: Taming Overconfident Models

When you have many features, linear regression can overfit — assigning large weights to features that happen to correlate with the target in the training data but not in reality.

### Ridge Regression (L2 Regularization)

```
Loss = MSE + λ × Σⱼ wⱼ²
```

| Symbol | Meaning |
|--------|---------|
| `λ` | Regularization strength (hyperparameter you choose). Higher = more penalty on large weights |
| `Σⱼ wⱼ²` | Sum of squared weights — penalizes large weights |

**In English:** "Minimize the error, but also keep the weights small." This prevents any single feature from dominating the model.

### Lasso Regression (L1 Regularization)

```
Loss = MSE + λ × Σⱼ |wⱼ|
```

Same idea, but uses absolute value instead of squares. The magical property: Lasso can push weights to **exactly zero**, effectively removing features. This is automatic feature selection.

### When to Use Which

- **Many features, most probably relevant:** Ridge (shrinks all weights, keeps everything)
- **Many features, some probably irrelevant:** Lasso (zeros out the noise)
- **Not sure:** Try both. Or use ElasticNet (combines Ridge + Lasso)

---

## The Full Workflow (What You'll Do in Every Project)

```
1. Load data (pandas)
2. Explore: distributions, correlations, missing values (matplotlib, seaborn)
3. Clean: handle missing values, remove outliers if justified
4. Engineer features: transforms, interactions, encodings
5. Split: train/test (sklearn.model_selection)
6. Train: fit model on training data (sklearn.linear_model)
7. Evaluate: RMSE, R², MAE on test data (sklearn.metrics)
8. Interpret: examine coefficients — which features matter?
9. Iterate: add features, try regularization, compare
```

---

## What Comes After

Linear regression assumes a straight-line relationship. Reality is messier. After mastering this:
- **Logistic Regression:** Same framework, but for yes/no predictions (classification)
- **Gradient Boosting:** Ensembles of decision trees that capture non-linear patterns
- **Neural Networks:** Stacked layers of "neurons" — each one is basically a linear regression + a non-linear activation function

Every one of these builds directly on what you learn here. The loss function, gradient descent, train/test split, evaluation metrics, regularization — all of it carries forward.
