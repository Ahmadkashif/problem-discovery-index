# Machine Learning Opportunities — Online Marketplaces

**Industry:** [[online-marketplaces|Online Marketplaces]]
**Derived from:** [[problems/online-marketplaces/high-impact|High Impact]], [[problems/online-marketplaces/low-impact-1|Low Impact 1]], [[problems/online-marketplaces/low-impact-2|Low Impact 2]], [[problems/online-marketplaces/worker-life-1|Worker Life 1]], [[problems/online-marketplaces/worker-life-2|Worker Life 2]]

---

## 1. Attribute Extraction and Similarity for One-of-a-Kind Inventory
#cnns #contrastive-learning #bert #word-embeddings #dimensionality-reduction #k-nearest-neighbors #evaluation-metrics #revenue-impact

**Problem statement:** Every listing on a unique-inventory marketplace is a permanent cold start — one unit, no behavioural history, described by an amateur, gone when it sells. Collaborative filtering has nothing to work with and content signals depend on content sellers produced badly, which is why matching fails exactly where these marketplaces are most valuable.

**ML task:** Multimodal attribute extraction from listing images and text, plus learned similarity between items that never co-occur in behavioural data
**Input data:** Listing images, titles, descriptions and seller-entered attributes; category assignments; sale outcomes and time to sale; buyer browse and consideration sequences within sessions; historical listings with confirmed attributes from returns, authentication or seller correction.
**Target:** Structured attributes — category, brand, size, condition, material, era, style — and an embedding where proximity predicts that the same buyer would consider both items.
**Evaluation metric:** For attributes, precision per field weighted by how much each drives search and filtering, with brand and size weighted highest since they are the fields buyers actually filter on. For similarity, whether items placed close together were in fact considered together by the same buyers in held-out sessions — a direct behavioural validation that needs no human labelling.
**Scope:** Images carry more reliable signal than amateur titles and are systematically underused; this is the central design point. Similarity learned from co-consideration within sessions is what survives when items themselves never repeat, and it is the mechanism that makes recommendation possible on transient inventory. Condition assessment from photographs is the hardest attribute and the most commercially valuable in resale categories. 3 ML engineers, 6 months.
**Data availability:** Listing images and text are abundant. Confirmed attribute labels are scarce and come from indirect sources — authentication outcomes, return reasons, seller corrections — which makes weak supervision the practical approach.

---

## 2. Unmet Demand Measurement and Temporal Matching
#evaluation-metrics #hypothesis-testing #confidence-intervals #k-nearest-neighbors #gradient-boosting #time-series-forecasting #descriptive-statistics

**Problem statement:** Searches returning nothing acceptable and listings expiring unsold are recorded as absence rather than as signal, so the marketplace measures conversion on the transactions that happened and is blind to the demand it failed to serve. Supply is also transient — a listing that would have suited last week's buyer appears today and nothing connects them.

**ML task:** Classifying search and browse sessions as unmet demand, characterising what was wanted, and matching later supply to earlier intent
**Input data:** Search queries with result sets and downstream engagement; browse sessions ending without engagement; listings that expired unsold with their attributes and price; buyer session histories; the attribute embedding space; time between intent and matching supply appearing.
**Target:** A characterised unmet demand signal — what was sought, in what attribute region, at what price — and a later listing that satisfies it.
**Evaluation metric:** Conversion on temporally matched reconnections against the platform's baseline re-engagement rate, which is the direct business test. For demand characterisation, whether predicted unmet demand regions subsequently show high sell-through when supply arrives — a validation that runs automatically over time.
**Scope:** Distinguishing genuine unmet demand from casual browsing is the classification problem and matters because acting on the latter produces spam. Temporal matching must be opt-out rather than opt-in to be useful, which raises real notification-fatigue questions that should be designed around rather than ignored. Unmet demand aggregated by attribute region is directly actionable for supply acquisition and is the output most marketplaces would benefit from first. 2 ML engineers, 5 months.
**Data availability:** Search and session logs are complete and retained. Expired listings are usually retained. The join between an early unmet intent and a later matching listing does not exist and is the thing being built.

---

## 3. Pre-Publication Listing Success Prediction
#gradient-boosting #cnns #bert #confidence-intervals #evaluation-metrics #hypothesis-testing #feature-engineering #worker-facing

**Problem statement:** New sellers produce their worst listings during the window in which they decide whether the marketplace works. The platform can predict which listings will sell and can attribute the shortfall to fixable causes, and tells sellers generic best practice instead.

**ML task:** Predicting sale probability and time to sale from listing attributes, images, price and category before publication, with attribution to specific fixable factors
**Input data:** Historical listings with images, titles, descriptions, attributes, price and category; sale outcomes and time to sale; image quality measures; category-level attribute importance; seller tenure and history; comparable listing outcomes.
**Target:** Probability of sale within a horizon, and the marginal effect of each fixable listing attribute.
**Evaluation metric:** Calibration of the sale probability, since the seller-facing claim is a prediction they will check against reality. For attribution, the measured improvement when a seller acts on a specific recommendation — testable directly by comparing outcomes for listings edited on advice against comparable ones that were not, which is the only honest validation of the guidance.
**Scope:** The feedback must be specific and category-aware to be worth anything — telling a seller that listings without a brand field sell at half the rate in this category is actionable, while telling them photographs matter is not. Pricing guidance for unique items is the hardest component, since comparables are thin, and the honest output is a range with stated uncertainty rather than a number. Image quality assessment and automated enhancement are available technology and should ship before any modelling. 2 ML engineers, 4-5 months.
**Data availability:** Excellent. Listings, images and outcomes are complete, and the relationship between listing quality and sale outcome is exactly what these platforms have the most of.

---

## 4. Enforcement Consistency and Policy Gap Detection
#bert #large-language-models #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #compliance

**Problem statement:** Trust and safety reviewers decide the cases automation declined, which means every case is genuinely ambiguous and policies do not cover the edges. Inconsistency between reviewers is unmeasured, and the queue's most valuable output — knowledge of exactly where the rules fail — has no route to the people who write them.

**ML task:** Measuring inter-reviewer disagreement and clustering it against policy language, plus false-positive prediction on enforcement actions
**Input data:** Enforcement decisions with reviewer, case content, policy category and outcome; appeals and their overturn outcomes; deliberately duplicated cases sent to multiple reviewers; policy document text and versions; seller history and tenure; enforcement volume by category over time.
**Target:** Disagreement clusters mapped to policy clauses, and the probability that a given enforcement action will be overturned on appeal.
**Evaluation metric:** For policy gap detection, the reduction in disagreement and overturn rate after a flagged clause is clarified — the intervention is the test. For false-positive prediction, precision at a review threshold, since the use is triggering proactive review of likely errors before the seller has to appeal, and a false alarm costs a reviewer's time while a miss costs a livelihood.
**Scope:** Deliberate case duplication is the measurement instrument and costs a small percentage of review capacity, which is why it is not done and why consistency is currently unknown. Enforcement sweep monitoring — detecting a spike in suspensions or overturn rate in a category — requires no modelling and catches misfiring rules in hours rather than weeks. Proactive false positive review for long-tenured sellers caught by new rules is the highest-value single application. 2 ML engineers plus a policy specialist, 5 months.
**Data availability:** Decisions and appeals are logged completely. Duplicated cases for consistency measurement do not exist and must be generated deliberately.
