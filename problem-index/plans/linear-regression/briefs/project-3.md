# Teaching Brief: Project 3 — Crop Yield Prediction

## Context for the Teaching Agent

Ahmad has completed Projects 1 and 2. He can build regression and classification models, engineer temporal features, handle data leakage, interpret coefficients, and evaluate models. He has built two working ML systems.

This project is the capstone. It introduces the hardest and most important lesson in applied ML: **the model is only as good as the features you engineer, and the features are only as good as your understanding of the domain.** Linear regression with smart features will match or beat a complex model with dumb features. This is the lesson that separates ML practitioners from ML tourists.

This project also introduces multi-source data integration — downloading from three separate government sources, cleaning each, joining them by geography and time. This is what real data science looks like: 80% plumbing, 20% modeling.

## The Problem (Ground It First)

**The story:** Every fall, corn gets harvested across the American Midwest. Before a single combine enters the field, commodity traders bet billions on how big the harvest will be. Governments stockpile grain or release reserves based on yield forecasts. A bad forecast can spike food prices globally.

The USDA employs thousands of field agents who walk into actual cornfields, count ears of corn, weigh samples, and estimate yields county by county. This is expensive and slow. But the signals are in the data: if July was scorching hot and August was bone-dry, yields will drop. If a satellite photograph shows brown fields instead of green, the crop is struggling.

**The punchline Ahmad needs to discover:** You can predict corn yield surprisingly well from just two things — how hot was the growing season and how much did it rain. Add a satellite photo of how green the fields are in late July, and you've captured most of the signal. Linear regression on these engineered features gets you 60-75% of the way. Gradient boosting adds 5-15% more. **The features did the work, not the algorithm.**

## Real-Life Connections to Reinforce During This Project

### 1. Multi-source data integration → Assembling IKEA furniture with parts from different boxes

**Analogy:** Imagine you bought a desk, but the tabletop came from one shipment, the legs from another, and the screws from a third. Each has its own packaging, its own instruction sheet, its own part numbering. Before you can build anything, you need to figure out which tabletop goes with which legs, match the screw sizes, and deal with the fact that one shipment measures in inches and the other in centimeters.

**Teach:** USDA yield data uses FIPS county codes. NOAA weather data uses state + county name (sometimes formatted differently). Satellite data uses latitude/longitude grids. Before a single model is trained, you spend days just getting these three datasets to talk to each other. Joining on FIPS code is the equivalent of matching the screw sizes. This is not glamorous. It IS the job.

### 2. Growing Degree Days → Your phone's step counter

**Analogy:** Your phone doesn't track how fast you walked — it counts cumulative steps. 10,000 steps in a day, regardless of whether you ran them in an hour or strolled all day. Growing Degree Days (GDD) is the same concept for crops: cumulative heat above a baseline temperature (10°C for corn) over the growing season. A corn plant doesn't care if it was 25°C today — it cares about the total accumulated heat since planting. Every day above 10°C is a "step" toward maturity.

**Teach:** GDD = `max(0, (T_max + T_min)/2 - 10)` accumulated daily from April to September. This is the single most predictive feature for corn yield. It captures the fundamental biology: corn needs ~2,500 GDD to reach maturity. Show Ahmad how to compute it from monthly temperature data (approximation: `monthly_GDD ≈ max(0, avg_temp - 10) × days_in_month`).

### 3. The quadratic relationship → The Goldilocks zone

**Analogy:** Water for a houseplant. Too little — the plant wilts. Too much — the roots rot. There's a sweet spot. The relationship isn't linear (more water = better). It's curved — it goes up, hits a peak, and comes back down. Precipitation and crop yield have the same shape: too little rain = drought, too much = flooding and disease. The optimal amount depends on the crop and region.

**Teach:** If you only include `precipitation` as a feature, linear regression assumes more rain = linearly more/less yield. Adding `precipitation²` lets the model learn the curve — yield increases with rain up to a point, then decreases. This is the simplest form of capturing non-linearity in a linear model. Show both the scatter plot (curved relationship) and the improvement in R² when the quadratic term is added.

### 4. Interaction terms → Combo punches in boxing

**Analogy:** A jab alone — annoying but manageable. A hook alone — hurts but survivable. A jab-hook combo — devastating. The combination is worse than the sum of its parts. In crop yield, heat alone reduces yield a bit. Drought alone reduces yield a bit. Heat AND drought together — catastrophic. The 2012 Midwest drought + heatwave destroyed yields 25-30% below trend. Neither temperature nor precipitation alone captured the severity.

**Teach:** The interaction term `temperature × precipitation` (or more precisely, `heat_stress × drought_severity`) captures these combo effects. When Ahmad adds this feature and sees R² jump, the lesson lands: **domain knowledge creates features that capture real-world phenomena the model can't discover on its own from raw numbers.**

### 5. Leave-one-year-out cross-validation → Exam prep across semesters

**Analogy:** You took 5 semesters of exams. To predict how you'll do on the 6th semester exam, you could train on all 5 past semesters. But a better test: train on semesters 1-4, test on semester 5. Then train on semesters 1-3 and 5, test on 4. And so on. Each semester gets a turn as the "exam." This is leave-one-out cross-validation.

**Teach:** For crop yield, years are not interchangeable with random rows. 2012 was a drought year — all counties suffered. Randomly mixing 2012 rows into training and test sets leaks the drought signal. Leave-one-year-out ensures the model is tested on entire years it's never seen. This is the correct way to evaluate a model with temporal structure.

### 6. Feature importance → Ranking causes of a plane crash

**Analogy:** After a plane crash, investigators rank the contributing factors: 1) engine failure, 2) pilot fatigue, 3) bad weather, 4) maintenance oversight. They don't just say "many things went wrong." They quantify the contribution of each factor so that the most impactful one gets the most attention in the fix.

**Teach:** After fitting the model, standardize the coefficients (multiply each by the feature's standard deviation) so they're on the same scale. Now rank them. GDD should be near the top. Heat stress days should be up there. Year (capturing genetic improvement trend) should be significant. The student should be able to look at this ranking and say "this makes sense" — or "this is surprising, let me investigate."

### 7. Features > Algorithms → The chef vs. the oven

**Analogy:** A great chef with a basic oven will outcook a terrible chef with a $50,000 commercial oven every time. The oven (algorithm) matters, but the chef (feature engineering) is where the magic happens. Gordon Ramsay with a campfire beats a culinary student with a sous vide.

**Teach:** This is the capstone lesson. After Ahmad builds his best linear regression with domain-engineered features (GDD, heat stress, precip², interaction terms, lagged yield), have him build a gradient boosting model (XGBoost or LightGBM) on the SAME features and on RAW features separately.

Show three results:
1. Linear regression + engineered features: R² ≈ 0.65-0.75
2. Gradient boosting + raw features: R² ≈ 0.55-0.65
3. Gradient boosting + engineered features: R² ≈ 0.70-0.80

The gap between (1) and (2) proves the point: **a simple model with great features beats a complex model with bad features.** The gap between (1) and (3) shows what you gain from model complexity — it's real but smaller than what you gain from features.

### 8. NDVI from satellites → Taking the crop's temperature from space

**Analogy:** A doctor doesn't need to talk to you to know you're sick. They can see it — pale face, droopy eyes, sweaty forehead. A satellite does the same for crops. It doesn't measure yield directly — it measures "greenness" (NDVI). Green = healthy, photosynthesizing, growing. Brown/yellow = stressed, drought-hit, dying. A satellite photo of a cornfield in late July is like a doctor's visual assessment — it tells you a LOT without touching the patient.

**Teach:** NDVI = (NIR - Red) / (NIR + Red). Plants reflect near-infrared light (NIR) strongly when healthy. A high NDVI in late July means the crop is in good shape; yield will be near-trend or above. A low NDVI means trouble. This feature, if Ahmad gets it (via Google Earth Engine or a pre-computed dataset), should be the strongest single predictor — stronger than any weather variable — because it's a direct observation of crop status, not an indirect proxy.

---

## Teaching Flow for This Project

### Days 1-3: Data Assembly (The Hard Part)

1. Download USDA yield data from Quick Stats. Walk through the filters together.
2. Download NOAA county-level climate data. Walk through the format.
3. **The join.** Match by FIPS county code + year. Handle mismatches, missing counties, naming inconsistencies. The IKEA analogy.
4. Explore: yield trends by state, year-to-year volatility, the 2012 drought visible in the data.
5. Explore: weather-yield scatter plots. See the non-linear precipitation relationship. See the heat stress effect.

### Days 4-5: Feature Engineering (The Creative Part)

1. Compute GDD. The step counter analogy. Show the correlation with yield.
2. Compute heat stress days. Show the damage above 35°C threshold.
3. Add precipitation². The Goldilocks analogy. Show the improved fit.
4. Add GDD × precipitation interaction. The combo punch analogy.
5. Add yield_lag1 (previous year's yield for same county). Add 5-year rolling average.
6. Add year as a feature (captures genetic improvement trend of ~2 bu/acre/year).

### Days 6-8: Model and Compare

1. Leave-one-year-out cross-validation. The semester exam analogy.
2. Fit linear regression with all engineered features. Report R² and RMSE.
3. Feature importance ranking. The plane crash analogy. Does it match agronomic knowledge?
4. **The capstone comparison:** Fit XGBoost on raw features and on engineered features. Show all three R² values. The chef vs oven analogy. Let the numbers speak.
5. Residual analysis: which years/states does the model miss? (Extreme events like 2012 drought)
6. Optional: add NDVI if Ahmad has Google Earth Engine access. See the R² jump.

### Days 9-10: Reflect

1. What did this project teach that Projects 1 and 2 didn't?
2. The meta-lesson: **domain knowledge is an ML superpower.** A PhD agronomist who can code will beat an ML PhD who doesn't know crops. In every industry, the same is true.
3. Preview the future: "You just used linear regression on tabular features. But that satellite image you used for NDVI? A CNN could look at the raw image and learn features you didn't think to engineer. That's where computer vision starts."
4. Preview time-series: "You used monthly averages. But crops grow day by day. An LSTM could process the daily weather sequence directly. That's where deep learning starts."

## What You Have Access To

The full project specification with dataset URLs and implementation phases:
```
problem-index/plans/linear-regression/project-3.md
```

## What Success Looks Like

Ahmad should finish this project able to:
1. Download, clean, and join data from multiple government sources
2. Engineer domain-specific features that encode real-world knowledge (GDD, heat stress, quadratic precipitation)
3. Use leave-one-year-out cross-validation for temporal data
4. Interpret standardized coefficients as feature importance
5. Prove to himself that features > algorithms by comparing LR + smart features vs XGBoost + raw features
6. Understand that every domain has its own "GDD equivalent" — tacit knowledge waiting to be encoded as features
7. See the path from here to deep learning: "What if the model could learn the features itself from raw data?" That's what neural networks do. That's what comes next.
