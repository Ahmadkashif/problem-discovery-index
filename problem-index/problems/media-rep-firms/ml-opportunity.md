# Machine Learning Opportunities — Media Representative Firms

**Industry:** [[media-rep-firms|Media Representative Firms]]
**Derived from:** [[problems/media-rep-firms/high-impact|High Impact]], [[problems/media-rep-firms/low-impact-1|Low Impact 1]], [[problems/media-rep-firms/low-impact-2|Low Impact 2]], [[problems/media-rep-firms/worker-life-1|Worker Life 1]], [[problems/media-rep-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior AE's Clearing-Price Read
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Senior rep account executives "read the market". They know what cost per point a buyer will accept for a station this week, when to hold rate and when to take the order, and they cannot write it down. The ML problem is to learn that read from the AE's own historical negotiations and their outcomes, so that every AE pricing the same stations can see what clears and what a senior colleague did in similar situations.

**ML task:** Conditional price-response modelling: a calibrated probability of order at each offered CPP (win curve) for a station × buyer × market × daypart mix × week-of-quarter, plus regression of the final clearing CPP and a time-to-order hazard
**Input data:** Avails requests (demo, dayparts, flight, budget, CPP goal), the station's proposals and every counter-offer with timestamps, from buying-system exports and email threads; final orders and rates from the traffic system; the station's sell-out level and pacing for the weeks requested; projected and posted ratings; buyer and agency-office identifiers; market-level share of each agency's spend from pooled revenue reports; the AE's confirmed floor and rationale where captured.
**Target:** Order or no order at the offered price; clearing CPP; days from request to order; and agreement between the model's suggested price and the senior AE's actual decision.
**Evaluation metric:** Calibration and log loss of the order-probability curve, measured strictly out of time by quarter. Revenue lift in counterfactual replay is reported with wide intervals, because price changes alter which buyers say yes. Agreement with held-out senior-AE decisions is reported against the AE's own consistency on near-duplicate requests, which is the ceiling. Errors are asymmetric: suggesting a price below what would have cleared gives away margin on every unit, while suggesting one above it loses one order. Report both, by station size.
**Scope:** The data collection challenge dominates. Proposals and counters must be reconstructed by joining agency exports, traffic orders and email, and going forward the AE's floor and reason need a near-zero-effort capture at the moment of decision. The labelling challenge is that outcomes are confounded by ratings, competitor pricing and client budget changes. Share labels arrive weeks later at market and agency level, not per order, and the same AE prices the same buyer differently in a soft first quarter and a political fourth quarter, so intra-rater consistency must be estimated on repeated cases. The deployment challenge is speed and firewalls: suggestions must appear inside the AE's proposal screen while the buyer waits, and models must be trained per division so competing stations' rates never cross. 2 ML engineers and 1 data engineer with a rep firm's sales operations team, 6–9 months. Value appears first as retrieval ("the last five times this buyer countered at this level") before any price suggestion is trusted.
**Data availability:** Orders and rates are in station traffic systems the rep can access for its clients. Proposals and counters are partly in agency buying-system exports and partly in email. The decisive asset, AE rationale tied to each decision, does not exist and has to be captured prospectively. Pooled revenue share is licensable by subscription.

---

## 2. Share-of-Buy Reconstruction from Partial Signals
#bayesian-inference #expectation-maximization #causal-inference #confidence-intervals #feature-engineering #revenue-impact

**Problem statement:** A station knows its own orders but not the full size of each agency's buy in its market. Pooled revenue reports give agency-level share monthly, and ad occurrence monitoring shows which advertisers aired where. Combine them to estimate each station's share of each campaign, and decompose changes in power ratio into ratings, pricing and allocation effects.

**ML task:** Latent-variable estimation of campaign-level market spend and station share, with hierarchical Bayesian decomposition of power-ratio change
**Input data:** The station's orders by advertiser and agency; market revenue share reports by agency and category; ad occurrence data by station and advertiser; ratings by daypart; the station's proposals and rates where available.
**Target:** Estimated market spend and station share per campaign; attribution of quarter-on-quarter power-ratio change to audience, price and allocation components.
**Evaluation metric:** Mean absolute error of share estimates against the subset of campaigns where agencies disclose the full buy, and coverage of credible intervals. A share estimate that is confidently wrong will be used in a renewal pitch, so interval honesty matters more than point accuracy.
**Scope:** 1 data scientist and 1 engineer, 4–5 months for one station group across its markets. Occurrence-to-spend conversion is the hardest step.
**Data availability:** Revenue reports and occurrence data are subscription products; their licence terms decide what can be combined. Station orders belong to the station.

---

## 3. Avails Request Extraction and Proposal Assembly
#large-language-models #transformers #seq2seq #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Turn free-form avails requests and revisions (emails, PDFs, spreadsheets in every agency office's layout) into a structured spec. Then assemble a priced proposal per station from traffic-system inventory and ratings projections, and turn revision emails into exact change lists.

**ML task:** Document and email information extraction into a fixed schema, plus schema mapping from agency daypart and program language to each station's inventory codes; change detection between order versions
**Input data:** Historical avails requests and the proposals assistants built from them; revision emails paired with the resulting order changes in traffic systems; station inventory and daypart code tables; ratings projections.
**Target:** Structured request fields (markets, demo, dayparts, weeks, lengths, budget, CPP goal); line-level change lists for revisions.
**Evaluation metric:** Field-level exact match, and line-level precision and recall on revisions, at the confidence threshold where output is applied without review. A silently wrong week or demo is worse than a field left for the assistant, so precision on auto-applied changes is the binding metric.
**Scope:** 2 engineers, 3–4 months. Historical request–proposal pairs give supervised examples per agency office. The long tail of odd layouts and ambiguous daypart language is the hard part.
**Data availability:** Every rep firm holds years of request emails and the resulting proposals; pairing them is a matching job, not a labelling one.

---

## 4. Spot-Level Ratings Forecasting for Guarantee Delivery and Makegoods
#gradient-boosting #time-series-forecasting #dynamic-programming #optimization-fundamentals #evaluation-metrics #automation

**Problem statement:** Forecast the rating each spot will deliver for the buyer's demo and choose placements and makegoods that meet the buy's guarantee with the least inventory given away, as ratings shift and preemptions arrive.

**ML task:** Probabilistic forecasting of program-by-week demo ratings, followed by constrained allocation of makegood and audience-deficiency units across remaining inventory
**Input data:** Historical ratings by program, daypart, week and demo under both Big Data + Panel and Panel-Only methodologies; preemption logs; the buy's guarantee and posted delivery to date; remaining inventory and its sell-out level.
**Target:** Delivered rating distribution per scheduled spot; a makegood plan that closes the delivery gap.
**Evaluation metric:** Pinball loss and interval coverage on delivered ratings; inventory value given away per point of under-delivery against the current manual practice. Under-forecasting causes unnecessary makegoods and over-forecasting causes deficiency claims later, so both tails are reported.
**Scope:** 1 data scientist and 1 engineer, 4 months. The January 2025 methodology change breaks the history for local ratings, so models must learn across both regimes.
**Data availability:** Ratings are licensed by stations and agencies; preemption and posting records sit in traffic systems and rep spreadsheets.

---

## 5. Political Demand Forecasting by Market and Week
#time-series-forecasting #bayesian-inference #gaussian-processes #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Forecast candidate, issue and PAC demand for each represented station by week ahead of an election, so issue-ad pricing and displacement of regular advertisers can be planned before inventory runs out.

**ML task:** Hierarchical forecasting of political spend by market × race type × week, with race competitiveness and fundraising as covariates
**Input data:** Prior cycles' political orders by station and week; FCC political file disclosures; race ratings and fundraising reports; ballot measures; current-cycle bookings to date.
**Target:** Weekly political spend per market and station, split candidate versus non-candidate.
**Evaluation metric:** Weighted absolute percentage error by week in the final 60 days, where the decisions are made, with interval coverage. Under-forecasting leaves issue inventory sold at regular rates, which is the costly error.
**Scope:** 1 data scientist, 3–4 months before a cycle. Only one even year in two yields training data, so cycles must be pooled across markets.
**Data availability:** The rep's own political orders across many stations are the asset; political file data is public but messy.
