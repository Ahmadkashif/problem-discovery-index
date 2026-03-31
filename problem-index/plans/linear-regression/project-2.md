# Project 2: Restaurant Health Inspection Failure Prediction

**Difficulty:** Intermediate
**Domain:** Public Health / Food Safety
**Source Problem:** Cities inspect restaurants for health code violations. Some restaurants fail repeatedly. Others maintain perfect records. Can you predict which restaurants will fail their next inspection — and get there before someone gets sick?

---

## The Problem

Chicago and NYC publish every restaurant health inspection result. You have 10+ years of inspections: which restaurant, when, what violations, what result. The City of Chicago actually built and deployed a machine learning model to prioritize inspections — and published the code on GitHub. You're going to replicate and improve on a real government ML system.

The intermediate challenge: the raw data is a log of inspections over time. You need to **engineer temporal features** — "how many times has this restaurant failed before?", "how long since the last inspection?", "is the violation trend getting better or worse?" This is where real ML engineering starts.

---

## Dataset

**Primary:** Chicago Food Inspections
- **URL:** https://data.cityofchicago.org/Health/Food-Inspections/4ijn-s7e5
- **Direct CSV:** https://data.cityofchicago.org/api/views/4ijn-s7e5/rows.csv?accessType=DOWNLOAD
- **Kaggle mirror:** https://www.kaggle.com/datasets/chicago/chicago-food-inspections
- **Size:** 250,000+ inspection records, January 2010 to present
- **Key columns:** DBA Name, License # (links same restaurant across inspections), Facility Type, Risk (1=High/2/3=Low), Address, Zip, Inspection Date, Inspection Type (Canvass, Complaint, Re-inspection, License), **Results** (Pass / Pass w/ Conditions / Fail / No Entry / Out of Business), **Violations** (free text with codes 1-44+ and inspector comments), Latitude, Longitude

**Secondary:** NYC DOHMH Restaurant Inspection Results
- **URL:** https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j
- **Size:** ~400,000 rows, 87 cuisine types
- **Key advantage:** NYC has a **numeric score** (continuous target for regression). Grading: A = 0-13 points, B = 14-27, C = 28+. Each violation type has a defined point value.

**Reference implementation:** City of Chicago's deployed model
- **GitHub:** https://github.com/Chicago/food-inspections-evaluation
- **Model:** Elastic net (regularized linear regression) — exactly what you're learning
- **Result:** Found critical violations significantly faster than default inspection scheduling

---

## ML Task

**Two framings (do both):**

1. **Regression (NYC):** Predict inspection **score** (continuous integer, 0-100+) from restaurant features and history. This is pure linear regression.

2. **Classification (Chicago):** Predict **pass vs fail** (binary) from restaurant features and history. This is logistic regression — the natural next step from Project 1.

**Input features (engineered from raw inspection history):**
- Number of prior inspections for this restaurant
- Number of prior failures
- Failure rate (failures / total inspections)
- Days since last inspection
- Result of most recent inspection
- Number of critical violations in last inspection
- Trend: is the violation count increasing or decreasing over last 3 inspections?
- Risk category (1/2/3)
- Facility type (Restaurant, Bakery, Grocery, etc.)
- Zip code / neighborhood
- Cuisine type (NYC only)
- Season / month of inspection
- Chain indicator: does this DBA Name appear at multiple addresses? (chains may have better/worse compliance than independents)

---

## Evaluation Criteria

### For regression (NYC score):

| Level | R² | RMSE (points) | What it means |
|-------|-----|---------------|--------------|
| Beginner | > 0.15 | < 18 | Beating the average — history matters |
| Good | > 0.30 | < 14 | Prior violations and restaurant type captured |
| Excellent | > 0.45 | < 11 | Strong temporal features, regularization tuned |

### For classification (Chicago pass/fail):

| Level | AUC-ROC | Precision@100 | What it means |
|-------|---------|--------------|--------------|
| Beginner | > 0.60 | > 30% | Better than random |
| Good | > 0.70 | > 45% | Competitive with Chicago's deployed model |
| Excellent | > 0.75 | > 55% | You've built a real inspection prioritization tool |

**Domain metric:** Precision@K — "If we inspect the top 100 restaurants the model flags as high-risk first, how many actually have critical violations?" This is what matters operationally.

---

## Implementation — 4 Phases

### Phase 1: Exploration (Days 1-2)

1. Download Chicago data. Load with pandas.
2. **Understand the structure:** Each row is one inspection. Same restaurant appears multiple times (linked by License #). Sort by License # and Inspection Date to see a restaurant's history.
3. **Explore Results distribution:** What % pass vs fail? (Class balance matters for classification)
4. **Parse Violations:** The Violations column is a pipe-delimited mess of codes and comments. Count violations per inspection. Identify critical vs non-critical violations.
5. **Time patterns:** Do failure rates vary by month? By year? By day of week?
6. **Geography:** Map failure rates by zip code. Any neighborhoods with systemic issues?
7. **Key question:** Can you predict the *next* inspection result from a restaurant's *history*? This requires restructuring the data.

### Phase 2: Baseline (Days 3-4)

1. **Restructure the data:** This is the hard part.
   - For each inspection, compute features from ALL PRIOR inspections of the same restaurant
   - This means: group by License #, sort by date, and for each row, look backward
   - Features to compute: `num_prior_inspections`, `num_prior_failures`, `failure_rate`, `days_since_last_inspection`, `last_result`, `violations_in_last_inspection`
   - **Important:** Never use future information. Each row's features can only use data from BEFORE that inspection date. This is called preventing **data leakage**.
2. **Handle cold starts:** Restaurants with zero prior inspections have no history features. Fill with reasonable defaults or flag them.
3. **Split:** Time-based split (not random!) — train on inspections before 2022, test on 2022+. This simulates real deployment where you predict the future from the past.
4. **Baseline linear regression:**
   ```python
   # Binary target for Chicago
   df['failed'] = (df['Results'] == 'Fail').astype(int)
   ```
   Train a logistic regression. Report AUC-ROC.
5. Compare to "always predict the majority class" baseline. How much better is your model?

### Phase 3: Primary Model (Days 5-6)

1. **Richer temporal features:**
   - Violation count trend: slope of violation counts over last 3 inspections
   - Time-weighted failure rate: recent failures count more than old ones
   - Inspection type effects: complaint-driven inspections have higher fail rates than routine canvasses
2. **Regularization:**
   - Try Ridge and Lasso logistic regression (`sklearn.linear_model.LogisticRegression(penalty='l1', solver='saga')`)
   - Which features does Lasso zero out? These are noise.
3. **NYC regression variant:**
   - Download NYC data. Predict numeric score with linear regression.
   - Compare: is the regression R² higher than the classification AUC? (Different framing of a similar problem)
4. **Benchmark against Chicago's model:**
   - Their model used elastic net. Compare your AUC-ROC to theirs.
   - Read their GitHub code — what features did they use that you didn't?

### Phase 4: Iteration (Day 7)

1. **Error analysis:** Which restaurants does the model get wrong?
   - False negatives (predicted pass, actually failed): These are the dangerous ones — what features are they missing?
   - False positives (predicted fail, actually passed): Are these restaurants that cleaned up since their last bad inspection?
2. **Threshold tuning:** Logistic regression outputs probabilities. At what threshold do you flag a restaurant? 50%? 30%? Lower threshold = more restaurants flagged (higher recall, lower precision). What's the right tradeoff for public health?
3. **Fairness check:** Do certain cuisines or zip codes get flagged disproportionately? Is that because they actually fail more, or because inspectors target them more?
4. **Stretch: NLP on violation text.** The Violations column has free-text inspector comments. Can you extract features from the text (e.g., presence of words like "rodent", "temperature") to improve prediction? This is a preview of NLP — your future specialization.

---

## What You Learn from This Project

| Concept | How it shows up |
|---------|----------------|
| Temporal feature engineering | Computing features from a restaurant's inspection history |
| Data leakage prevention | Never using future inspections to predict past ones |
| Time-based train/test split | Training on 2010-2021, testing on 2022+ |
| Logistic regression | Binary classification (pass/fail) as an extension of linear regression |
| Probability thresholds | Choosing cutoff for flagging high-risk restaurants |
| Precision@K | "Of the top 100 flagged, how many actually failed?" |
| Class imbalance | More passes than failures — affects model training |
| Benchmarking against production | Comparing your model to Chicago's deployed system |
| Fairness and bias | Checking if the model treats all neighborhoods/cuisines equitably |
| Real-world impact framing | This model saves people from foodborne illness |
