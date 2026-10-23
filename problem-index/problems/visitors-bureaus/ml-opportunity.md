# Machine Learning Opportunities — Convention & Visitors Bureaus

**Industry:** [[visitors-bureaus|Convention & Visitors Bureaus]]
**Derived from:** [[problems/visitors-bureaus/high-impact|High Impact]], [[problems/visitors-bureaus/low-impact-1|Low Impact 1]], [[problems/visitors-bureaus/low-impact-2|Low Impact 2]], [[problems/visitors-bureaus/worker-life-1|Worker Life 1]], [[problems/visitors-bureaus/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Sales Director's Read of a Group's Pickup
#tacit-knowledge-ml #gradient-boosting #survival-analysis #logistic-regression #evaluation-metrics #feature-engineering #revenue-impact #worker-facing

**Problem statement:** Experienced convention sales directors "know" which leads will book, which groups will fill their blocks and which will book around them, and they set bid effort and incentive money on that read. The ML problem is to learn the read from the director's own dated forecasts and the realised outcome, and to give an equivalent forecast to the next director and to the funders.

**ML task:** Two linked models: time-to-decision survival model for lead and tentative conversion (booked, lost, still open), and regression of realised pickup as a share of contracted block, both calibrated and compared with the director's stated forecast
**Input data:** Destination CRM history (Simpleview CRM, iDSS): leads, stages, dates, lost reasons, competing cities; RFP text; the group's meeting history across cities from Knowland or MINT+; incentive offers; hotel block structure and rates; drive-in share from the attendee origin mix; rates at nearby non-contracted hotels and vacation rentals over the meeting dates; the director's confidence and expected pickup captured at the tentative stage.
**Target:** Booked or lost and when; realised pickup percentage from housing reports and, where groups agree, hotel actuals matched to registrations; attrition penalties triggered.
**Evaluation metric:** For conversion, concordance and Brier score out of time (train on earlier booking years, test on later). For pickup, mean absolute error on pickup share and calibration of the 80% interval, with the director's own forecast as the baseline the model must beat. Over-forecasting costs more than under-forecasting, because over-promised blocks lead to attrition penalties, lost repeat business and overstated KPIs, so report bias separately.
**Scope:** The data collection challenge comes first: the director's read has to be captured at the tentative stage, as they work, through a one-click confidence and expected-pickup prompt in the CRM, and past bids need their forecasts reconstructed from proposal notes. The labelling challenge is that pickup is fragmented across housing companies, hotels and outside-the-block bookings, and directors disagree with their own earlier ratings, so a sample of bids needs repeat rating to estimate intra-rater consistency. Outcomes also lag the decision by years. The deployment challenge is that the forecast must arrive before the incentive offer and the hotel blocks are committed, faster than the director can form a view, and inside a sales culture paid on booked room nights. 1 data scientist and 1 engineer with a CRM vendor or a group of 5-10 bureaus pooling data, 6-9 months to a first model. Value appears first as account history ("this group has picked up 72-78% of block in its last four cities") before any score is trusted.
**Data availability:** CRM histories exist at every sizeable bureau but are inconsistent across bureaus. Pickup data is the bottleneck: housing companies and hotels hold it, and most groups share it only under their own agreements. A pooled model across bureaus is the realistic route, because one bureau books too few citywides a year to train on.

---

## 2. Incremental Visitation From Destination Campaigns
#causal-inference #bayesian-inference #hypothesis-testing #time-series-forecasting #confidence-intervals #revenue-impact

**Problem statement:** Estimate how many overnight visits and how much visitor spending a leisure campaign caused, over and above what would have happened without it, instead of reporting exposed-visitor counts or survey-based return ratios.

**ML task:** Geo-experiment design and analysis (matched-market holdouts), with synthetic-control and Bayesian structural time-series estimates where holdouts are not possible
**Input data:** Campaign flight plans and spend by origin market and channel; location-panel visitor counts by origin (Placer.ai, Zartico, Datafy); card-spend by origin (Visa Spend Signals, Mastercard); hotel and vacation-rental demand (STR, AirDNA); hotel-tax receipts; event calendars and weather.
**Target:** Incremental visitor trips, room nights and spend per origin market per campaign flight, with intervals.
**Evaluation metric:** Placebo tests on non-campaign periods and markets (the estimator should find nothing where nothing happened); coverage of intervals in simulated lift experiments; and agreement between panel-based and hotel-based lift estimates. A bureau that reports a lift its own placebo test also "finds" has learned nothing.
**Scope:** The statistics are established; the hard parts are getting media buyers to hold out markets and getting enough origin-market granularity from the panels. 1 econometrician and 1 data engineer, 4-6 months for a first holdout campaign. Best built by an agency, a state tourism office or a data vendor that can run designs across many bureaus.
**Data availability:** Panel and card data are licensed per destination and can be re-cut by origin. Holdouts must be designed in; historical campaigns support only synthetic-control estimates with wide intervals.

---

## 3. Visitor Volume and Spend Nowcast From Conflicting Sources
#bayesian-inference #time-series-forecasting #maximum-likelihood-estimation #feature-engineering #data-integration #automation

**Problem statement:** Produce one monthly estimate of visitors, overnight stays and visitor spend, with uncertainty, by combining sources that each measure part of the picture with their own bias and lag.

**ML task:** Bayesian state-space data fusion: a latent visitor-volume series observed through several noisy, biased measurements, with source-specific bias and lag terms
**Input data:** Location-panel visitor counts and their panel sizes; card-spend totals and card-share assumptions; STR room nights; vacation-rental nights; hotel-tax collections (accurate but ~2-3 months late, estimate); airport passenger counts; visitor survey ratios (party size, spend per day).
**Target:** Monthly latent visitor volume and spend with intervals; source-level bias estimates.
**Evaluation metric:** Out-of-time error against hotel-tax-implied room nights once they arrive, the one source tied to audited money; interval coverage; stability of the estimate when one vendor's panel changes.
**Scope:** 1 statistician and 1 engineer, 3-4 months for one destination, mostly spent on source definitions. The output replaces the hand reconciliation in the monthly board report.
**Data availability:** All inputs are already licensed or public to the bureau. Panel methodology changes are rarely announced, which the model must detect as structural breaks.

---

## 4. RFP-to-Hotel Fit Ranking and Proposal Drafting
#large-language-models #word-embeddings #k-nearest-neighbors #logistic-regression #automation #workflow-orchestration

**Problem statement:** Rank partner hotels for each incoming RFP by likelihood of a competitive response and a win, deduplicate RFPs arriving by several routes, and draft the bid proposal from the hotels' actual responses.

**ML task:** Information extraction from RFPs, near-duplicate detection, and a response-and-win propensity model per hotel; text generation for the proposal
**Input data:** RFP documents and Cvent records; CRM lead history with hotel responses, rates quoted and outcomes; hotel meeting-space specs; hotel tentative holds where shared; past proposals.
**Target:** Structured RFP fields; duplicate clusters; probability each hotel responds and wins; draft proposal.
**Evaluation metric:** Extraction field accuracy; precision of duplicate detection (a false merge loses a real lead); top-3 recall of the hotel that eventually won; time from RFP to proposal sent.
**Scope:** 1-2 engineers, 3-4 months on top of a destination CRM. Bureau lead histories give hundreds to thousands of labelled routing decisions each.
**Data availability:** CRM data is the bureau's; hotel holds and displacement data are the hotels' and would be shared only through the extranet.

---

## 5. Hotel-Tax Receipts Forecasting and Remittance Anomalies
#time-series-forecasting #gradient-boosting #exponential-smoothing #change-point-detection #compliance #data-integration

**Problem statement:** Forecast hotel-tax and district-assessment collections a year ahead for the bureau's budget, and flag properties whose remittances diverge from their expected pattern.

**ML task:** Hierarchical time-series forecasting (destination, submarket, property type) with change-point detection on property-level remittance series
**Input data:** Monthly tax and assessment collections by property where the city shares them; STR submarket performance; vacation-rental supply and nights; convention-centre calendar; macro forecasts.
**Target:** Monthly collections with intervals; anomaly flags by remitter.
**Evaluation metric:** Mean absolute percentage error at 6 and 12 months, against the city budget office's own forecast; precision of anomaly flags confirmed by the city's audit staff.
**Scope:** 1 data scientist, 2-3 months. Most useful to large bureaus whose budgets are a fixed share of collections, and to district boards managing assessment income.
**Data availability:** Aggregate collections are often public; property-level data is confidential taxpayer information held by the city, so the anomaly half works only inside a city partnership.
