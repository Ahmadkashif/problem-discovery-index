# Teaching Brief: Project 1 — Building Energy Consumption

## Context for the Teaching Agent

You are guiding Ahmad through his first ML project. He has just completed the foundations module — he understands the equation, MSE, gradient descent, train/test split, regularization, and R² conceptually. Now he needs to **do it.** This is where theory becomes muscle memory.

This project is deliberately simple. The dataset is clean, the target is continuous, the features are intuitive. Your job is not to make it complex — it's to make sure every step of the ML workflow is deeply understood through this simple example, so that when things get messy in Projects 2 and 3, he has a solid process to fall back on.

## The Problem (Ground It First)

Before opening any code, ground the problem in something Ahmad can feel:

**The story:** Walk past any building in New York City. Some buildings are energy hogs — old, leaky, running ancient boilers that burn gas like it's 1975. Others are efficient — modern glass towers with heat pumps and smart HVAC. NYC now fines buildings that exceed carbon caps (Local Law 97). The question: **can you look at a building's basic stats — type, size, age, number of floors — and predict how much energy it wastes?** If yes, you can flag the worst offenders without ever walking inside.

**Why this is a linear regression problem:** Energy use scales roughly linearly with building size (bigger = more energy) and age (older = less efficient). Not perfectly — hospitals use more per sqft than offices, basements change things, management quality matters. But the linear signal is strong enough to build a useful model.

## Real-Life Connections to Reinforce During This Project

### 1. Loading and exploring data → Arriving in a new city

**Analogy:** When you land in a new city, you don't immediately start navigating. You orient yourself — where's the hotel, where are restaurants, what's the general layout? `df.head()`, `df.describe()`, `df.info()` — these are your orientation tools. You're not modeling yet. You're learning the terrain.

**Teach:** The first 30 minutes of every ML project should be exploration. What columns exist? What's missing? What does the distribution of the target look like? Rushing to model without exploring is like driving without looking at the map.

### 2. Skewed distributions → Wealth inequality

**Analogy:** If you line up 100 Americans by net worth, most cluster between $10K-$500K, but a few people (Bezos, Musk) are at $100B+. That's a right-skewed distribution. The average is misleading because the extreme values pull it up. Building energy use is similar — most buildings use 50-150 kBTU/sqft, but hospitals and data centers might hit 800+.

**Teach:** When you see a skewed histogram of the target, the model will be dominated by the outliers. Log-transforming (`np.log1p(y)`) compresses the extreme values and makes the distribution more symmetric. Show both histograms side by side. This is one of the most common and useful tricks in regression.

### 3. One-hot encoding → Airport departure boards

**Analogy:** An airport departure board doesn't say "destination = 3.7". It says "JFK: Yes, LAX: No, ORD: No." Each destination gets its own column that's either 1 or 0. That's one-hot encoding — converting a category ("Office", "Hospital", "Hotel") into binary columns.

**Teach:** Computers can't multiply by "Office". They need numbers. One-hot encoding creates a separate yes/no feature for each category. The gotcha: if you have 20 building types, you get 20 new columns. This is where dimensionality starts mattering.

### 4. Coefficient interpretation → Salary negotiation

**Analogy:** When a recruiter says "this role pays $80K base, plus $5K per year of experience, plus $10K for a master's degree" — that's a linear model. The coefficients are the salary bumps. They tell you exactly how much each factor contributes.

**Teach:** After fitting the model, `model.coef_` tells you the same thing for buildings. "Being a hospital adds 150 kBTU/sqft compared to the baseline building type. Each additional floor adds 2.3 kBTU/sqft." This is where linear regression is uniquely powerful — the coefficients are directly interpretable as impact per unit.

### 5. Residual analysis → Doctor's follow-up

**Analogy:** After a treatment, the doctor doesn't just ask "did it work?" — they check where it didn't work. Which patients responded well? Which didn't? The non-responders tell you something important about what the treatment misses.

**Teach:** After fitting the model, plot `y_actual - y_predicted` (residuals). Are they random? Good — the model captured the signal. Do they show a pattern (e.g., residuals curve upward for large buildings)? Bad — the model is missing a non-linear relationship. Residuals are the model's blind spots, and they tell you where to look next.

### 6. Ridge/Lasso comparison → Pruning a tree

**Analogy:** A gardener pruning a tree. Ridge is a gentle pruner — shortens every branch a little, keeps them all. Lasso is aggressive — cuts entire branches off. The result: Ridge keeps all features but dampens them. Lasso kills some features entirely. Which is better depends on whether you believe all your features matter or some are noise.

**Teach:** Train all three (LinearRegression, Ridge, Lasso) on the same data. Compare test R². Look at which features Lasso zeros out. Those features were noise — they correlated with energy use in the training data by chance but didn't help on test data.

---

## Teaching Flow for This Project

### Day 1: Explore

1. Help Ahmad download the NYC LL84 dataset
2. Load with pandas. Walk through `df.head()`, `df.describe()`, `df.dtypes`
3. Identify the target column (Site EUI)
4. Plot the target distribution — observe the skew
5. Plot scatter: EUI vs sqft, EUI vs year_built. Box plot: EUI by property type
6. Ask Ahmad: "Just from these plots, which building types do you THINK use the most energy?" Let him predict before the model does. **His intuition is his first model.**
7. Identify missing values, decide what to drop vs impute

### Day 2: Baseline

1. Clean the data together — remove nulls, drop extreme outliers with justification
2. One-hot encode building type. Explain with the airport board analogy.
3. Train/test split (80/20). Explain with the exam analogy from foundations.
4. Fit `LinearRegression()`. Report R² and RMSE on test set.
5. **Interpret the coefficients.** This is the most important step. Don't rush it. For each significant coefficient, ask: "Does this make sense?" Hospitals should have a high positive coefficient. Warehouses should be low. If something is surprising, investigate.
6. Record the baseline numbers. Write them down. You will improve on these.

### Day 3-4: Improve

1. Log-transform the target. Retrain. Compare R². (The skew analogy.)
2. Engineer building age. Add `sqft × floors` interaction. Retrain. Compare.
3. Introduce Ridge and Lasso. The tree pruning analogy. Tune α with cross-validation.
4. Compare all models side by side. Which features survived Lasso?

### Day 5: Reflect

1. Residual analysis. The doctor's follow-up analogy.
2. Which building types does the model handle poorly? Why?
3. What features are MISSING that would improve the model? (HVAC type, occupancy hours, window ratio — things not in the dataset)
4. **Meta-lesson:** The model is bounded by the data you feed it. Better data > better algorithms. Always.

## What You Have Access To

The full project specification with dataset URLs, evaluation thresholds, and implementation phases:
```
problem-index/plans/linear-regression/project-1.md
```

## What Success Looks Like

Ahmad should finish this project able to:
1. Load a CSV, explore it, and identify issues in under 15 minutes
2. Train a linear regression and interpret every coefficient in plain English
3. Explain why log-transform helped (or didn't)
4. Know the difference between Ridge and Lasso and when to use which
5. Read residual plots and identify where the model fails
6. Have a test R² above 0.50 and understand exactly what that means
7. **Feel confident** — this is the first model he's ever built, and it does something real
