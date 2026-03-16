# Machine Learning Opportunities — Pest Control

**Industry:** [[pest-control|Pest Control]]
**Derived from:** [[problems/pest-control/high-impact|High Impact]], [[problems/pest-control/low-impact-1|Low Impact 1]], [[problems/pest-control/low-impact-2|Low Impact 2]], [[problems/pest-control/worker-life-1|Worker Life 1]], [[problems/pest-control/worker-life-2|Worker Life 2]]

---

## 1. Pest Species Identification and Infestation Severity from Visual Evidence
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced pest control technicians identify species from evidence photos (droppings, damage patterns, tracks, body parts, nesting material) and assess infestation severity from distribution patterns — skills that take years to develop and that new technicians lack. A German cockroach dropping looks different from an American cockroach dropping; Norway rat gnaw marks differ from roof rat gnaw marks. The expert reads these signals instantly; the novice misidentifies 30-40% of the time, leading to wrong treatment selection.

**ML task:** Multi-task: (1) Multiclass classification — species identification from evidence photos across 40-60 common pest species; (2) Regression — severity score (1-10) from evidence distribution and volume
**Input data:** Photos of pest evidence (droppings, damage, tracks, grease marks, body parts, nesting material), structural context photos (entry points, harborage locations), geographic region, season, building type
**Target:** Species ID (top-3 with confidence), severity score, estimated population size range, estimated infestation duration
**Evaluation metric:** Top-1 accuracy on species ID targeting 85%+ for top 20 species; top-3 accuracy 95%+. MAE on severity score. Critical: distinguish similar species that require different treatments (German vs. American cockroach, Norway vs. roof rat).
**Scope:** Requires 30,000-100,000 labeled evidence photos across species. Partnership with pest control companies for field photo collection + entomologist labeling. 3-4 person team, 12-18 months. Transfer learning from entomological image datasets. Challenge: field photo quality varies enormously (dark crawlspaces, smartphone cameras, rushed shots).
**Data availability:** No existing large-scale pest evidence dataset. Must be collected from field operations. iNaturalist has some pest photos but not evidence-based (droppings/damage). Entomological collections have specimen photos, not field evidence. University extension services may have labeled collections. Multi-company data partnership needed for species and regional coverage.

---

## 2. Treatment Outcome Prediction
#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** First-visit resolution rates vary 50-90% depending on species, severity, treatment approach, and building characteristics. Predicting whether a treatment plan will resolve the infestation enables treatment plan optimization.

**ML task:** Binary classification (will this treatment plan resolve the infestation within the expected number of visits?)
**Input data:** Species identified, severity score, treatment plan (products, application methods, exclusion work), building characteristics (construction type, age, condition), customer compliance factors (sanitation, exclusion cooperation), geographic/seasonal factors, technician experience level
**Target:** Binary: resolved within expected visits / required additional service
**Evaluation metric:** AUC-ROC; precision-recall optimized for catching failures (recall > 80% on failed treatments)
**Scope:** Trainable on 10,000-50,000 service records with outcome tracking. 1-2 person team, 4-6 months. Challenge: defining "resolved" — some pest issues recur from external reinfestation, not treatment failure.
**Data availability:** Service records in PestPac/FieldRoutes contain treatment details and callback history. Linking initial treatment to resolution outcome requires temporal analysis of service sequences per customer.

---

## 3. Seasonal Pest Pressure Forecasting
#gradient-boosting #time-series-forecasting #tabular-ml

**Problem statement:** Pest activity follows seasonal patterns modified by weather, construction activity, and population dynamics. Anticipating demand spikes (ant season, rodent fall migration) enables staffing and inventory preparation.

**ML task:** Time-series forecasting (predict service call volume by pest category by week for the next 8 weeks)
**Input data:** Historical service call data by pest type and region, weather data (temperature, precipitation, degree-day accumulation), local construction activity, housing density changes, prior season patterns
**Target:** Weekly service call count by pest category (rodents, ants, cockroaches, termites, bed bugs, mosquitoes, wildlife)
**Evaluation metric:** MAPE on weekly call volume by category; must capture peak timing within 1 week
**Scope:** Trainable on 3-5 years of service call data from a regional operator. 1-person team, 2-3 months. Simple time-series models with weather regressors.
**Data availability:** Service call data in operations platforms. Weather data freely available. Low data engineering effort.

---

## 4. Entry Point Detection from Structural Photos
#cnn #object-detection #computer-vision

**Problem statement:** Identifying pest entry points — gaps around pipes, foundation cracks, soffit vents, door sweeps — is critical for exclusion work but requires structural knowledge that takes years to develop.

**ML task:** Object detection (identify and locate potential pest entry points in structural photos)
**Input data:** Photos of building exterior and interior structural features (foundation, utility penetrations, roofline, door frames, vent openings), annotated with entry point locations and sizes
**Target:** Bounding boxes around potential entry points with pest-type relevance (rodent-sized vs. insect-sized), severity score (actively used vs. potential), and recommended exclusion method
**Evaluation metric:** mAP@0.5 for entry point detection; recall above 85% (missing an entry point undermines the entire exclusion plan)
**Scope:** Requires 10,000-30,000 labeled structural photos. 2-3 person team, 9-12 months. Challenge: entry points are context-dependent (a 1/4" gap means nothing for rodents but is critical for cockroaches).
**Data availability:** Photos collectible during routine inspections. Labeling requires experienced technician review. No existing annotated dataset of pest entry points.

---

## 5. Customer-Level Service Optimization
#gradient-boosting #regression #tabular-ml #recommendation

**Problem statement:** Recurring pest control service frequency (monthly, bi-monthly, quarterly) is set at contract signing and rarely adjusted. Some customers are over-serviced (paying for monthly when quarterly would suffice); others are under-serviced (quarterly visits between which infestations return).

**ML task:** Regression (predict optimal service frequency for each customer based on property and historical activity)
**Input data:** Service history (findings per visit, products applied, callback frequency), property characteristics (age, construction, surrounding environment, prior infestation history), geographic pest pressure data, customer sanitation compliance
**Target:** Recommended service frequency (monthly/bi-monthly/quarterly) that maintains pest-free status at minimum service cost
**Evaluation metric:** Reduction in callbacks + service calls between scheduled visits while maintaining or improving customer satisfaction
**Scope:** Trainable on 10,000+ customer service histories with 12+ months of data. 1-person team, 3-4 months. Challenge: changing service frequency is a revenue decision — model must be trusted by operations.
**Data availability:** Service records with findings and callbacks available in operations platforms. Property characteristics partially available; may need enrichment from property databases.
