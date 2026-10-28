# Machine Learning Opportunities — Parking Operators

**Industry:** [[parking-operators|Parking Operators]]
**Derived from:** [[problems/parking-operators/high-impact|High Impact]], [[problems/parking-operators/low-impact-1|Low Impact 1]], [[problems/parking-operators/low-impact-2|Low Impact 2]], [[problems/parking-operators/worker-life-1|Worker Life 1]], [[problems/parking-operators/worker-life-2|Worker Life 2]]

---

## 1. Learning the Area Manager's Read of Demand
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #time-series-forecasting #feature-engineering #revenue-impact #worker-facing

**Problem statement:** Experienced area managers set transient, event and monthly-oversell decisions from a read of fill patterns, events and competitor prices that they cannot fully explain, and that read leaves with them. The ML problem is to learn it from their logged rate decisions, the reasons they give and what happened next, and offer it to the next manager as a forecast and a recommendation with a track record.

**ML task:** Imitation of rate decisions (predict the manager's chosen rate and reason given the facility's state) plus probabilistic hourly occupancy forecasting conditioned on the chosen rate, with a hierarchical Bayesian layer that shares strength across facilities and managers
**Input data:** PARCS entry and exit events per facility (5–15 minute bins); rate-change history across PARCS, app and marketplace channels; one-tap reasons and expected fill logged by managers; event calendars (venues, conventions, games); weather; competitor rates scraped from marketplace listings; monthly-account counts and Friday show-up rates.
**Target:** The manager's rate decision and reason category; occupancy and revenue per available space by hour; and the gap between the manager's stated expectation and the outcome.
**Evaluation metric:** For forecasts, pinball loss at the 10th, 50th and 90th percentiles and the share of event days where the facility hit "full" within ±20 minutes of the forecast, measured strictly out of time by season. For recommendations, the estimated RevPAS lift against the manager's own decisions on held-out days, with the manager's test–retest consistency (the same event priced months apart) as the ceiling. Under-forecasting fill on event days costs more than over-forecasting: a sold-out deck at a $25 rate leaves the most money on the table.
**Scope:** The data-collection challenge comes first: the read happens on a sidewalk, so capture has to be a phone tap at the moment of the rate change, with the event, the competitor price and the fill curve pre-filled for the manager to confirm. The labelling challenge is that revenue is a confounded label, because managers raise rates when they expect demand. Counterfactuals need nearby comparable facilities, any owner-approved rate tests, and repeated logging of the same event type to measure how much a manager disagrees with themselves. The deployment challenge is that recommendations must reach the manager's phone before they drive past the garage, for twenty facilities at once, and must respect each contract's rate approvals and caps. Team: 2 ML engineers and 1 data engineer embedded with one operator's region, 6–9 months, with value showing first as a shared rate ledger before any model is trusted.
**Data availability:** PARCS and channel data sit with the operator, but at managed sites the revenue is the owner's, so use needs the owner's consent under each contract. Manager reasons do not exist yet and must be captured going forward. Competitor rates are public on marketplace listings.

---

## 2. Hourly Occupancy Forecast and Rate Recommender on City Open Data
#time-series-forecasting #temporal-fusion-transformers #gradient-boosting #causal-inference #evaluation-metrics #quick-win #revenue-impact

**Problem statement:** Forecast hourly paid occupancy for every blockface and recommend the rate step that keeps it inside the city's target band, using public meter data, and estimate drivers' price response from the city's own scheduled rate changes. This is the two-week MVP, and it transfers directly to off-street facilities once an operator's PARCS data replaces the meters.

**ML task:** Multi-horizon probabilistic forecasting (hour ahead to week ahead) per blockface, plus price-elasticity estimation using scheduled rate changes as natural experiments, plus a rule-constrained rate recommender
**Input data:** Seattle's "Paid Parking Occupancy (Last 30 Days)" feed (per-minute paid occupancy and space count by blockface; 13.4 million rows on 2026-10-28) and annual files back to 2012; Seattle's paid-parking transaction feed (amount, duration, payment means); SFMTA's block-level rate-change spreadsheets (±$0.25 about every quarter, raising above 80% and lowering below 60%; latest change 2026-07-13); event calendars and weather.
**Target:** Paid occupancy per blockface-hour; the effect of a $0.25 or $0.50 rate step on occupancy and revenue; and the recommended rate.
**Evaluation metric:** Weighted MAPE and interval coverage on held-out weeks against a seasonal-naive baseline; the share of blockface-hours in the target band (70–85% in Seattle, search summary; 60–80% in San Francisco) under the recommended rates in simulation; elasticity estimates checked against before and after windows around SFMTA's published changes. Over-pricing a block into emptiness costs local businesses; under-pricing costs circling and revenue. Report both.
**Scope:** Week one: ingest the Seattle feed, build hourly panels, train a LightGBM baseline and a temporal fusion transformer, and report coverage. Week two: estimate elasticities from rate-change events with difference-in-differences across treated and untreated blocks, then wrap the forecasts in the city's own band rules to produce a rate recommendation per block. Pair it with an open-source plate detector and OCR model on a small set of entry and exit images to show how gate events become parking sessions with entry time, exit time and dwell. Keep images synthetic or consented, and delete plates after the session is matched. One engineer, two weeks.
**Data availability:** Public and live. Paid occupancy is inferred from payments, so permit, placard and unpaid parkers are missing, a known bias to report. Off-street PARCS data needs an operator partner.

---

## 3. Revenue Leakage Detection Across Managed Facilities
#autoencoders #gaussian-mixture-models #change-point-detection #feature-engineering #evaluation-metrics #compliance #automation

**Problem statement:** Detect cashier, shift and facility patterns that signal lost or diverted revenue (excess voids, lost-ticket waivers, gate raises, validations redeemed above invoices, marketplace bookings without exits) before the owner's audit finds them.

**ML task:** Unsupervised anomaly scoring on shift-level transaction profiles, plus change-point detection on facility revenue against entries
**Input data:** PARCS transactions with void, override and lost-ticket codes by cashier and lane; intercom gate-raise logs; validation redemptions and invoices; marketplace payout files; monthly cards issued and billed; deposits and card settlements; staffing schedules.
**Target:** An anomaly score per cashier-shift and per facility-month, and a list of the transactions that drive it.
**Evaluation metric:** Precision in the top 1% of flagged shifts against cases confirmed by revenue-control investigators. Investigator time per confirmed case is the operating cost, so precision at the top matters more than recall. Track dollars recovered per investigator-hour.
**Scope:** Labels are scarce, so the system starts unsupervised and learns from investigators' confirmed and dismissed flags. Shift profiles need per-facility normalisation for event days and seasons. 1 data scientist and 1 engineer, 4 months for one operator's region.
**Data availability:** Held by the operator. At managed facilities the transactions are the owner's revenue records, usable for the owner's own audit; pooling across owners needs contract permission.

---

## 4. Plate Reads, Session Matching and Misread Risk Before a Notice Is Mailed
#cnns #object-detection #transformers #logistic-regression #evaluation-metrics #compliance #automation

**Problem statement:** At gateless facilities, turn entry and exit images into parking sessions and estimate, for each unpaid session, the probability that the plate read or the entry–exit match is wrong, so that no notice is mailed on a misread and every notice passes the state's rules.

**ML task:** Plate detection and character recognition (detector plus sequence OCR), entry–exit matching with read confidence, and a calibrated misread-risk classifier that gates notice creation
**Input data:** Entry and exit camera images at the operator's own facilities; payment records (app, kiosk, marketplace, monthly); confirmed disputes and their outcomes; lot-level metadata (state, signage audit, whether plate recognition is permitted there).
**Target:** Session records (entry time, exit time, dwell, paid or unpaid) and a misread probability per unpaid session.
**Evaluation metric:** Character-level and plate-level accuracy by lighting and plate type; for notices, the share of notices voided on dispute because of a misread or mismatch, with a hard ceiling. A wrongful notice costs a dispute, possible statutory damages and the owner's goodwill; a missed unpaid session costs one fee. Operate at high precision.
**Scope:** Restrict the model to matching sessions inside one facility. Never link a plate across facilities or owners, and delete images on the retention schedule each state and contract sets. Check plate-recognition rules per state before deployment: Maine applies its ALPR prohibition to lots open to the public, subject to that statute's exceptions. 2 ML engineers, 4–5 months; much of the work is calibrating confidence on hard cases (temporary tags, dirty plates, motorcycles).
**Data availability:** Images are captured at the operator's sites under its contracts with owners. Dispute outcomes are logged by notice processors and are the best supervised signal.

---

## 5. Valet Handoff Damage Comparison
#cnns #semantic-segmentation #contrastive-learning #transfer-learning #worker-facing #quick-win

**Problem statement:** Compare fixed-camera images of a car at valet drop-off and at return, panel by panel, and flag damage that appeared in between, so claims are settled on evidence rather than on the runner's word.

**ML task:** Vehicle panel segmentation, damage detection, and change detection between paired image sets under different lighting
**Input data:** Paired drop-off and return images from fixed stand cameras, linked to claim tickets; historical claims with outcomes; public vehicle-damage image sets for pre-training.
**Target:** Per-panel "new damage" flags with location and a confidence score; a handoff condition record per car.
**Evaluation metric:** Recall on new damage confirmed by adjusters at a false-alarm rate under ~1 per 200 cars, because every false alarm costs a captain's inspection on a busy night. Report the share of contested claims resolved from images.
**Scope:** Pre-train on public damage images, then fine-tune on stand footage; rain, reflections and night lighting are the hard cases. 1 ML engineer, 3–4 months per camera layout.
**Data availability:** Operators hold claims histories; stand images do not exist until cameras are installed, so the first months are collection.
