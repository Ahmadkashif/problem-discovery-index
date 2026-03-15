# Machine Learning Opportunities — Landscaping

**Industry:** [[landscaping|Landscaping]]
**Derived from:** [[problems/landscaping/high-impact|High Impact]], [[problems/landscaping/low-impact-1|Low Impact 1]], [[problems/landscaping/low-impact-2|Low Impact 2]], [[problems/landscaping/worker-life-1|Worker Life 1]], [[problems/landscaping/worker-life-2|Worker Life 2]]

---

## 1. Turf Disease and Nutrient Deficiency Classification from Photos
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced lawn care technicians diagnose turf disease and nutrient deficiency by reading visual patterns on grass — lesion shape, color, distribution, mycelium presence — a visual library built from years of field experience. A CNN trained on labeled turf diagnostic photos can replicate this diagnosis to enable junior technicians to apply correct treatments on the first visit.

**ML task:** Multi-label image classification per photo — disease/deficiency type (Brown Patch, Dollar Spot, Pythium, Gray Leaf Spot, Nitrogen Deficiency, Iron Chlorosis, Potassium Deficiency, etc.) with confidence and differential diagnosis
**Input data:** Turf photos labeled by certified turfgrass agronomists or CPAs (Certified Pesticide Applicators). Regional stratification required — cool-season grass diseases differ from warm-season. University turf research program archives as seed dataset.
**Target:** Top-3 differential diagnosis with confidence; key visual features driving each diagnosis; recommended treatment protocol
**Evaluation metric:** Agreement rate with expert agronomist diagnosis on held-out photos; treatment outcome rate (did the recommended treatment resolve the issue by next visit?); false positive rate on fungicide recommendation (unnecessary application cost)
**Scope:** University turfgrass programs (Penn State, Ohio State, UGA, NC State, Texas A&M) maintain diagnostic photo archives and have certified diagnosticians. A consortium data collection partnership to build a 30,000-60,000 image labeled dataset: 6-10 month data collection phase. Fine-tuning a CNN on this dataset: 8-12 week training phase.
**Data availability:** Academic archives exist but may not be organized for ML training. Field collection from lawn care firms with agronomist review for labels is the path to a large enough training set. Climate-regional stratification is essential for model accuracy.

---

## 2. Customer Churn Prediction for Seasonal Renewal
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Predict which recurring lawn care customers will not renew for the upcoming season based on their prior-season service history — enabling proactive outreach 60-90 days before the season begins.

**ML task:** Binary classification (will not renew: yes/no) from prior-season service features
**Input data:** Customer features: service frequency (completed vs. skipped visits), complaint/service issue count, payment timeliness, service add-on count, tenure (years), total annual spend, last contact date with account manager, seasonal service interruptions
**Target:** Churn probability per customer at 90-day pre-season horizon; churn segment (disengaged, service-quality issue, price-sensitive, moving/life change)
**Evaluation metric:** Recall on customers who did not renew (did we flag them in advance?); precision at top-quintile flag (were flagged customers actually at risk?); revenue retained through proactive outreach to flagged customers vs. control
**Scope:** Any landscaping firm with 300+ recurring customers and 2+ years of Jobber/LMN data has training data. Gradient boosting on ~12 customer features: 3-4 week project. Value is in the proactive outreach program, not the model complexity.
**Data availability:** Jobber and LMN log service completion, complaints, and billing. Renewal status (did the customer return next season?) is the label — available from the next season's customer records.

---

## 3. Job Duration Estimation for Route Optimization
#gradient-boosting #regression #tabular-ml #quick-win

**Problem statement:** Accurate service time estimates per property are the foundation of efficient multi-stop routing. Replace manual time estimates (crew foreman's judgment) with a regression model trained on actual historical job durations by property characteristics.

**ML task:** Regression — estimated job duration in minutes from property features
**Input data:** Historical job completion records: measured job duration (clock-in/clock-out from field app), property size (sq ft, from county records or Google Maps), obstacle count (trees, beds, tight areas), service type (mow-only, mow+edge+blow, mow+edge+blow+hedge trim), crew size, equipment type used
**Target:** Job duration estimate per property per service type; variability estimate (high vs. low uncertainty) for properties with inconsistent history
**Evaluation metric:** MAE between predicted and actual job duration on held-out jobs; improvement in daily route completion rate vs. manual time estimates; overtime rate for crews using model-estimated routes vs. manual
**Scope:** Quick win — Jobber and LMN log job durations with clock-in/clock-out timestamps. Any firm with 6+ months of service records and 100+ recurring properties has training data. Linear or gradient boosting regression on 6-8 property features: 2-3 week project.
**Data availability:** Job duration data is in any field service platform with time-tracking. Property size requires one-time property area lookup (county assessor or Google Maps API). Both are readily available.

---

## 4. Irrigation System Fault Classification from Zone Observation Data
#gradient-boosting #multiclass-classification #tabular-ml #tacit-knowledge-ml #quick-win

**Problem statement:** Codify the diagnostic reasoning of experienced irrigation technicians — interpreting dry spots, pressure patterns, and head performance per zone — into a structured model that generates the repair list from observation inputs.

**ML task:** Multiclass classification per zone — fault type (broken head, tilted head, valve failure, pressure loss, coverage gap, normal) from observation inputs; tabular prediction from zone-level feature inputs
**Input data:** Irrigation service records with per-zone observations (technician-logged) and confirmed repair items. Features: zone area, head type, observed pressure category, head count, visible surface anomalies, zone runtime history.
**Target:** Fault type per zone; complete repair and parts list for the system; estimated labor hours
**Evaluation metric:** Recall on repair items (did the model identify all repairs that were completed?); precision (did the model generate repair items that were confirmed as necessary?); return trip rate for jobs using vs. not using structured observation capture
**Scope:** Quick win once observation capture is digitized. Firms currently logging repairs in Jobber or ServiceTitan with consistent service codes have partial training data — adding structured zone observation capture provides the feature inputs. 2-3 month data collection + 3-4 week modeling.
**Data availability:** Repair items are logged in service platforms. Zone-level observation data requires adding a structured intake form to the technician's mobile workflow — moderate friction but tractable.

---

## 5. Weed Species Identification and Selective Herbicide Recommendation
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** Selective herbicide application requires identifying the weed species — grassy weeds (crabgrass, annual bluegrass) require different herbicides than broadleaf weeds (clover, dandelion, ground ivy), and applying the wrong product wastes cost and may harm the turf. Experienced technicians identify weed species visually; junior technicians default to broad-spectrum products that are less effective and higher cost.

**ML task:** Multiclass classification — weed species from photo (leaf shape, growth habit, color). Target: 30-50 most common residential turf weeds by climate region.
**Input data:** Weed photos labeled by species by certified pesticide applicators or turfgrass agronomists. iNaturalist and PlantNet have large plant photo datasets that can seed the residential turf weed subset.
**Target:** Weed species identification with confidence; recommended herbicide category (pre-emergent, selective post-emergent, non-selective); timing advice (application timing relative to weed growth stage)
**Evaluation metric:** Top-1 species accuracy on held-out photos; treatment outcome rate (was the recommended herbicide effective by the next service visit?); false identification rate on grass species (misidentifying turf as a weed)
**Scope:** iNaturalist and PlantNet provide millions of plant photos with species labels — the residential lawn weed subset (50 species) can be extracted and fine-tuned. The main challenge is regional accuracy (weed species distribution varies by climate zone) and turfgrass-specific context (distinguishing annual bluegrass from Kentucky bluegrass in a lawn context). 8-12 week fine-tuning project on existing plant identification models.
**Data availability:** Open-source plant identification datasets (iNaturalist, PlantNet) provide a foundation. Residential lawn-specific fine-tuning data requires collection from lawn care firms with certified applicator labels.
