# Machine Learning Opportunities — Alterations & Tailoring

**Industry:** [[alterations-tailoring|Alterations & Tailoring]]
**Derived from:** [[problems/alterations-tailoring/high-impact|High Impact]], [[problems/alterations-tailoring/low-impact-1|Low Impact 1]], [[problems/alterations-tailoring/low-impact-2|Low Impact 2]], [[problems/alterations-tailoring/worker-life-1|Worker Life 1]], [[problems/alterations-tailoring/worker-life-2|Worker Life 2]]

---

## 1. Fit Assessment from Garment-on-Body Photos (Primary Opportunity — Tacit Knowledge ML)
#cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

**Problem statement:** A master tailor looks at a garment on a client's body for 15-30 seconds and identifies every fit issue — shoulder alignment, back width, chest ease, waist suppression, hip balance, trouser break, hemline level — along with the specific alterations required and the order in which they must be performed. This assessment considers the garment's construction (where seams are, how much allowance exists), the fabric's behavior (how it drapes, stretches, and responds to pressing), and the client's body asymmetries (most bodies are not symmetrical, and garments reveal this). A junior employee or front desk worker cannot perform this assessment at all, creating a bottleneck where only the master tailor can do intake. When the master tailor retires, the shop loses its ability to handle complex garments.

**ML task:** Multi-label classification (detect which fit issues are present from a set of ~30 categories) plus regression (severity/magnitude of each detected issue in cm) plus structured prediction (recommended alteration sequence)
**Input data:** Multi-angle photos of garment on client body (front, back, left side, right side — minimum 4 images), garment category (trouser, jacket, dress, skirt, shirt), approximate fabric type (from visual classification), client's reported concern areas
**Target:** Fit issue detection (presence/absence of each issue category), severity score per issue (magnitude of correction needed in cm), alteration prescription (ordered list of recommended alterations with location and direction), difficulty classification (simple/intermediate/complex/expert-only)
**Evaluation metric:** Weighted F1 on fit issue detection (target: 0.80+ on common issues, 0.65+ on subtle issues like body asymmetry); MAE on severity regression (target: <0.5cm); prescription accuracy measured by expert agreement rate (target: prescription matches at least one expert's recommendation in 75%+ of cases)
**Scope:** Requires 5,000-10,000 annotated garment-on-body photo sets with expert tailor assessments. Each photo set needs 4+ angles with lighting adequate for fabric drape analysis. Data collection through partnership with 20-30 alterations shops, each contributing 10-20 cases per week over 6-12 months. Annotation requires master tailors verbalizing their assessment while viewing photos — unnatural workflow. Transfer learning from pose estimation (for body landmark detection) and garment segmentation (for seam and edge detection) reduces training data requirements. 3-5 person team (2 CV engineers, 1 garment domain expert, 1-2 annotators), 12-18 months. Data collection challenge: fitting room photography is sensitive — lighting varies, clients are partially dressed, and consent is required. Standardized photo protocol must be simple enough for non-technical intake staff. Labeling challenge: expert tailors disagree on ~30% of specific alteration prescriptions (though they agree on issue detection 85%+ of the time). Must handle multi-valid-label situations. Deployment challenge: assessment must complete in under 60 seconds from photo upload to be faster than walking to the master tailor. Must work with smartphone cameras in variable fitting room lighting.
**Data availability:** No public dataset exists. Wedding dress alteration shops have the highest volume of complex garments. Bridal chains (David's Bridal, BHLDN) have internal data but it's proprietary. Independent shops are fragmented. Building the dataset is the primary bottleneck — the model architecture is less novel than the training data.

---

## 2. Alteration Time Estimation
#gradient-boosting #regression #tabular-ml

**Problem statement:** Alteration time varies 5-10x for nominally identical tasks depending on garment construction and fabric. Accurate per-garment time estimation enables correct pricing, realistic scheduling, and fair piece-rate compensation.

**ML task:** Regression (predict total alteration time in minutes for a specific garment and set of alterations)
**Input data:** Garment category, fabric type, construction features (lined/unlined, number of layers, boned/unboned, beaded/unbeaded), specific alterations requested, garment brand/quality tier (fast fashion vs. designer vs. couture), tailor experience level, historical completion times for similar garments in this shop
**Target:** Total alteration time in minutes; confidence interval (to flag high-uncertainty estimates requiring master tailor review)
**Evaluation metric:** MAE in minutes (target: <10 minutes for simple alterations, <20 minutes for complex); percentage within 25% of actual (target: >80%)
**Scope:** Requires 3,000-5,000 completed alterations with actual time tracking. 1-person team, 3-4 months. Challenge: tailors don't currently track time per garment — requires introducing time tracking without creating resentment (piece-rate workers may view tracking as surveillance).
**Data availability:** No structured dataset of alteration times exists. Must be collected prospectively by adding time tracking to the workflow. Historical pricing data (which correlates loosely with time) may serve as a proxy for initial models.

---

## 3. Fabric Behavior Prediction
#cnn #multiclass-classification #computer-vision

**Problem statement:** How a fabric responds to alteration — whether it frays when cut, puckers when machine-sewn, stretches when pressed, or shows needle marks after basting — determines which alteration techniques are appropriate. Master tailors identify fabric behavior by touch and visual inspection. A classification model could identify fabric type and predict behavior from photos.

**ML task:** Multi-class classification (fabric type: wool, silk, polyester, cotton, linen, blends) plus multi-label classification (behavior properties: frays easily, stretches under heat, shows needle marks, requires hand finishing, needs stabilizer)
**Input data:** Close-up photos of fabric (texture, weave pattern, sheen, weight appearance), garment brand (correlated with fabric quality), garment price point
**Target:** Fabric type classification; predicted behavior properties that affect alteration technique selection
**Evaluation metric:** Accuracy on fabric type classification (target: 85%+ for major categories); F1 on behavior property prediction (target: 0.75+)
**Scope:** Requires 2,000-5,000 fabric samples photographed with smartphone cameras and labeled by experienced tailors. 1-2 person team, 4-6 months. Challenge: lighting significantly affects fabric appearance in photos — model must be robust to variable smartphone camera conditions.
**Data availability:** Fabric swatch databases exist in textile industry but don't include behavior labels relevant to alteration work. Must be collected from tailors handling real garments. Could bootstrap from textile classification datasets and add behavior labels.

---

## 4. Customer Satisfaction Prediction
#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** Some alteration outcomes predictably lead to customer dissatisfaction — work on cheap garments where the alteration cost exceeds the garment value, structurally limited alterations where the result will be a compromise, and expectation-reality gaps. Predicting dissatisfaction risk before accepting the job enables proactive expectation management.

**ML task:** Binary classification (will this customer report dissatisfaction or request rework?)
**Input data:** Garment value estimate, alteration cost as percentage of garment value, alteration complexity, number of alterations requested, customer's stated expectations (captured during intake), garment construction limitations that constrain the outcome, customer history (repeat vs. first-time, prior satisfaction)
**Target:** Binary: rework requested or complaint received / satisfied outcome
**Evaluation metric:** AUC-ROC targeting 0.75+; precision at recall 0.6 (flag 60% of dissatisfaction cases with acceptable false positive rate)
**Scope:** Requires 2,000-5,000 completed orders with satisfaction outcomes. 1-person team, 2-3 months. Challenge: most shops don't systematically track satisfaction — dissatisfaction manifests as complaints, rework requests, or simply never returning.
**Data availability:** Limited structured data. Rework requests are trackable. Customer return rates serve as a proxy. Must be collected prospectively.

---

## 5. Pricing Optimization by Market and Complexity
#gradient-boosting #regression #tabular-ml

**Problem statement:** Alterations shops set prices based on tradition and local competition rather than actual cost-to-serve. Optimal pricing that reflects garment complexity, local market willingness-to-pay, and shop capacity utilization could increase revenue by 15-25% without losing volume.

**ML task:** Regression (predict optimal price for a specific alteration on a specific garment in a specific market)
**Input data:** Alteration type and complexity, garment characteristics, estimated completion time, local market pricing (competitor rates), shop capacity utilization (busy vs. slack periods), customer segment (bridal vs. everyday, luxury vs. budget), historical price-to-conversion data
**Target:** Recommended price that maximizes revenue accounting for conversion probability at each price point
**Evaluation metric:** Revenue per alteration-hour compared to baseline flat pricing; conversion rate at recommended prices vs. historical conversion rates
**Scope:** Requires 5,000+ orders with pricing, conversion, and garment data across multiple shops in different markets. 1-2 person team, 4-6 months. Challenge: most shops have no digital pricing records — must be collected prospectively.
**Data availability:** Extremely limited. No industry pricing database exists. Would need to aggregate data across participating shops. Competitive pricing can be scraped from websites of larger alteration chains.
