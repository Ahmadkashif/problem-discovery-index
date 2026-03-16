# ML Opportunities — Land Surveyors

**Industry:** [[land-surveyors|Land Surveyors]]
**Tags:** #bert #cnn #gradient-boosting #lstm #llm #multiclass-classification #regression #binary-classification #semantic-segmentation #ocr #anomaly-detection #text-classification #nlp #computer-vision #tabular-ml #signal-processing #tacit-knowledge-ml #revenue-impact #compliance

---

## 1. Monument and Boundary Evidence Detection from Historical Documents and Field Reconnaissance (Primary Opportunity — Tacit Knowledge ML)

#bert #cnn #multiclass-classification #nlp #computer-vision #tacit-knowledge-ml

**Problem statement:** Senior surveyors identify boundary evidence — iron pins beneath soil, stone remnants indicating historical monuments, tree lines following old fence rows, deed language patterns indicating specific eras and conventions — through pattern recognition built over decades of local practice. This tacit knowledge is the profession's most critical capability and is being permanently lost as 3,000-4,000 surveyors retire annually. Junior surveyors miss evidence that seniors would catch, leading to 2-3 additional field trips per complex boundary survey and, in worst cases, incorrect boundary determinations.

**ML task:** Multi-class classification of field evidence (monument type, age, reliability) combined with NLP classification of deed language (era, convention, bearing system, monument hierarchy).

**Input data:** Field photographs of found monuments and boundary evidence (georeferenced, with scale reference), drone/aerial imagery of the survey area showing vegetation patterns and topographic features, scanned deed documents (often handwritten, 50-200 years old), and historical aerial photography (USGS archives dating to 1930s-1940s).

**Target:** For field evidence: classification of monument type (iron pin, stone, concrete, pipe, nail), estimated installation era (pre-1900, 1900-1950, 1950-2000, post-2000), and reliability score (original monument, replacement, unrelated object). For deed language: structured extraction of bearings (with magnetic declination era), distances (with unit identification), monument descriptions (with permanence classification per boundary law hierarchy: natural > artificial > record), and adjoiner references (linked to parcel IDs).

**Model:** Two parallel pipelines. CV pipeline: CNN (ResNet-50 or EfficientNet) trained on labeled monument photographs for type/era classification, plus semantic segmentation of drone imagery to identify occupation lines (fence rows, tree lines, mowed boundaries) and topographic features referenced in deeds. NLP pipeline: BERT fine-tuned on historical deed language for structured extraction, with an OCR pre-processing stage (Tesseract or cloud OCR) for handwritten deeds. Outputs from both pipelines feed into a boundary evidence fusion model that produces confidence-weighted corner position candidates.

**Evaluation:** CV pipeline: per-class F1 on monument classification (target: 85%+ on common types). NLP pipeline: exact match on bearing/distance extraction (target: 95%+ on typed deeds, 80%+ on handwritten). End-to-end: percentage of boundary corners where the model's top recommendation matches the PLS's final determination (target: 70%+ for straightforward cases, 50%+ for contested/ambiguous cases).

**Scope:** Very high difficulty. 18-24 months to production. Requires multi-modal data collection partnership with 15-25 survey firms across diverse geographies (Midwest metes-and-bounds, Western PLSS, Eastern colonial deeds). Team: 2 ML engineers, 1 CV specialist, 1 NLP specialist, 1 senior PLS (20+ years), 1 boundary law consultant. Budget: $800K-$1.2M.

**Data availability:** Deed records are available from county recorders but vary widely in digitization level. Historical aerial photography is available from USGS Earth Explorer. Monument photographs are the critical gap — firms don't systematically photograph found evidence. Building the training dataset requires equipping cooperating firms with a standardized photo capture workflow (georeferenced, scaled, classified) for 6-12 months of field work. An estimated 5,000-10,000 labeled monument photographs are needed for robust classification.

---

## 2. Survey Time and Cost Estimation

#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** Survey firms estimate project costs based on the PLS's experience with similar projects, but estimates are frequently wrong — underestimates lose money, overestimates lose bids. The variables that drive actual field time (terrain difficulty, vegetation density, monument recovery probability, deed complexity) are assessable from available data but not systematically modeled.

**ML task:** Regression — predict total field hours and office hours for a survey project given property and project characteristics.

**Input data:** Parcel geometry (size, shape complexity, number of corners), terrain characteristics (slope from DEM, vegetation density from aerial imagery, access point distance), deed characteristics (number of calls, age of oldest deed in chain, number of adjoiners), project type (boundary, ALTA, topographic, construction staking), historical monument recovery rates for the area, and weather/season factors.

**Target:** Predicted field hours (crew-hours) and office hours (CAD/processing hours), with confidence interval. Secondary: predicted number of field trips required.

**Model:** Gradient-boosted regression with features engineered from GIS data (parcel geometry metrics, terrain roughness from LiDAR DEM, NDVI from aerial imagery for vegetation density) and deed complexity metrics (NLP-derived from deed text).

**Evaluation:** MAPE on total project hours. Target: within 15% of actual for standard boundary surveys, within 25% for complex ALTA surveys. Calibration: 80% of actual values within the predicted 80% CI.

**Scope:** Moderate. 4-6 months to MVP. Training data from cooperating firms' project records (completed projects with actual hours vs. estimates). Team: 1 ML engineer, 1 GIS specialist.

**Data availability:** Moderate. Firms track actual hours against estimates internally, but this data is not standardized. Requires partnerships with 10-20 firms to export project records. GIS features (parcel boundaries, terrain, aerial imagery) are publicly available.

---

## 3. Deed Language Interpretation and Legal Description Generation

#bert #llm #ocr #text-classification #nlp

**Problem statement:** Reading and interpreting deed language is one of the most time-consuming aspects of boundary survey preparation. A complex chain of title may include 5-15 deeds spanning 100+ years, written in evolving legal conventions and sometimes handwritten. Extracting the structured boundary description (bearings, distances, monuments, adjoiners) from these documents takes 1-4 hours per survey.

**ML task:** Information extraction — parse deed text into structured boundary calls (bearing, distance, monument, curve data, adjoiner reference) with era-appropriate interpretation.

**Input data:** Deed document images (scanned, often handwritten for older deeds), OCR-processed deed text, and county-specific deed convention metadata (when magnetic bearings transitioned to true bearings, local measurement unit conventions, common legal phrases and their interpretations).

**Target:** Structured boundary call table: for each call, the bearing (corrected to current reference frame), distance (in feet), monument description (classified by type and permanence), and adjoiner reference (linked to parcel ID where possible). Confidence score for each extracted element.

**Model:** OCR pipeline (custom-trained for historical handwriting styles common in legal documents) feeds into a BERT-based information extraction model fine-tuned on annotated deed texts. County-specific adaptation through few-shot fine-tuning on local deed conventions.

**Evaluation:** Exact match rate on bearing extraction (target: 95% on typed, 80% on handwritten), distance extraction (target: 98% on typed, 85% on handwritten), and monument classification (target: 90%). End-to-end: time savings vs. manual extraction (target: 60%+ reduction).

**Scope:** Moderate-high. 6-9 months to MVP. OCR quality on handwritten deeds is the primary technical challenge. Team: 1 ML engineer, 1 NLP specialist, 1 PLS domain expert.

**Data availability:** Deed images available from county recorders, increasingly digitized. The labeling challenge is significant — annotating structured boundary calls from deed text requires PLS-level expertise. An initial labeled corpus of 2,000-5,000 deeds from cooperating firms and county records would establish the training base.

---

## 4. Point Cloud to Survey Plat Automation

#cnn #semantic-segmentation #computer-vision #gradient-boosting #regression #tabular-ml

**Problem statement:** LiDAR scanners and drone photogrammetry generate point clouds with millions of points, but extracting survey-relevant features (ground surface, structures, utilities, vegetation boundaries) and producing deliverables (topographic maps, cross-sections, volume calculations) still requires 8-20 hours of manual processing per project.

**ML task:** Semantic segmentation of 3D point clouds into survey-relevant categories, plus automated feature extraction for deliverable generation.

**Input data:** Georeferenced 3D point clouds (LiDAR or photogrammetry-derived), project specifications (deliverable type, contour interval, feature categories required), and jurisdictional standards (symbology, annotation conventions).

**Target:** Classified point cloud (ground, vegetation, building, utility, water, road surface, curb, fence, etc.) plus extracted feature linework (building footprints, edge of pavement, utility poles, fence lines, contour lines) in CAD-ready format.

**Model:** PointNet++ or KPConv for 3D point cloud semantic segmentation, trained on survey-classified point clouds. Post-processing pipeline converts classified points to vector linework meeting survey drafting standards.

**Evaluation:** Per-class IoU on point classification (target: 90%+ for ground, buildings, vegetation; 80%+ for utilities, fences). Linework accuracy: positional accuracy within survey tolerance (0.1 feet for boundary features, 0.5 feet for topographic features).

**Scope:** High difficulty. 9-12 months to MVP. Point cloud datasets with survey-grade classification labels are rare — must be created through partnerships with firms performing LiDAR/drone surveys. Team: 2 ML engineers (3D CV expertise), 1 survey domain expert.

**Data availability:** Raw point clouds are increasingly common (firms collect them on every project), but survey-classified point clouds (where each point is labeled by an experienced technician) are rare and expensive to produce. A labeled dataset of 50-100 classified point clouds from diverse project types is the minimum training requirement.

---

## 5. Boundary Dispute Risk Prediction

#gradient-boosting #binary-classification #tabular-ml #nlp

**Problem statement:** Surveyors occasionally deliver boundary determinations that trigger disputes between adjacent landowners — creating professional liability exposure, costly litigation, and client dissatisfaction. Identifying high-dispute-risk surveys before delivery would allow the surveyor to take additional precautions (more thorough research, adjoiner notification, additional monument documentation).

**ML task:** Binary classification — predict whether a boundary survey will result in a dispute or complaint within 2 years of delivery.

**Input data:** Survey characteristics (parcel value, deed ambiguity score, number of adjoiners, monument recovery rate, magnitude of discrepancy between deed and measured distances), neighborhood characteristics (recent property sales activity, ongoing construction, homeowner demographics), and historical dispute data for the area.

**Target:** Binary dispute probability within 2 years. Secondary: predicted dispute type (fence encroachment, building encroachment, access/easement, acreage discrepancy).

**Model:** Gradient-boosted classifier on engineered features from survey data and neighborhood characteristics. Text features from deed language (ambiguity indicators) extracted via NLP preprocessing.

**Evaluation:** PR-AUC given low base rate (~3-5% of surveys result in disputes). Optimize for recall — missing a high-risk survey is more costly than a false alarm that triggers extra due diligence. Target: flag 60%+ of eventual disputes at 30% precision (acceptable because the "cost" of a false positive is merely additional care, not wasted effort).

**Scope:** Moderate. 4-6 months to MVP. Training data from firms' records of completed surveys paired with subsequent dispute/complaint/claim records. Team: 1 ML engineer, 1 PLS domain expert.

**Data availability:** Moderate. Survey delivery records are available from cooperating firms. Dispute data is harder to aggregate — comes from professional liability insurance claims (available through insurance carriers) and court records (boundary dispute filings). A dataset of 10,000+ completed surveys with 2-year outcome tracking from 10-20 firms would provide sufficient training data.
