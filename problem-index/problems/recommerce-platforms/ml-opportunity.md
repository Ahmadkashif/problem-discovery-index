# Machine Learning Opportunities — Recommerce Platforms

**Industry:** [[recommerce-platforms|Recommerce Platforms]]
**Derived from:** [[problems/recommerce-platforms/high-impact|High Impact]], [[problems/recommerce-platforms/low-impact-1|Low Impact 1]], [[problems/recommerce-platforms/low-impact-2|Low Impact 2]], [[problems/recommerce-platforms/worker-life-1|Worker Life 1]], [[problems/recommerce-platforms/worker-life-2|Worker Life 2]]

---

## 1. Joint Price and Time-to-Sell Prediction from Images
#cnns #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #k-nearest-neighbors #time-series-forecasting #revenue-impact

**Problem statement:** Every unit is unique, comparables are thin for most of the long tail, and processing cost is sunk before the price is set. The objective is not the highest price but the best combination of price and holding cost, and the category treats it as a lookup against a rules table.

**ML task:** Joint modelling of realised price and time-to-sell as a function of item attributes and photographs, formulated as survival analysis conditional on listed price
**Input data:** Intake photographs under controlled lighting; extracted and entered attributes including brand, category, size, colour, material and style; assigned condition grade; listed price and any markdown path; realised sale price and date, or expiry; storage cost per day; seasonality; category demand trends.
**Target:** The sale probability curve over time at a given price, and the realised price.
**Evaluation metric:** Expected contribution per item under model-set prices against the current rules baseline, on held-out inventory — the direct economic test, since neither price accuracy nor sell-through alone captures the trade-off. Report calibration of the sale probability curve, because the markdown optimisation depends on it being right rather than merely ranked correctly.
**Scope:** Photographs carry condition information that the grade band discards, which is why image features rather than the grade should be the primary input — this is the central design decision. Thin comparables are the reason a learned mapping from attributes to price beats comparable lookup for the long tail, which is most of the inventory by count. The same model applied at intake, deciding whether to accept an item at all, is the highest-leverage application and comes free once the model exists. 3 ML engineers, 6 months.
**Data availability:** Outstanding — every managed platform holds photographs, attributes, grades, prices and outcomes for millions of items. Storage cost per item is often not attributed at item level, which is needed to make the trade-off real.

---

## 2. Continuous Condition Scoring Trained on Economic Outcomes
#cnns #semantic-segmentation #object-detection #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #worker-facing

**Problem statement:** Condition is the dominant price variable, is assigned by human graders under quota with unmeasured variance, and is recorded as a coarse band that discards the information the platform most needs. Two items in the same band can differ by a factor of two in realised value.

**ML task:** Continuous condition scoring from photographs with defect detection and localisation, trained against realised price and return rate rather than against the human grade
**Input data:** Intake photographs; assigned grades; defect annotations where they exist; realised prices controlling for style and brand; return events with reasons; buyer complaints about condition; duplicated gradings across graders where collected.
**Target:** A continuous condition score calibrated so that it explains price variation within a style, and localised defects.
**Evaluation metric:** Variance in realised price explained within style-and-brand groups, compared against the human grade band — a direct test of whether the score carries more information than the rubric. Return rate prediction is the second metric and the operationally important one, since condition-driven returns are the expensive failure.
**Scope:** Training against economic outcomes rather than against the rubric is the key move: it sidesteps human grading inconsistency entirely by using labels that are abundant, objective and directly aligned with what the platform cares about. Human grades become a weak prior rather than the target. Defect localisation supports both the grader assist and the buyer-facing listing, where showing a defect precisely reduces returns. 2-3 ML engineers, 5 months.
**Data availability:** Photographs and outcomes are abundant. Deliberate duplicated grading for variance measurement does not exist and costs a small fraction of intake capacity to generate.

---

## 3. Authentication Triage by Anomaly Against Genuine References
#cnns #contrastive-learning #object-detection #confidence-intervals #evaluation-metrics #bayesian-inference #hypothesis-testing #compliance

**Problem statement:** Authentication is scarce expert judgement made under time pressure against an adversary that improves specifically in response to whatever is being checked. Volume grows faster than authenticators can be trained, and reference knowledge decays continuously.

**ML task:** Fine-grained anomaly detection against a corpus of confirmed genuine references, producing a triage decision and localised evidence rather than a verdict
**Input data:** Photographs and specialised imaging of confirmed genuine items across brands, models and production periods; confirmed counterfeits where available; authenticator decisions with reasoning; disputed cases and their resolutions; production period metadata; newly observed counterfeit tells.
**Target:** Deviation from the genuine reference distribution for this model and period, with the specific regions driving it.
**Evaluation metric:** For triage, the proportion of volume that can be cleared automatically at a false accept rate the business will tolerate — which should be extremely low, since a false accept is a guaranteed financial loss and a reputational one. Report false reject rate separately at the operating point, since rejecting genuine items has its own serious cost that a single accuracy figure hides.
**Scope:** Anomaly detection against genuine rather than classification against counterfeit is the correct formulation, because the counterfeit class is small, non-stationary and adversarially adapted — a classifier trained on today's counterfeits degrades precisely as counterfeiters respond. Continuous re-validation is therefore mandatory rather than optional. The output is evidence for an authenticator, never an autonomous rejection, both because the error costs are severe and because the seller conversation requires articulable reasoning. 3 ML engineers plus authentication experts, 7 months.
**Data availability:** Genuine reference imagery is abundant at scale platforms. Confirmed counterfeits are far scarcer and are precisely the class that cannot be relied on, which reinforces the anomaly formulation.

---

## 4. Automated Item Identification at Intake
#cnns #object-detection #bert #k-nearest-neighbors #transfer-learning #evaluation-metrics #confidence-intervals #automation

**Problem statement:** Intake processors identify brand, style, category, colour and size for hundreds of items a shift under quota, alongside the condition and authenticity judgements that genuinely need a person. Identification is mechanical, error-prone at pace, and determines whether an item is findable at all.

**ML task:** Multimodal identification from photographs and label imagery — brand, category, style, colour, material and size — with confidence-gated routing to a human
**Input data:** Intake photographs including label and tag close-ups; historical confirmed identifications with subsequent corrections; brand and style catalogues; size chart conventions by brand; processor corrections and their patterns; downstream findability and sale outcomes.
**Target:** Confirmed item identification as corrected by processors and validated by sale outcomes.
**Evaluation metric:** Per-field accuracy with brand and size weighted highest, since those are what buyers filter on and a wrong size is a guaranteed return. The operational metric is processing time saved per item at a fixed accuracy threshold, since the whole point is returning quota headroom to the judgement tasks.
**Scope:** Label text is the strongest signal where present and absent on a meaningful share of secondhand goods, which is exactly where identification is hardest and where human product knowledge currently carries the work. Confidence gating is essential: the system should identify what it can and route the rest, rather than guessing at a rate that pollutes the catalogue. Closing the feedback loop — connecting returns and realised prices back to the processor who made the call — requires no modelling and is the single most requested thing by the people doing the work. 2 ML engineers, 4 months.
**Data availability:** Millions of photographs paired with confirmed identifications, which is an unusually strong supervised dataset. Label close-ups are captured inconsistently and are worth standardising.
