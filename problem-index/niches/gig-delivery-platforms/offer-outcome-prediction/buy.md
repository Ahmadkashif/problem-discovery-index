# Buy: ETA and Forecasting Stacks Repointed at the Courier's Question

**Niche:** [[niches/gig-delivery-platforms/offer-outcome-prediction/profile|Offer Outcome Prediction]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every platform already runs excellent ETA and readiness forecasting; it is aimed at the customer's promise and the dispatch decision, and answers a different question than the courier's.
**Tags:** #time-series-forecasting #gradient-boosting #evaluation-metrics #confidence-intervals #feature-engineering #data-integration #automation #recurrent-forecasting
**Contested on:** Whether forecasting infrastructure built to predict a delivery's arrival can be repointed at predicting a courier's engaged time and cost.

## The Problem

Delivery platforms have some of the best applied forecasting in commercial use. Customer ETA prediction, merchant readiness estimation, demand forecasting by geography and time, and supply positioning are all mature, continuously evaluated and genuinely good.

All of it answers questions posed by the customer promise and the dispatch decision. When will the food arrive. How many couriers should be in this zone at 7pm. When should this order be assigned. None of them is the courier's question, which is how long this specific job will occupy me and what it will cost me to do it — a different decomposition of largely the same underlying quantities.

## What Already Exists

In-house ETA stacks at every major platform, typically gradient-boosted or neural models over route, traffic, merchant and historical features, with strong serving infrastructure and continuous evaluation. Third-party routing and traffic services. Merchant readiness models driving dispatch timing. Demand forecasting for incentive allocation. Feature stores serving at real-time latency. The infrastructure is in place and performs.

## The Customization Gap

**The clock starts and stops in different places.** Customer ETA measures order placement to delivery. Courier engaged time measures acceptance to drop-off completion and includes segments the customer ETA either excludes or absorbs — the drive to the merchant, the wait, the parking, the walk into a building. Re-decomposing the existing models around the courier's interval is the core adaptation, and it changes which segments need their own model.

**The loss function is wrong for the purpose.** ETA models are typically trained to minimise average error, which is right for a customer promise. The courier's decision is dominated by the tail, and a model that is well calibrated on the mean can be badly calibrated at the 90th percentile. Quantile objectives rather than mean objectives, evaluated at the tail, is a retraining rather than a rebuild — but it is not what the existing model does.

**Cost is not in the stack at all.** No ETA model computes vehicle cost, because no customer-facing question requires it. Route distance is available from the routing layer; per-mile cost is a courier attribute that has to be captured and stored somewhere new. Small work, entirely absent.

**Merchant readiness is modelled for dispatch timing, not for disclosure.** The internal readiness prediction is tuned to decide when to send a courier, which makes systematic optimism relatively cheap internally and expensive to the courier who arrives early. Re-tuning for courier disclosure means a different operating point and a different calibration target on the same model.

**Building and address features need a home.** Handoff time by building type, parking availability, gated access and repeat-failure addresses are highly predictive of the tail and are not features in any current model, because they do not move the customer ETA much. Extracting them from GPS traces the platform already holds is the highest-value feature engineering available here, and it belongs to nobody's existing system.

## Target Customer

Platform ML teams who own the ETA and readiness stacks and are being asked for courier-facing estimates, and who need to know what is a retrain and what is a rebuild. Also the smaller regional and vertical delivery platforms buying routing and ETA services, for whom this defines the layer they still have to own.

## Impact If Solved

The existing forecasting investment gets a second consumer with different requirements, at a fraction of the cost of building fresh. In practice: the same models, re-decomposed around the courier's clock, trained at the quantiles that matter to them, with vehicle cost and building-handoff features added — which is a quarter of work rather than a year.
