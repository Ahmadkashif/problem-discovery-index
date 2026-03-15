# Machine Learning Opportunities — Roofing Contractors

**Industry:** [[roofing-contractors|Roofing Contractors]]
**Derived from:** [[problems/roofing-contractors/high-impact|High Impact]], [[problems/roofing-contractors/low-impact-1|Low Impact 1]], [[problems/roofing-contractors/low-impact-2|Low Impact 2]], [[problems/roofing-contractors/worker-life-1|Worker Life 1]], [[problems/roofing-contractors/worker-life-2|Worker Life 2]]

---

## 1. Hail and Wind Damage Classification from Inspection Photos
#cnn #multiclass-classification #object-detection #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced roofing inspectors identify storm damage type, severity, and insurance eligibility by reading visual patterns on asphalt shingles — hail impact crater size and depth, granule displacement density, wind lift signatures — a tacit visual skill built from thousands of insurance inspections. A CNN trained on labeled inspection photos can replicate this damage classification to enable junior inspectors to produce adjuster-quality assessments.

**ML task:** Multi-label image classification per photo: damage type (hail impact / wind lift / granule loss / mechanical / wear), severity tier, functional vs. cosmetic damage flag, claim evidence quality score (strong/weak/insufficient)
**Input data:** Roof inspection photos labeled by damage type and insurance claim outcome. Supervision signal from filed claims with adjuster-approved vs. denied line items. Covers multiple shingle types (3-tab, architectural, designer), hail sizes (sub-1" to 2"+), and roofing material conditions (new/mid-life/aging).
**Target:** Per-photo damage classification with confidence; aggregated job-level damage summary report with claim evidence quality rating per damage category
**Evaluation metric:** Agreement rate with senior estimator damage classification on held-out inspection sets; recall on claimable damage vs. adjuster-contested outcomes; false negative rate on covered damage (missed claim items)
**Scope:** Labeled training data is the primary bottleneck. Insurance claim data from roofing franchise networks (GAF, Owens Corning contractor networks) provides both photos and outcome supervision. Fine-tuning a vision model (YOLOv8, GPT-4V fine-tune, or Gemini) on 50,000–100,000 labeled photos: 9-15 months end-to-end. The franchise network partnership provides distribution to thousands of contractors simultaneously.
**Data availability:** Photos exist at every insurance restoration roofing firm — CompanyCam and similar platforms have massive repositories. The labeling challenge is attaching claim outcome data (adjuster approved/denied per line item) to individual photos. A structured data partnership with a major roofing manufacturer's contractor network makes this tractable.

---

## 2. Roof Condition Scoring from Aerial Imagery
#cnn #regression #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced roofing estimators can visually assess a roof's remaining useful life and current condition from aerial imagery or street view — reading granule loss patterns, visible sagging, discoloration, and patch repair history. Automate this assessment at scale to enable post-storm property targeting and proactive maintenance outreach.

**ML task:** Regression (condition score 0-100, estimated remaining useful life in years) from aerial/satellite imagery; binary classification (replacement candidate within 2 years: yes/no)
**Input data:** Aerial imagery (EagleView, Nearmap, Google Maps) matched to roofing service history for the same properties. Supervision signal: properties where a roof was replaced within 24 months of imagery capture represent "near-end-of-life" ground truth.
**Target:** Condition score per property; replacement probability score for lead generation and post-storm targeting
**Evaluation metric:** Correlation between condition score and actual replacement rate; precision at top-quintile replacement flag; AUC for 2-year replacement prediction
**Scope:** Aerial imagery is commercially available at scale. Building a training dataset by joining aerial imagery to roofing contractor service records (date of last replacement + property address) is tractable via data partnerships. 100,000+ labeled property records. A gradient boosting or CNN model on normalized aerial imagery patches: 4-8 weeks of training once dataset is assembled.
**Data availability:** EagleView and Nearmap license imagery to roofing contractors. Condition ground truth (replacement date) comes from contractor service records and permit databases (many jurisdictions record permit-pulled roof replacements).

---

## 3. Storm Canvas Lead Scoring
#gradient-boosting #ranking #tabular-ml #revenue-impact

**Problem statement:** Rank properties within a storm footprint by insurance claim probability to optimize sales rep canvas routing after hail and wind events.

**ML task:** Ranking/scoring — composite lead score per property from weather data, aerial condition, and property characteristics
**Input data:** Per-property features: hail size at property location (NOAA/CoreLogic), roof age from permit records or last contractor service, aerial condition score, property type (owner-occupied vs. rental), prior claim history if available, home age
**Target:** Claim probability score per property; ranked canvas route for sales rep
**Evaluation metric:** Conversion rate (signed contract per door knock) in ranked-top vs. unranked canvas sets; revenue per canvas hour with vs. without routing intelligence
**Scope:** This is a tabular gradient boosting problem once the feature engineering pipeline (joining weather, property, and permit data) is built. The feature pipeline is 80% of the work. 2-3 months end-to-end. Integration with the firm's CRM (AccuLynx, JobNimbus) for route output is the deployment step.
**Data availability:** NOAA storm data and commercial hail verification (CoreLogic, Verisk) are available by subscription. County assessor data provides property age and owner status. Permit records provide roof replacement dates in most jurisdictions.

---

## 4. Supplement Line-Item Prediction from Inspection Data
#gradient-boosting #multiclass-classification #tabular-ml #revenue-impact

**Problem statement:** Predict which Xactimate line items are claimable for a given inspection report — and which the insurance carrier is likely to contest — to guide supplement writing and prioritize negotiation effort.

**ML task:** Binary classification per potential line item (approved/denied given carrier + damage profile + jurisdiction); ranking of supplement items by approval probability
**Input data:** Historical claim submissions with line-item outcomes by carrier, damage type, property location, and claim date. Labeled by: approved on first submission / approved after supplement / denied.
**Target:** Per-line-item approval probability; ranked list of supplement items worth pursuing for a given claim profile
**Evaluation metric:** Precision on predicted-approved items (did we submit items the adjuster actually approved?); recall on claimable items (did we identify all approvable line items?); supplement revenue per claim for firms using vs. not using the model
**Scope:** Requires structured historical claim data with per-line-item outcomes. Available at large roofing franchise networks with standardized Xactimate workflows. Gradient boosting on claim features: 3-4 week modeling project once data is assembled.
**Data availability:** Xactimate exports per-claim line items with approved/denied status. Firms with disciplined Xactimate workflow and 2+ years of claims history have sufficient training data.

---

## 5. Installation Quality Control from Progress Photos
#cnn #binary-classification #computer-vision #tacit-knowledge-ml #quick-win

**Problem statement:** Roofing manufacturer warranties (GAF Golden Pledge, CertainTeed SureStart Plus) require specific installation details — starter strip alignment, nail pattern, valley metal flashing method, ridge cap exposure — that are verified by photo documentation. A quality control model that flags installation photos for non-compliant details enables real-time QC without requiring a senior inspector on every job.

**ML task:** Binary classification per installation photo (compliant/non-compliant) for specific warranty checkpoints; defect localization (what specifically is non-compliant)
**Input data:** Installation photos labeled for compliance with manufacturer installation specifications for each checkpoint type. Supervision from manufacturer warranty audit outcomes.
**Target:** Real-time compliance flag during installation; end-of-job compliance report for warranty submission
**Evaluation metric:** Recall on non-compliant installations (catching real defects before the job is complete); false positive rate; manufacturer warranty approval rate for jobs inspected with vs. without the model
**Scope:** Manufacturer-specific installation specs define clear labeling criteria. A dataset of 20,000–40,000 labeled installation checkpoint photos (compliant/non-compliant per spec checkpoint) is achievable through a manufacturer contractor network. Quick win because the classification is binary, the compliance criteria are well-defined, and the training signal is unambiguous.
**Data availability:** Manufacturers track warranty claims and installation quality audits. A GAF or Owens Corning data partnership provides both labeled training photos and distribution to their certified contractor networks.
