# Machine Learning Opportunities — Med Spas

**Industry:** [[med-spas|Med Spas]]
**Derived from:** [[problems/med-spas/high-impact|High Impact]], [[problems/med-spas/low-impact-1|Low Impact 1]], [[problems/med-spas/low-impact-2|Low Impact 2]], [[problems/med-spas/worker-life-1|Worker Life 1]], [[problems/med-spas/worker-life-2|Worker Life 2]]

---

## 1. Facial Aging Assessment and Injection Mapping
#cnns #transfer-learning #feature-engineering #evaluation-metrics #loss-functions #backpropagation #gradient-descent #cross-validation #activation-functions #bias-variance-tradeoff #tacit-knowledge-ml

**Problem statement:** An experienced aesthetic injector looks at a face and reads a complex map of aging — midface volume loss in the malar fat pads, deepening nasolabial folds from descending SMAS tissue, perioral lines from orbicularis oris hyperactivity, lateral brow ptosis from frontalis fatigue, and jawline blunting from pre-jowl fat pad atrophy and masseter hypertrophy. They mentally map which areas need volume restoration (filler), which need muscle relaxation (toxin), which need skin tightening (RF/laser), and which need surface-level treatment (chemical peel/microneedling). This multi-layered assessment — combining anatomical knowledge, aging pattern recognition, and product-specific outcome prediction — takes 5-10 years of full-time injection experience to develop. New injectors see "wrinkles" and reach for Botox; experienced injectors see "volume loss creating skin folds that wrinkles follow" and reach for filler first, toxin second.

**ML task:** Multi-output regression — predict aging severity scores by facial zone AND recommend treatment modality priority by zone
**Input data:** Standardized facial photographs (front, 45-degree, profile) with controlled lighting and color calibration; patient demographics (age, sex, skin type Fitzpatrick I-VI); previous treatment history; patient-reported concerns
**Target:** (1) Per-zone aging severity scores (14 facial zones: forehead, glabella, periorbital, malar, nasolabial, perioral, marionette, mental crease, jawline, submental, temple, lateral cheek, lips, neck) on a 0-4 scale matching GAIS and Merz scales. (2) Treatment modality recommendation per zone (neurotoxin, HA filler, biostimulator, RF microneedling, laser resurfacing, topical/peel, no treatment). (3) Predicted outcome score change per treatment combination.
**Evaluation metric:** MAE on per-zone aging scores (targeting <0.5 on 0-4 scale, matching inter-rater variability among expert injectors); treatment modality agreement with expert panel (top-2 accuracy targeting 0.80+); outcome prediction MAE on patient satisfaction scores
**Scope:** Zone-level aging scoring is achievable with 2,000-3,000 expert-annotated facial photo sets. Treatment modality recommendation requires 5,000-10,000 treatment records with before/after photos and outcome ratings. Outcome prediction requires 10,000+ completed treatment courses with standardized before/after photography and satisfaction scores. 3-4 person team, 12-18 months. The photo standardization challenge (consistent lighting, angle, expression) is as significant as the ML challenge.
**Data availability:** Med spas collect extensive before/after photos but in non-standardized formats (varying lighting, angles, expressions, cameras). Treatment records exist in practice management systems (Aesthetic Record, PatientNow). Expert annotations require building a labeling panel of experienced injectors. RealSelf.com contains before/after photos with treatment descriptions and patient reviews — a potential pre-training data source.

---

## 2. Treatment Outcome Prediction from Before/After Photo Analysis
#cnns #transfer-learning #evaluation-metrics #loss-functions #backpropagation #gradient-descent #gans #diffusion-models #cross-validation #bias-variance-tradeoff

**Problem statement:** Patients want to know "what will I look like after this treatment?" and providers want to know "which treatment combination will produce the best result for this face?" Before/after photo analysis across thousands of cases could answer both questions — but no standardized outcome measurement system exists in aesthetics.

**ML task:** Regression — predict post-treatment facial appearance scores from pre-treatment photos and treatment plan
**Input data:** Pre-treatment standardized photos, treatment plan (products, quantities, injection sites, concurrent treatments), patient demographics and skin type, provider experience level
**Target:** Post-treatment aging scores by facial zone (same 14-zone framework as Entry 1); patient satisfaction prediction (1-10 scale); predicted visual outcome (image generation or transformation)
**Evaluation metric:** MAE on predicted vs. actual post-treatment zone scores; patient satisfaction prediction correlation (targeting r > 0.6); visual outcome similarity metric (SSIM or LPIPS on standardized photos)
**Scope:** 5,000-10,000 before/after pairs with complete treatment records and outcome ratings. 2-3 person team, 9-12 months. The visual outcome generation (showing the patient a predicted result) requires GAN or diffusion model approaches and significantly more data.
**Data availability:** Before/after photos exist abundantly but are unstandardized. The main bottleneck is creating matched photo pairs with consistent conditions. RealSelf and practice-level photo databases are potential sources. Patient satisfaction data is collected by some practices but not systematically linked to treatment details.

---

## 3. Client Lifetime Value Prediction
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #linear-regression #probability-distributions #expectation-variance-covariance #bias-variance-tradeoff

**Problem statement:** Med spa revenue depends on repeat visits. Predicting which new patients will become high-LTV clients (>$5,000/year) versus one-time visitors enables targeted retention investment. Currently, practices spend equally on retaining all patients.

**ML task:** Regression — predict 12-month and 24-month patient LTV from initial visit data
**Input data:** Patient demographics (age, sex, zip code income proxy), first-visit treatment type and spend, referral source, payment method (self-pay, membership, financing), booking channel (online, phone, walk-in), treatment type (entry-level like basic facial vs. premium like filler), consultation-to-booking conversion speed
**Target:** Total patient spend at 12 and 24 months
**Evaluation metric:** MAE on predicted LTV; top-decile precision (correctly identifying the highest-value 10% of patients)
**Scope:** 5,000-10,000 patients with 12+ months of history. 1-person team, 2-3 months. Straightforward tabular regression with high business value.
**Data availability:** Practice management systems contain complete patient spend histories. Data extraction is straightforward from Aesthetic Record, PatientNow, or Zenoti. Cross-practice aggregation would improve model performance but requires data sharing agreements.

---

## 4. Injectable Inventory Demand Forecasting
#gradient-boosting #time-series-forecasting #exponential-smoothing #feature-engineering #cross-validation #evaluation-metrics #probability-distributions #expectation-variance-covariance

**Problem statement:** Med spas must balance between product waste (reconstituted Botox expires in 24 hours, fillers have 12-24 month shelf life) and stockouts (canceling a Sculptra appointment because the product wasn't reconstituted 72 hours in advance costs $1,500+ in lost revenue). Forecasting demand by product by day would optimize ordering and preparation.

**ML task:** Time-series forecasting — predict daily units needed by product type
**Input data:** Appointment schedule (booked treatments by type and provider), historical cancellation/no-show rates by day of week and provider, historical product usage per treatment type, seasonal demand patterns (summer = more body treatments, fall = more laser), marketing campaign calendar (promotions drive demand spikes), provider schedule (each provider has different product preferences)
**Target:** Daily units needed by product (Botox units, filler syringes by type, Sculptra vials, etc.)
**Evaluation metric:** MAPE on daily unit prediction; product waste rate reduction; stockout event reduction
**Scope:** 12-24 months of daily usage data per product. 1-person team, 2-3 months. The model is relatively simple; the value is in integrating appointment schedule data with historical usage patterns.
**Data availability:** Treatment records in practice management systems contain product usage. Appointment schedules are digital. The challenge is connecting product inventory systems (often separate from practice management) with treatment data.

---

## 5. Treatment Plan Recommendation Engine
#gradient-boosting #cnns #transfer-learning #feature-engineering #cross-validation #evaluation-metrics #loss-functions #conditional-probability-and-bayes-theorem #bias-variance-tradeoff

**Problem statement:** Given a patient's facial assessment, goals, budget, and treatment history, what combination of treatments will produce the best outcome? Currently each injector makes this decision independently — a recommendation engine trained on outcome data from thousands of cases would provide evidence-based treatment planning.

**ML task:** Recommendation — rank treatment plan options by predicted outcome for this patient
**Input data:** Facial assessment scores (14-zone aging analysis), patient goals (mapped to facial zones — "look less tired" → periorbital + midface), budget constraints, treatment history (what's been done before and when), skin type, contraindications, provider capability (which treatments this provider is trained on)
**Target:** Ranked list of treatment plans with predicted outcome scores, cost, and treatment timeline
**Evaluation metric:** NDCG on treatment plan ranking vs. expert injector recommendations; patient outcome satisfaction correlation for recommended vs. non-recommended plans
**Scope:** Requires the facial assessment model (Entry 1) and outcome prediction model (Entry 2) as prerequisites. Recommendation layer is relatively thin on top of these. 1-2 person team, 3-4 months after prerequisites are deployed.
**Data availability:** Dependent on data from Entries 1 and 2. Additional data: treatment plan records showing what experienced injectors recommend for various presentations — this is the "expert policy" the recommendation engine attempts to replicate and extend.
