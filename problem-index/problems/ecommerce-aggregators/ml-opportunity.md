# Machine Learning Opportunities — Ecommerce Aggregators

**Industry:** [[ecommerce-aggregators|Ecommerce Aggregators]]
**Derived from:** [[problems/ecommerce-aggregators/high-impact|High Impact]], [[problems/ecommerce-aggregators/low-impact-1|Low Impact 1]], [[problems/ecommerce-aggregators/low-impact-2|Low Impact 2]], [[problems/ecommerce-aggregators/worker-life-1|Worker Life 1]], [[problems/ecommerce-aggregators/worker-life-2|Worker Life 2]]

---

## 1. Revenue Persistence Prediction from Realised Acquisitions
#survival-analysis #gradient-boosting #causal-inference #confidence-intervals #time-series-forecasting #hypothesis-testing #evaluation-metrics #revenue-impact

**Problem statement:** Aggregators paid multiples on trailing earnings for brands whose performance rested on supplier relationships, seller responsiveness and ranking momentum that did not transfer. The sector's contraction was an underwriting failure, and the training data for a better model — pre-acquisition characteristics paired with realised post-acquisition trajectories — was accumulating throughout.

**ML task:** Time-series regression on post-acquisition revenue trajectory, with survival framing for the probability of decline below a threshold within a horizon
**Input data:** Pre-acquisition sales, advertising, inventory, review and returns history; category competitive dynamics from public marketplace data; supplier concentration and contract terms; seller response time and review velocity patterns; product differentiation measures; acquisition price and terms; realised post-acquisition revenue by month; migration actions taken.
**Target:** Revenue trajectory relative to the trailing baseline at twelve, eighteen and twenty-four months.
**Evaluation metric:** Calibration of the predicted distribution rather than point accuracy, since the investment decision is about downside risk — a model that predicts the mean well and understates variance produces exactly the outcome the sector experienced. Report performance against the trailing-multiple heuristic, which is the incumbent method and a fair baseline.
**Scope:** Confounding by migration quality is severe and must be handled explicitly: a brand that declined may have been badly underwritten or badly migrated, and separating the two requires the migration actions as covariates. Selection bias is the second issue — sellers choose when to sell and the rational moment is at peak, so the trailing window systematically overstates the sustainable level, which is a modellable adjustment. Sample sizes are modest even at large aggregators, which argues for pooled industry data and against overfitting to one firm's history. 2-3 ML engineers plus an investment analyst, 6 months.
**Data availability:** Excellent within any aggregator that has made dozens of acquisitions, and it exists as deal files and financial reporting rather than as a dataset. Assembling it is the first task and is entirely internal.

---

## 2. Migration Step Impact Measurement
#change-point-detection #causal-inference #time-series-forecasting #hypothesis-testing #confidence-intervals #gradient-boosting #evaluation-metrics

**Problem statement:** Migration playbooks differ substantially between aggregators, which indicates nobody knows which steps matter. Every firm has dozens of prior migrations with different sequences and different outcomes, and treats the accumulated scar tissue as knowledge rather than analysing it.

**ML task:** Estimating the causal effect of each migration action on ranking and revenue, plus stockout risk forecasting across the transition window
**Input data:** Migration timelines with each action and its date — account transfer, listing changes, inventory relocation, advertising restructure, catalogue consolidation; daily ranking, sales, conversion and buy box data before and after; inventory positions and transfer durations; sales velocity; recovery trajectories after disturbances.
**Target:** Change in ranking and revenue attributable to each migration action, and inventory required to avoid a stockout across the transition.
**Evaluation metric:** For causal effects, out-of-sample prediction of post-migration disturbance magnitude on held-out migrations. For stockout avoidance, whether recommended buffer levels actually prevented stockouts at the stated confidence, which is directly checkable and is the single highest-value output.
**Scope:** Migrations are not randomised and steps co-occur, so honest estimation relies on natural variation in sequencing and timing across the portfolio, with results reported as candidate effects rather than as certainties. Stockout risk requires no causal machinery and delivers most of the immediate value: a stockout is the most damaging single event available to a marketplace ranking and the buffer is currently chosen by intuition. Recovery trajectory modelling tells a manager what to expect after a disturbance rather than prompting a panic increase in advertising spend. 2 ML engineers, 4-5 months.
**Data availability:** Migration timelines exist in project records of varying quality. Daily marketplace performance data is retained. The join between the two is the work.

---

## 3. Cross-Brand Product and Supplier Resolution
#bert #word-embeddings #k-nearest-neighbors #dbscan #cnns #evaluation-metrics #data-integration #optimization-fundamentals

**Problem statement:** Consolidated purchasing is the model's headline synergy and requires knowing which products across forty acquired catalogues are comparable, and which supplier records refer to the same factory. Both are unresolved, so consolidation happens only where the overlap is obvious.

**ML task:** Entity resolution over products and suppliers across heterogeneous acquired catalogues, plus specification comparison for substitutability
**Input data:** Product catalogues from acquired brands with titles, descriptions, images, specifications and packaging details; supplier records with names, addresses and contacts; supplier documents and specification sheets; purchase order history; freight and packaging records; demand cycles and minimum order quantities per brand.
**Target:** Product groups that are substitutable or share a plausible supplier base, and canonical supplier identities across trading company and factory names.
**Evaluation metric:** Precision on proposed product groupings judged by sourcing staff, weighted heavily since a wrong grouping leads to a purchasing decision that produces unsellable inventory. For suppliers, precision and recall on resolution against manually confirmed identities, where the hard cases are factories operating under multiple trading names.
**Scope:** Specification comparison is the hard half — two functionally identical products described differently by two sellers require reading supplier documents rather than matching catalogue fields, which makes this a document extraction problem before it is a matching one. Images carry substantial signal for physical goods and are always present. Joint order optimisation across brands with different demand cycles, minimum order quantities and cash constraints is a real optimisation problem that only becomes possible once resolution exists. 2-3 ML engineers plus a sourcing lead, 5-6 months.
**Data availability:** Catalogues and purchase history are held. Supplier specification documents sit in shared drives in inconsistent formats, which is the main obstacle and is entirely tractable.

---

## 4. Portfolio Drift Detection and Prioritisation
#change-point-detection #gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #evaluation-metrics #k-means-clustering #automation

**Problem statement:** A brand manager carrying a dozen brands attends to whatever is on fire while everything else declines a few per cent at a time. Rankings slip slowly, advertising efficiency degrades, and detection happens when drift becomes a crisis and recovery is expensive.

**ML task:** Per-listing and per-brand change detection against each entity's own baseline, with prioritisation by expected value and cross-portfolio correlation analysis
**Input data:** Daily ranking, sales, conversion, buy box share, advertising efficiency, review velocity and inventory position per listing; competitor pricing and listing changes; marketplace policy events; brand revenue and margin for value weighting; historical drift episodes and their eventual cost.
**Target:** A detected material change with its estimated revenue impact if unaddressed, and its likely cause.
**Evaluation metric:** Lead time between detection and the point at which the manager would otherwise have noticed — measurable against historical episodes — and the expected revenue protected per alert. Alert precision is the binding constraint, since a manager with twelve brands will ignore a noisy queue within a week.
**Scope:** Baselining per listing rather than against a global threshold is essential, because listings differ enormously in volatility and a fixed threshold produces constant noise on some and silence on others. Cross-portfolio correlation is the highest-value single feature: when several brands move together the cause is a marketplace change rather than twelve independent problems, and recognising that immediately saves days of separate investigation. Diagnosis alongside detection — naming the competitor price change or the suppressed image — is what makes an alert actionable rather than merely alarming. 2 ML engineers, 4 months.
**Data availability:** Marketplace performance data is pulled daily by every aggregator for reporting. Competitor data requires public marketplace collection. Historical drift episodes with their costs are rarely recorded and would need reconstruction.
