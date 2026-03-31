# Teaching Brief: Project 2 — Restaurant Health Inspection Failure

## Context for the Teaching Agent

Ahmad has completed Project 1 (Building Energy). He can load data, train a regression, interpret coefficients, use regularization, and read residual plots. Now you raise the stakes.

This project introduces two new dimensions of complexity:
1. **Temporal feature engineering** — the raw data is a log of events over time. Features don't exist in the data; they must be *constructed* from history.
2. **The shift from regression to classification** — predicting pass/fail (binary) instead of a continuous number. This is where logistic regression enters.

This is also the project where Ahmad learns that the data he downloads is NOT the data he models on. The modeling dataset must be built. This is the real work of ML engineering.

## The Problem (Ground It First)

**The story:** You eat at restaurants. Every restaurant in Chicago and NYC gets inspected by a health inspector — surprise visit, checklist of violations, pass or fail. Some restaurants are serial offenders. Rodents, improper food temperatures, no handwashing stations. Others are spotless.

Here's the twist: the City of Chicago asked themselves — "Can we predict which restaurants will fail BEFORE we inspect them, so we send inspectors to the worst places first?" They built a machine learning model, tested it in a double-blind study, and found it identified critical violations significantly faster than the default scheduling. **Then they published the code on GitHub.**

Ahmad is replicating a model that a major US city actually deployed to protect public health.

## Real-Life Connections to Reinforce During This Project

### 1. Temporal feature engineering → A judge sentencing a repeat offender

**Analogy:** When a judge considers sentencing, they look at the defendant's history: first offense or fifth? How long since the last offense? Is the severity escalating? They don't just look at the current crime — they reconstruct a narrative from the timeline.

**Teach:** Each row in the Chicago data is one inspection. But a restaurant with 3 prior failures in 2 years is very different from one with zero prior inspections. Those features — `num_prior_failures`, `failure_rate`, `days_since_last_inspection`, `violation_trend` — don't exist in the raw data. You compute them by looking backward through each restaurant's history. This is temporal feature engineering, and it's one of the most valuable ML skills.

### 2. Data leakage → Time travel cheating

**Analogy:** Imagine a stock trader who "backtests" their strategy but accidentally includes information from the future — like using tomorrow's closing price to decide today's trade. Of course it works perfectly. But it's cheating. In ML, this is called data leakage.

**Teach:** When computing features for an inspection on June 15, 2021, you can ONLY use data from BEFORE June 15, 2021. If you accidentally include the result of the June 15 inspection itself, or future inspections, your model will seem amazing but will fail completely in production. This is the #1 mistake in temporal ML. Walk through exactly how to prevent it with `groupby + shift` in pandas.

**Make it visceral:** Show what happens when you intentionally leak. R² jumps to 0.95. Then remove the leak. R² drops to 0.30. The difference is the difference between a useless model and an honest one.

### 3. Time-based train/test split → The stock market backtester

**Analogy:** You wouldn't test a trading strategy by randomly picking days from the past — you'd train on 2015-2020 and test on 2021. Because in real life, you only ever predict the future from the past. Randomly shuffling time-series data into train/test leaks temporal patterns.

**Teach:** Don't use `train_test_split(random_state=42)` for this project. Split by date: train on inspections before 2022, test on 2022+. This simulates the real deployment scenario — "given everything we know up to today, predict what happens tomorrow."

### 4. The shift from regression to classification → Temperature vs. fever

**Analogy:** A thermometer gives you a continuous number: 98.6°F, 100.2°F, 103.4°F. That's regression — predicting a number. But when you call the doctor, they don't care about the exact temperature. They ask: "Does the patient have a fever? Yes or no." That's classification — converting a continuous signal into a discrete decision.

**Teach:** NYC has a continuous inspection score (0-100+) — pure regression. Chicago has pass/fail — binary classification. Logistic regression handles the binary case by outputting a probability (0-1) and then applying a threshold. "If the model says 73% chance of failure, do we send an inspector?" This threshold is a decision you make, not one the model makes.

### 5. Logistic regression → Dimmer switch vs. light switch

**Analogy:** Linear regression is a dimmer switch — it outputs any value on a continuous range. But for pass/fail, you need a light switch — on or off. The sigmoid function is what converts the dimmer (any number from -∞ to +∞) into a probability (0 to 1). Then you choose the threshold that flips the switch.

**Teach:** Show the sigmoid curve. `σ(z) = 1 / (1 + e^(-z))`. Show how it squashes any input to 0-1. The "z" is exactly the same linear equation as before: `z = w₁x₁ + w₂x₂ + ... + b`. Logistic regression IS linear regression → passed through a squashing function → interpreted as probability.

### 6. Precision vs. Recall → Airport security vs. nightclub bouncer

**Analogy:** Airport security optimizes for **recall** — catch every possible threat, even if it means hassling 100 innocent travelers. The cost of a false negative (missed threat) is catastrophic. A nightclub bouncer optimizes for **precision** — only let in people who actually belong, even if you turn away some VIPs. The cost of a false positive (letting in a troublemaker) is high.

**Teach:** For restaurant inspections, which matters more? Missing a restaurant that should have failed (false negative = someone gets food poisoning) vs. sending an inspector to a restaurant that passes (false positive = wasted inspector time). Public health says: optimize for recall. Catch every dangerous restaurant, even if you over-inspect some clean ones. This is why threshold tuning matters — lowering the threshold from 50% to 30% catches more true failures at the cost of more false alarms.

### 7. Precision@K → Hiring the top candidates

**Analogy:** A recruiter has 500 applicants and 10 interview slots. They rank everyone and interview the top 10. Precision@10 = "of the 10 people I interviewed, how many were actually good hires?" That's the metric that matters — not overall accuracy across all 500.

**Teach:** The city has limited inspectors. If the model ranks 250 restaurants as high-risk and they can only inspect 100 this week, Precision@100 is the metric: "of the 100 we inspected first, how many actually had critical violations?" This is how the City of Chicago evaluated their model.

### 8. Fairness → Redlining

**Analogy:** Banks used to draw red lines around neighborhoods (predominantly Black neighborhoods) and refuse to lend there. The "model" was accurate in a narrow statistical sense — default rates were higher in those areas. But the model was also the CAUSE of the problem (no loans → no investment → declining property values → more defaults). The model reinforced the very inequality it measured.

**Teach:** If your restaurant model flags certain cuisines or neighborhoods disproportionately, ask: is that because those restaurants are genuinely more likely to fail, or because inspectors already target them more (creating more failure data)? The model learns from historical inspection data — which reflects historical inspection BIASES. This is a real concern, not a hypothetical.

---

## Teaching Flow for This Project

### Days 1-2: Explore and Restructure

1. Download Chicago data. Explore. Understand that each row = one inspection, not one restaurant.
2. **The restructuring exercise:** This is the hardest part. Walk Ahmad through:
   - Group by `License #` (restaurant ID)
   - Sort by `Inspection Date` within each group
   - For each inspection, compute features from ALL PRIOR inspections only
   - `num_prior_inspections`, `num_prior_failures`, `failure_rate`, `days_since_last_inspection`, `last_result`, `avg_violations_last_3`
3. Talk through data leakage. Show the time travel analogy. Make him implement the backward-looking computation correctly.
4. Parse the `Violations` column — count total violations, count critical vs non-critical

### Days 3-4: Baseline and Classification

1. Time-based split: train pre-2022, test 2022+
2. Train logistic regression on pass/fail. Report AUC-ROC.
3. **The sigmoid lesson.** Show the probability outputs. Pick 5 restaurants and discuss: "This one has 82% failure probability. This one has 23%. What should the threshold be?"
4. Draw the precision-recall tradeoff curve. The airport security vs bouncer analogy.
5. Compute Precision@100: "If we inspect our top-100 flagged restaurants first, how many actually fail?"

### Days 5-6: Improve and Benchmark

1. Richer temporal features: violation trend slope, time-weighted failure rate
2. Regularized logistic regression (L1/L2). Which features survive Lasso?
3. **Download Chicago's open-source model from GitHub.** Compare your features and performance to theirs. What did they think of that you didn't?
4. Optional: try NYC data with the numeric score as a regression target. Does regression or classification work better?

### Day 7: Reflect and Stretch

1. Error analysis: which restaurants does the model get wrong and why?
2. Fairness analysis: failure rates by cuisine type, by zip code. The redlining analogy.
3. Stretch preview: the Violations column has free text. Mention that NLP could extract features from inspector comments ("rodent droppings", "improper temperature"). This is a preview of Ahmad's NLP future.

## What You Have Access To

The full project specification:
```
problem-index/plans/linear-regression/project-2.md
```

The Chicago model to benchmark against:
```
https://github.com/Chicago/food-inspections-evaluation
```

## What Success Looks Like

Ahmad should finish this project able to:
1. Restructure event-log data into a modeling dataset with temporal features — without leakage
2. Explain logistic regression as "linear regression + sigmoid"
3. Choose a classification threshold and justify it with precision/recall tradeoffs
4. Compute and interpret Precision@K as an operational metric
5. Compare his model to a real deployed system and understand the gap
6. Articulate fairness concerns in ML systems that affect real people
7. Know that **data engineering (building the feature matrix) is 70% of the work** — and be OK with that
