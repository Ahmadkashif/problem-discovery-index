# Machine Learning Opportunities — Funeral Homes

**Industry:** [[funeral-homes|Funeral Homes]]
**Derived from:** [[problems/funeral-homes/high-impact|High Impact]], [[problems/funeral-homes/low-impact-1|Low Impact 1]], [[problems/funeral-homes/low-impact-2|Low Impact 2]], [[problems/funeral-homes/worker-life-1|Worker Life 1]], [[problems/funeral-homes/worker-life-2|Worker Life 2]]

---

## 1. Family Needs and Budget Assessment from Arrangement Conference Signals (Primary Opportunity — Tacit Knowledge ML)
#gradient-boosting #bert #regression #nlp #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced funeral directors read dozens of signals during a family's first contact and arrangement conference — the family's communication style, vocabulary around death (clinical vs. euphemistic), questions about pricing versus questions about personalization, references to the deceased's wishes, family group dynamics (who speaks, who defers) — and synthesize these into an intuitive assessment of which service tier, add-ons, and memorialization options to present. This tacit read determines whether a family spends $4,000 or $14,000. New directors lack this pattern recognition and either under-present (losing revenue) or over-present (creating resentment). The knowledge retires with veteran directors and is never systematically captured.

**ML task:** Multi-output regression (predicted spend by category: casket, service, memorialization, add-ons) plus classification (recommended presentation tier)
**Input data:** Family intake form data (relationship to deceased, number of family members involved, preneed file existence, expressed preferences), community demographics (median household income by ZIP, religious composition), historical case data (prior families from same community, same referral source), communication signals from intake call transcription (sentiment, vocabulary analysis, question patterns), case characteristics (age of deceased, cause of death category, military/fraternal affiliations)
**Target:** Total case revenue by category; recommended service presentation tier (economy/standard/premium/luxury); add-on acceptance probability for each available option
**Evaluation metric:** MAE on total case revenue prediction (target: within $1,500 of actual); AUC on tier classification; Spearman rank correlation on add-on recommendation ordering
**Scope:** Requires 2,000-5,000 historical cases with complete revenue breakdowns and family demographic data. Intake call transcription adds NLP capability. 2-3 person team, 6-9 months. Data collection challenge: arrangement conferences are unrecorded, so the model must rely on pre-conference signals and post-conference outcomes. Labeling challenge: directors may disagree on what constitutes the "right" presentation for a given family. Deployment challenge: recommendations must feel like decision support, not sales scripts — directors will reject anything that feels like it commoditizes grief.
**Data availability:** Case management systems (SRS, Passare) contain revenue data per case. Family demographic data requires integration with census/ZIP-level data. Intake call recordings require opt-in transcription. Historical pattern data exists in experienced directors' memories but not in any system — initial model must rely on structured case data and demographics, with NLP added as call transcription data accumulates.

---

## 2. Preneed Conversion Prediction
#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** Preneed (pre-planning) sales represent the funeral industry's highest-margin revenue and customer lock-in, but conversion rates from outreach to signed contract average only 3-5%. Identifying which community members are most likely to convert from general interest to funded preneed contracts would dramatically improve marketing ROI.

**ML task:** Binary classification (will this prospect convert to a funded preneed contract within 12 months?)
**Input data:** Prospect demographics (age, marital status, homeownership, ZIP code), engagement history (seminar attendance, website visits, brochure requests, community event participation), referral source, prior funeral home interactions (at-need cases for family members), community affiliation data (church membership, civic organization, veterans' group)
**Target:** Binary: funded preneed contract signed within 12 months / not converted
**Evaluation metric:** AUC-ROC targeting 0.75+; precision at recall 0.5 (identify the 50% most likely converters with high confidence to focus outreach resources)
**Scope:** Requires 5,000-20,000 prospect records with conversion outcomes over 2-3 years. 1-person team, 3-4 months. Data aggregation across multiple funeral homes needed for sufficient sample size.
**Data availability:** Preneed CRM systems contain prospect and conversion data. Most funeral homes track this in spreadsheets or basic CRM tools. Data standardization across homes is the primary challenge.

---

## 3. Death Call Volume Forecasting
#linear-regression #time-series-forecasting #tabular-ml

**Problem statement:** Funeral homes staff based on historical averages but experience significant demand volatility — flu seasons, heat waves, cold snaps, and pandemic waves create surges that overwhelm capacity, while summer months may leave staff underutilized. Accurate 2-4 week forecasting would enable proactive staffing adjustments.

**ML task:** Time-series forecasting (predict weekly case volume 2-4 weeks ahead)
**Input data:** Historical weekly case volume (3-5 years), local weather forecasts (temperature extremes), CDC influenza surveillance data, local hospital census data, community demographics (aging population trends), seasonal patterns, local obituary counts from competing funeral homes
**Target:** Weekly case count (and daily distribution) for the next 2-4 weeks
**Evaluation metric:** MAPE targeting <20% at 2-week horizon; directional accuracy >75% (predicting above/below average weeks)
**Scope:** Relatively simple time-series model. 1-person team, 2-3 months. Challenge: individual funeral home volume is low (3-6 cases/week) making prediction noisy. Regional aggregation improves signal.
**Data availability:** Case volume data exists in management systems. Weather data is freely available. CDC flu data is public. Hospital census data may require partnerships. Small sample sizes per funeral home require multi-home aggregation.

---

## 4. Obituary Generation Quality Scoring
#bert #regression #nlp

**Problem statement:** AI-generated obituaries vary in quality — some read as generic templates while others capture the deceased's personality authentically. An automated quality scorer would enable iterative improvement of obituary generation systems and flag outputs that need human editing.

**ML task:** Regression (predict obituary quality score on a 1-10 scale)
**Input data:** Generated obituary text, source biographical details provided by family, comparison to the funeral home's historical obituary style, readability metrics, factual completeness checklist (survivors listed, service details included, charitable donations mentioned)
**Target:** Quality score (1-10) based on: factual completeness, tonal appropriateness, personal detail specificity, readability, family satisfaction proxy
**Evaluation metric:** Spearman rank correlation with human quality ratings; MAE on 1-10 scale targeting <1.0
**Scope:** Requires 1,000-3,000 obituaries rated by funeral directors or family members on quality dimensions. 1-person team, 3-4 months. Annotation is the bottleneck — directors are time-constrained.
**Data availability:** Obituaries are publicly available on funeral home websites and Legacy.com. Quality ratings must be collected from funeral professionals. Biographical source data (what the family provided) is harder to obtain.

---

## 5. Service Package Recommendation Engine
#gradient-boosting #recommendation #tabular-ml

**Problem statement:** Funeral homes offer 50-150 individual items and services that can be combined in thousands of ways, but directors typically present 3-4 standard packages. A recommendation engine that suggests personalized packages based on family characteristics and expressed preferences would increase both family satisfaction and revenue.

**ML task:** Recommendation (suggest optimal service package from family characteristics and preferences)
**Input data:** Family demographic and preference data from intake, case characteristics (burial vs. cremation, religious tradition, veteran status, fraternal affiliations), historical purchasing patterns for similar profiles, regional norms, price sensitivity indicators
**Target:** Ranked list of recommended service configurations with predicted satisfaction and predicted revenue
**Evaluation metric:** Hit rate (recommended package matches or is within one tier of selected package); revenue uplift vs. default package presentation
**Scope:** Requires 3,000-10,000 completed cases with detailed service selections and family characteristics. 1-2 person team, 4-6 months. Cold-start problem for new funeral homes or first-time families from underrepresented demographics.
**Data availability:** Case management systems contain detailed service selections. Family characteristic data is sparse in most systems — requires enrichment from intake forms and demographic data. Cross-funeral-home data sharing is limited by competitive concerns and privacy.
