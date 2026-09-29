# Machine Learning Opportunities — D2C Brand Operators

**Industry:** [[d2c-brand-operators|D2C Brand Operators]]
**Derived from:** [[problems/d2c-brand-operators/high-impact|High Impact]], [[problems/d2c-brand-operators/low-impact-1|Low Impact 1]], [[problems/d2c-brand-operators/low-impact-2|Low Impact 2]], [[problems/d2c-brand-operators/worker-life-1|Worker Life 1]], [[problems/d2c-brand-operators/worker-life-2|Worker Life 2]]

---

## 1. Experiment-Calibrated Media Mix Modelling
#causal-inference #bayesian-inference #time-series-forecasting #hypothesis-testing #confidence-intervals #linear-regression #evaluation-metrics #revenue-impact

**Problem statement:** Platform-reported conversions exceed actual orders, every channel claims the same purchases, and budget moves weekly on numbers everyone knows are unreliable. Media mix modelling is the right statistical answer and is under-identified on observational data where spend across channels moves together in response to the same conditions.

**ML task:** Bayesian media mix modelling with adstock and saturation, calibrated on incrementality experiments that provide causal anchors for individual channel effects
**Input data:** Spend by channel and date; the brand's own order and revenue data as ground truth; geographic and cohort-level holdout experiment results; seasonality, promotions and product launches; competitor and category signals where available; post-purchase survey responses; platform-reported conversions as a weak prior rather than as truth.
**Target:** Incremental revenue attributable to each channel, with the uncertainty that the data actually supports.
**Evaluation metric:** Out-of-sample prediction of total revenue under held-out spend patterns, and — the metric that matters — agreement between model-estimated channel effects and the results of incrementality tests reserved for validation. A model that disagrees with a clean geographic holdout is wrong regardless of how well it fits history.
**Scope:** Experiment calibration is the entire contribution: unconstrained mix models fitted to correlated spend recover the brand's own budgeting policy rather than the demand response, which is why practitioners distrust them. A programme of small, continuously running geographic or cohort holdouts is cheap, and the obstacle is operational friction rather than cost. Report intervals honestly and widen them where identification is weak — a false point estimate is what the current tooling already provides. 2-3 ML engineers plus a marketing scientist, 6 months.
**Data availability:** Order data is complete and is the ground truth nobody else has. Spend data is accessible by API. Experiment data does not exist and must be generated deliberately, which is the prerequisite and the cultural obstacle.

---

## 2. Creative Attribute Attribution and Fatigue Prediction
#cnns #diffusion-models #gradient-boosting #evaluation-metrics #hypothesis-testing #confidence-intervals #time-series-forecasting #revenue-impact

**Problem statement:** Creative is the dominant performance variable in paid social and brands test it by launching and watching. An asset differs from another in many ways at once, so performance is known per asset and never attributed to the attributes that caused it — which means each expensive test produces no transferable learning.

**ML task:** Automatic attribute tagging of creative assets, attribution of performance to attributes rather than to assets, and decay curve prediction for fatigue
**Input data:** Creative assets with their impression, click and conversion performance over time; automatically extracted attributes — hook type, framing, colour palette, pacing, talent presence, text overlay, format, message category; frequency and audience reach; placement; historical decay curves; category-level performance across brands where a vendor or agency has that view.
**Target:** Marginal performance contribution per creative attribute, and time to fatigue for an asset given its early performance.
**Evaluation metric:** Whether attribute-informed creative batches outperform intuition-selected ones on held-out launches — a direct test the brand can run. For fatigue, prediction accuracy on time to a defined performance decay threshold, evaluated against the current practice of running assets until someone notices.
**Scope:** Automatic attribute extraction is the enabling step and is now straightforward for video and static creative; manual tagging was the reason this was never done. Attribution is confounded because assets are not randomly assigned budget by the platform's own optimiser, which allocates toward early winners — this needs explicit handling or the model learns the optimiser's behaviour. Cross-brand pattern data is available to tooling vendors and agencies and inaccessible to individual brands, which shapes who can build this well. 2 ML engineers, 5 months.
**Data availability:** Asset performance data is complete in the ad platforms. Attribute tags do not exist and are generated. Cross-brand data requires an agency or vendor vantage point.

---

## 3. Joint Inventory and Acquisition Spend Planning
#time-series-forecasting #gradient-boosting #optimization-fundamentals #confidence-intervals #evaluation-metrics #exponential-smoothing #convex-optimization

**Problem statement:** Inventory is committed months ahead against a forecast that is last year plus a growth assumption, ignoring the brand's main demand lever — marketing spend. Inventory and acquisition compete for the same working capital and are planned separately, which is how brands end up with stock they cannot afford to advertise.

**ML task:** Demand forecasting with marketing spend as a controllable input, at product-attribute level for items without history, feeding a joint working capital allocation
**Input data:** Historical sales by product, size, colour and channel; marketing spend by channel and date; product attributes including category, price point and comparable prior launches; lead times and minimum order quantities; return rates by product; markdown history; cash position and financing terms.
**Target:** Demand by product and variant under a given spend plan, and the joint inventory and spend allocation maximising contribution subject to a cash constraint.
**Evaluation metric:** Forecast quantile accuracy rather than mean, because the cost of being wrong is asymmetric and differs by product — a stockout on a hero product and excess on a slow one are not equivalent errors. For the joint plan, realised contribution margin against the brand's own planning as baseline, evaluated over a full season.
**Scope:** Size and colour distribution is where excess actually accumulates and is usually treated as a fixed ratio rather than forecast, which is a straightforward and neglected improvement. New product forecasting must run on attributes and comparable launches rather than on history, since that is exactly when there is none and when the buying risk is highest. The joint optimisation is the genuinely novel piece and requires the demand model to be responsive to spend, which is why the two cannot be built separately. 2-3 ML engineers plus a merchandise planner, 6 months.
**Data availability:** Sales, spend and inventory data are all present in the brand's own systems. Returns are frequently tracked poorly at variant level, which matters because return rate varies enormously by size and colour.

---

## 4. Proactive Delivery Exception Detection
#time-series-forecasting #gradient-boosting #change-point-detection #confidence-intervals #evaluation-metrics #large-language-models #automation

**Problem statement:** Order status is the dominant support contact type and almost none of it needs a person. Customers contact support because tracking has not updated and they want a human to interpret it, and volume spikes exactly when a carrier or region is failing — producing hundreds of identical contacts about a single cause.

**ML task:** Predicting delivery date from carrier scan history at lane level, detecting shipments that have stalled, and clustering exceptions into incidents
**Input data:** Carrier scan events per shipment; historical transit times by carrier, origin, destination and service level; weather and known disruption events; order and product characteristics; support contact history joined to shipments; delivery outcomes and exception resolutions.
**Target:** Actual delivery date, and whether a shipment will require intervention.
**Evaluation metric:** Calibration of the delivery estimate — a promise the brand makes to a customer must be one it keeps at the stated rate — and, operationally, the reduction in inbound status contacts per thousand orders after proactive communication is introduced. Incident detection is measured on lead time before contact volume spikes.
**Scope:** Lane-level transit prediction from the brand's own shipment history substantially outperforms the carrier's published estimate, which is a generic national figure, and most delivery disappointment is a promise problem rather than a delivery problem. Incident clustering — recognising that four hundred stalled shipments share a facility or a region — turns hundreds of individual apologies into one communication with a remedy. 2 ML engineers, 4 months.
**Data availability:** Scan events are available through carrier APIs and aggregators. Historical shipment outcomes are complete. Support contacts are usually not joined to shipments, which is the integration that makes the contact-reduction measurement possible.
