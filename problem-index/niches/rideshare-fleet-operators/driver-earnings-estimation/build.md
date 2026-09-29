# Build: Earnings Inference from Telematics and Payment History

**Niche:** [[niches/rideshare-fleet-operators/driver-earnings-estimation/profile|Driver Earnings Estimation]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Infer a driver's weekly earnings from how their vehicle moved, calibrated against the fleet's own record of who paid and who did not.
**Tags:** #gradient-boosting #time-series-forecasting #hidden-markov-models #confidence-intervals #evaluation-metrics #feature-engineering #survival-analysis #automation
**Contested on:** Whether payment behaviour is a strong enough label to calibrate an earnings model against.

## The Problem

The operator's central blind spot is the driver's income, and it has been treated as unknowable because the platform holds it. That framing misses what the operator does hold.

A rideshare vehicle's telematics trace is close to a direct record of the driver's working life: when they started, how long they were out, how much of that time was moving versus stationary, the geography they covered, trip counts inferable from stop-start patterns, and the daypart mix. Two drivers in the same market with the same vehicle and very different traces have very different incomes, and the difference is legible.

What converts that into an earnings estimate is the operator's own payment record. Across a few hundred drivers and a few years, the fleet knows who paid on time, who fell behind, who paid late but caught up, and who walked away — which is a noisy but real signal about whether earnings cleared the rental and by how much.

## Why Nobody Has Built This

Because "we can't see their earnings" ended the conversation. The available substitute — inference — requires thinking of the fleet as a lender with an underwriting problem rather than as a rental business with a collections problem, and that reframing has not happened in an industry run on spreadsheets by people who are also arranging repairs.

The label is also indirect and needs care. Payment behaviour reflects earnings and also reflects a driver's other obligations, their discipline, their household circumstances and how they prioritise the rental among competing bills. A model trained naively on payment outcomes learns a mixture of earnings and character, which is both less useful and considerably more legally fraught than an earnings estimate.

And the telematics vendors, who hold the cleanest version of the input, sell safety and utilisation products to fleets with employed drivers, where the driver's personal income is not a variable at all.

## What to Build

An earnings model with the trace as input and payment behaviour as a calibrated, carefully-handled label.

**Extract the working pattern.** Segment the telematics trace into on-shift and off-shift periods, and within a shift into moving-with-passenger, moving-empty and stationary. A state model over speed, stop duration and location type recovers this well enough without any platform data, and the three states have very different earnings implications. Aggregate to weekly: hours on shift, productive fraction, distance, daypart mix, geography.

**Model earnings per productive hour by market and conditions.** This is where external data earns its place: platform fare structures where published, incentive announcements, event calendars, weather, seasonality, and any public rate information. Combined with the working pattern, it produces a weekly earnings estimate with an interval — and the interval matters more than the point, because the whole purpose is to understand variance.

**Calibrate against payment outcomes carefully.** Use payment behaviour as a censored signal on whether earnings exceeded the rental plus the driver's other costs, not as a direct earnings label. Survival modelling on time-to-arrears with the earnings estimate as a covariate is the right structure: it validates the estimate without asking it to predict a person's character. Watch for and remove the pathways by which the model could learn to score the driver rather than the earnings, because that is both a worse model and a different, regulated product.

**Validate on what you can see.** Some drivers will share earnings screenshots or authorise data access voluntarily, particularly in exchange for a better rate. A few dozen such cases are enough to check calibration properly, and collecting them deliberately is the cheapest validation available.

**Report it as a market quantity as well as a driver one.** Expected earnings for a driver in this market working these hours is the number that prices the rate card; the per-driver version is the one that times an intervention. Both come from the same model.

## Target Customer

Fleet operators above the scale where a spreadsheet stops working, and the fleet management software vendors who serve them — for whom this is the module that turns an administration product into an underwriting one. Also the lenders financing fleets, who need the market-level version to underwrite the operator.

## Impact If Built

The operator's central blind spot closes using data they have been paying to collect for years. Rates get set against modelled earnings, interventions get timed before arrears rather than after, and market entry decisions get made on an earnings estimate rather than on where vehicles are cheap. And the fleet stops being a lender who cannot see the borrower's income.
