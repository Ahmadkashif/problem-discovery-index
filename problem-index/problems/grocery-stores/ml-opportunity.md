# Machine Learning Opportunities — Grocery Stores

**Industry:** [[grocery-stores|Grocery Stores]]
**Derived from:** [[problems/grocery-stores/high-impact|High Impact]], [[problems/grocery-stores/low-impact-1|Low Impact 1]], [[problems/grocery-stores/low-impact-2|Low Impact 2]], [[problems/grocery-stores/worker-life-1|Worker Life 1]], [[problems/grocery-stores/worker-life-2|Worker Life 2]]

---

## 1. Learning the Fresh Manager's Read of Product Condition
#tacit-knowledge-ml #cnns #transfer-learning #survival-analysis #gradient-boosting #worker-facing #revenue-impact

**Problem statement:** Experienced produce, meat and bakery managers look at a case or a display and "know" how many days it will sell before it must be culled or marked down. The ML problem is to capture that read from photos taken on the handheld at receiving and on the floor, join it to what happened to each lot, and predict remaining sellable days per lot so the order, rotation and markdown can use it.

**ML task:** Image regression and ordinal classification of ripeness and defect grade per case or display, feeding a survival model of time-to-cull per lot conditioned on grade, item, supplier, temperature history, day of week and promotion
**Input data:** Handheld photos of cases at receiving and of displays during the morning walk; receiving records (item, supplier, lot, quantity, date); cull and markdown scans with reason and weight; daily item sales; cooler temperature logs; promotion calendar; weather.
**Target:** Ripeness and defect grade per photo, using the manager's own grading vocabulary; days from receipt to sale-out, markdown or cull per lot, with sale-out treated as censoring of the cull event.
**Evaluation metric:** For grades, agreement with held-out manager labels, reported against the managers' own test-retest agreement as the ceiling. For shelf life, concordance index and calibration of predicted days-to-cull on lots held out by time and store. Under-predicting shelf life costs margin through needless markdowns; over-predicting costs culls and empty displays. Report both errors in dollars per department per week, not one blended score.
**Scope:** The data collection challenge is the project. The expert's read must be captured as they do the task, so photo capture has to take two seconds on a device already in their hand, and cull logging has to be a scan and a tap at the scale. The labelling challenge is that managers disagree with themselves: the same case is graded harder after a bad weekend. A sample must be re-graded blind to estimate intra- and inter-rater reliability, and the survival outcome, not the grade, is the final arbiter. The deployment challenge is speed: the shelf-life estimate must be on the screen while the manager writes the order and walks the display, and it must explain itself ("this lot graded 2 days riper than last week's") or it will be overridden. 2 ML engineers and 1 field product lead embedded with 10 to 20 stores, 6–9 months, with value appearing first as better rotation and markdown timing before any order is changed.
**Data availability:** Sales, receiving and promotion data are clean at any chain. Cull data is thin or absent and must be built prospectively. Photos do not exist and must be collected; public produce-quality image sets (fruit freshness datasets on Kaggle) help pretraining but not the chain's own suppliers and lighting.

---

## 2. Fresh Demand Forecasting With Censored Sales and Graded Overrides
#time-series-forecasting #gradient-boosting #temporal-fusion-transformers #bayesian-inference #evaluation-metrics #revenue-impact

**Problem statement:** Forecast store-item-day demand for fresh items whose sales are capped by what was on the shelf, and learn which manager overrides of the suggested order improved on the forecast, so the order engine absorbs the good overrides and flags the bad ones.

**ML task:** Probabilistic (quantile) demand forecasting at store-item-day with stockout censoring correction, plus override attribution: did this override, with this stated reason, beat the forecast on realised demand and shrink?
**Input data:** Item-store daily sales and on-hand history; stockout and low-stock flags from shelf scans or zero-sales runs; orders, suggested orders and overrides with reason codes; promotions and ad placement; price; weather; local events; holidays; cull and markdown records.
**Target:** Demand quantiles per item-store-day; for each override, the counterfactual shrink and lost sales under the suggested order versus the placed order.
**Evaluation metric:** Weighted pinball loss on demand quantiles against the chain's current forecast, on held-out weeks, with stockout days handled by a censored likelihood rather than dropped. The business metric is shrink dollars and estimated lost sales together, because a forecast that cuts shrink by emptying shelves has only moved the loss. Override attribution reports the share of overrides, by reason and manager, that beat the forecast, with confidence intervals; small samples per manager are the norm.
**Scope:** The forecasting itself is well-trodden and vendors (Afresh, RELEX, Crisp/Shelf Engine) already sell it. The differentiated part is override capture and grading, which depends on reason codes nobody records today. 2 data scientists and 1 engineer, 4–6 months for a chain pilot.
**Data availability:** Sales and orders are internal and clean. True demand is censored and must be modelled. Override reasons must be captured going forward.

---

## 3. Markdown Timing and Depth for Short-Dated Fresh
#causal-inference #markov-decision-processes #dynamic-programming #bayesian-inference #gradient-boosting #revenue-impact

**Problem statement:** For each lot approaching its sell-by date, choose whether, when and how deep to mark it down, or to divert it to the deli, a surplus app or a food bank, to maximise recovered margin net of cannibalising full-price sales.

**ML task:** Price-elasticity estimation for markdowns by item, store and days-to-expiry, with a sequential decision policy over the remaining days
**Input data:** Markdown history (depth, timing, label method), sell-through after markdown, full-price sales of the same item that day, days-to-expiry at markdown, lot condition grades from entry 1, electronic shelf label price changes where present, surplus-app and donation outcomes.
**Target:** Units sold at each markdown depth and day; cannibalised full-price units; final disposition of each lot.
**Evaluation metric:** Recovered margin per marked-down lot net of cannibalisation, measured in store-matched tests, because observational markdown data is confounded (managers mark down what was not selling). Waste weight is reported alongside, since a policy that recovers margin by sending less to food banks may break a sustainability target.
**Scope:** Electronic shelf labels make dynamic markdowns possible but are not in most stores, so the first version prints labels on a schedule. Causal estimation needs randomised depth tests across stores, which a chain must agree to run. 1–2 data scientists, 4 months, with test design as much of the work as modelling.
**Data availability:** Markdown transactions are recorded at the POS when a markdown label is scanned. Depth and timing decisions are not recorded with their reasons, and donated or culled units are weighed only in stores with a programme.

---

## 4. State-by-State SNAP and WIC Item Eligibility Classification
#large-language-models #bert #transformers #decision-trees #compliance #automation

**Problem statement:** Classify every item in a chain's file, including private label and store-made items, as eligible or ineligible under each state's SNAP restriction waiver and each WIC Authorized Product List, and route the borderline items to a human with the reasoning recorded.

**ML task:** Multi-label text-and-attribute classification (item description, ingredients, nutrition panel, category) against rule definitions extracted from each waiver's text, with rules applied where attributes are decisive and a language model where they are not
**Input data:** The chain's item file with descriptions, categories, brand and size; GS1 and syndicated product attributes (ingredients, sugar, juice percentage, flour content); state waiver texts and FNS guidance; state WIC APL files; a labelled set of reviewed items.
**Target:** Eligible or ineligible per item per state programme, plus a confidence and the rule clause relied on.
**Evaluation metric:** Precision and recall per state against compliance-reviewed labels. Wrongly blocking an eligible item embarrasses a customer and loses a basket; wrongly allowing an ineligible one is a violation against the store's authorisation. Report both counts, and the share of the item file auto-classified at a confidence where reviewers agreed 99% of the time.
**Scope:** Waiver definitions are short but ambiguous ("candy" defined by flour content, "soft drink" covering flavoured water). The model must cite the clause and handle effective dates that a court can reverse. 1 ML engineer and 1 compliance analyst, 3 months to a first state, then weeks per state.
**Data availability:** Item files are internal. Attribute coverage is good for national brands and poor for private label and store-made items. Waiver texts are public. Labels come from the chain's own review decisions.

---

## 5. Missed-Scan Detection at Self-Checkout With Calibrated Alerts
#cnns #object-detection #transformers #evaluation-metrics #worker-facing #automation

**Problem statement:** Detect items moved from cart to bag without a matching scan at self-checkout, and alert the attendant only when confidence is high enough that an approach to the customer is justified.

**ML task:** Object detection and tracking of items across scan zone and bagging area in overhead video, matched against the POS scan stream, producing an event-level missed-scan probability
**Input data:** Overhead camera video per lane; POS scan log with timestamps; weight-scale events; attendant intervention outcomes (rescanned, honest error, no issue found, customer left).
**Target:** Per-event label: scanned, missed and recovered, missed and not recovered, false alarm.
**Evaluation metric:** Precision at the alert threshold, because each false alert sends an attendant to accuse an honest customer. Recall on high-value missed items is secondary but reported. The operational metric is recovered value per attendant hour against false approaches per hour.
**Scope:** Vendors already sell this. The open problem is calibration per store and lane, and using attendant outcomes as labels without the bias of only labelling flagged events. 2 ML engineers, 6 months, with privacy review of in-store video.
**Data availability:** Video and scan logs exist at stores that have deployed vision; outcome labels exist only where attendants record what they found.
