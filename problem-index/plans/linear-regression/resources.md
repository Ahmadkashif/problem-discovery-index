# Resources — Linear Regression

## Python Libraries You'll Use

| Library | What for | Install |
|---------|----------|---------|
| **pandas** | Load CSVs, manipulate dataframes, group/filter/join | `pip install pandas` |
| **numpy** | Math operations, arrays, log transforms | `pip install numpy` |
| **matplotlib** | Basic plots (scatter, histogram, line) | `pip install matplotlib` |
| **seaborn** | Statistical plots (heatmaps, box plots, pair plots) | `pip install seaborn` |
| **scikit-learn** | LinearRegression, Ridge, Lasso, train_test_split, metrics | `pip install scikit-learn` |
| **jupyter** | Interactive notebooks | `pip install jupyterlab` |

Install everything at once:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyterlab
```

## Key scikit-learn Classes

```python
# Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.linear_model import LogisticRegression  # for Project 2

# Preprocessing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures

# Metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import roc_auc_score, f1_score  # for Project 2
```

---

## Datasets — Direct Links

### Project 1: Building Energy
- NYC LL84: https://data.cityofnewyork.us (search "Energy and Water Data Disclosure")
- UCI Energy Efficiency (starter): https://archive.ics.uci.edu/dataset/242/energy+efficiency
- Chicago Benchmarking: https://data.cityofchicago.org (search "Energy Benchmarking")
- ASHRAE Kaggle: https://www.kaggle.com/c/ashrae-energy-prediction

### Project 2: Restaurant Inspections
- Chicago: https://data.cityofchicago.org/Health/Food-Inspections/4ijn-s7e5
- NYC: https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j
- Chicago ML model (GitHub): https://github.com/Chicago/food-inspections-evaluation
- Yelp + Inspections paper: https://ar5iv.labs.arxiv.org/html/1603.05673

### Project 3: Crop Yield
- USDA NASS Quick Stats: https://quickstats.nass.usda.gov/
- NOAA Climate at a Glance: https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping
- Google Earth Engine (NDVI): https://earthengine.google.com/
- Rangeland Analysis Platform: https://rangelands.app/

---

## Learning Materials (Curated, Not Exhaustive)

### Video — Best Single Resource for Math Intuition
- **3Blue1Brown: Essence of Linear Algebra** — YouTube playlist. Watch before touching matrices. Makes linear algebra visual and intuitive. Free.

### Interactive
- **StatQuest with Josh Starmer: Linear Regression** — YouTube. Explains MSE, R², gradient descent with simple visuals. No fluff.

### Textbook (Reference, Not Required)
- **An Introduction to Statistical Learning (ISLR)** — James, Witten, Hastie, Tibshirani. Free PDF at https://www.statlearning.com/. Chapter 3 covers linear regression thoroughly. The gold standard for applied ML with minimal mathematical prerequisites.

### Hands-On
- **Kaggle Learn: Intro to Machine Learning** — Free. Browser-based exercises. Covers the basics with real datasets.

---

## The Other 12 Problems (For Future Reference)

These are the remaining problems from the shortlist of 15. You can tackle them as independent practice after completing this plan, or they'll appear in future learning plans (logistic regression, gradient boosting, time-series).

| # | Problem | Data | Best For |
|---|---------|------|----------|
| 1 | County Health Outcomes | County Health Rankings (3,100 counties) | Coefficient interpretation, public health |
| 2 | Road Accident Severity | Moosavi US Accidents (7.7M records) | Feature engineering, linear→logistic |
| 4 | Air Quality PM2.5 | Beijing PM2.5 (43K records) | Beginner regression, multi-source |
| 6 | Engine Remaining Life | NASA C-MAPSS (20K records) | Time-series bridge, feature engineering |
| 7 | Bridge Deterioration | FHWA NBI (617K bridges) | Panel data, multicollinearity |
| 8 | Flood Damage | FEMA NFIP (2.5M claims) | Log-transforms, skewed targets |
| 9 | Hospital Readmission | Diabetes 130-US (101K encounters) | Logistic regression transition |
| 10 | Workplace Injury | OSHA (1M+ records) | Social impact, penalty prediction |
| 11 | Wildfire Size | FPA-FOD (1.88M fires) | Log-transform, interaction effects |
| 12 | Business Death | Yelp Open Dataset (150K businesses) | Creative proxy signals |
| 14 | Drug Adverse Events | FDA FAERS (20M+ reports) | Messy data, pharmacovigilance |
| 15 | Gentrification | Census ACS + City permits | Ambitious multi-source, ethics |

---

## What Comes Next

After completing this plan, you'll have:
- Built 3 regression models on real data
- Mastered feature engineering, evaluation, regularization, and interpretation
- Transitioned from regression to classification (Project 2)
- Integrated multiple data sources (Project 3)

**Next plan:** `logistic-regression` — formalize classification, tackle the hospital readmission and business death problems, learn precision/recall/ROC in depth.

**Then:** `gradient-boosting` → `time-series-forecasting` → deep learning (CNNs for computer vision, transformers for NLP).
