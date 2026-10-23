# Machine Learning Opportunities — Electrical Distributors

**Industry:** [[electrical-distributors|Electrical Distributors]]
**Derived from:** [[problems/electrical-distributors/high-impact|High Impact]], [[problems/electrical-distributors/low-impact-1|Low Impact 1]], [[problems/electrical-distributors/low-impact-2|Low Impact 2]], [[problems/electrical-distributors/worker-life-1|Worker Life 1]], [[problems/electrical-distributors/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Quoter's Completeness and Substitution Judgement
#tacit-knowledge-ml #large-language-models #transformers #object-detection #gradient-boosting #evaluation-metrics #revenue-impact #workflow-orchestration

**Problem statement:** Veteran quotation specialists read a plan set, a Division 26 specification and a contractor's partial list and "just know" what is missing, which equals the engineer will accept, and which lines will cause trouble after award. The ML problem is to learn those additions and substitution calls from the specialist's own edits and from later outcomes, and surface them to newer quoters on bid day.

**ML task:** Multi-label prediction of missing or inconsistent bill-of-materials lines given drawings, spec sections and the contractor's list; plus binary classification of substitution acceptability conditioned on spec language and the engineer's history
**Input data:** Drawing PDFs (panel schedules, one-line diagrams, fixture schedules, symbol legends), spec sections 26 05 00 onward with addenda, the contractor's original list, the quoter's edit trail (added, deleted, substituted lines with reasons), past submittal approvals and rejections by engineer, and post-award change orders and returns.
**Target:** Per-line probability that an item is required but missing; per-substitution probability of submittal approval; agreement with the quoter's final bill of materials.
**Evaluation metric:** Recall on lines the senior quoter added, at a precision the quoter will tolerate (a missed switchboard rating or transfer switch costs a change order; a false suggestion costs seconds), measured on held-out jobs split by time and by engineer. Substitution calls scored by AUC and calibration against actual submittal outcomes. Report model agreement against the quoters' own test-retest agreement on a re-quoted sample as the ceiling.
**Scope:** The data collection challenge comes first: the expert's reasoning has to be captured as they quote, so the quoting screen must log every edit to the contractor's list with a one-click reason and keep the drawing pages viewed, because historical quotes hold only the output. The labelling challenge is that experts disagree with themselves: the same veteran proposes an equal on a design-build job and refuses it on a hard-spec hospital, so a sample of jobs needs re-quoting by two seniors to measure agreement, and submittal outcomes arrive weeks later. The deployment challenge is speed: on bid day the suggestions must arrive in minutes with the source sheet or paragraph attached, faster than the veteran's own scan, or they are ignored. 2 ML engineers and a senior quoter as domain lead, 6–9 months, with value appearing first as drawing-schedule extraction and "items usually added on jobs like this" before any substitution classifier is trusted.
**Data availability:** Drawings and specs arrive with every bid request; the edit trail and reasons do not exist until the quoting workflow captures them. Submittal outcomes sit in email and the contractor's project platform and need joining by job.

---

## 2. Quote Win Probability and Price Response
#gradient-boosting #logistic-regression #causal-inference #survival-analysis #evaluation-metrics #revenue-impact

**Problem statement:** Given a project quote, estimate the probability it wins at each margin level, so the quoter sees the trade-off between price and win rate instead of guessing, and the distributor learns which contractors, engineers and package types it wins.

**ML task:** Binary classification with inferred labels, then price-response estimation corrected for the fact that margin is chosen by the quoter in response to perceived competition
**Input data:** Quote headers and lines (package type, value, margin by category, SPA coverage), contractor and engineer IDs, market and job type, number of contractors bidding when known, quote turnaround time, later orders and releases matched to the job name, and lead-data records of awarded contractors where licensed.
**Target:** Won/lost per quote, with won inferred from subsequent orders on the job and lost inferred from awards to other contractors or silence past the job's start date; time-to-award as a secondary target.
**Evaluation metric:** Brier score and calibration of win probability on quotes split by time, reported separately for quotes with confirmed versus inferred labels. For price response, the out-of-time margin realised on won jobs against the recommendation, with confidence intervals, since the quoter's own margin choice is confounded with how competitive the job looked.
**Scope:** The label problem is most of the work: matching orders to quotes by job name and ship-to is messy, and "unknown" must stay unknown rather than become "lost". 1 data scientist and 1 data engineer, 4–5 months to a calibrated model on a large distributor's history; smaller firms need pooled or synthetic priors.
**Data availability:** Quotes and orders are in the distributor's ERP; job-name matching needs cleaning. Award data can be licensed from the lead-data vendors profiled under [[electrical-contractors|Electrical Contractors]].

---

## 3. Gear Ship-Date Slip Forecasting
#survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #workflow-orchestration #data-integration

**Problem statement:** For every open purchase order line on long-lead gear, predict whether and by how much the manufacturer's promised ship date will move, early enough for the project manager to warn the contractor or substitute.

**ML task:** Time-to-event modelling of ship-date changes and final ship dates, with a binary early-warning classifier on top
**Input data:** Order acknowledgements and their revision history, ship notices, portal status snapshots, manufacturer, plant, product family and configuration, order size and options, season, the distributor's history of promised versus actual ship dates, and industry lead-time indices.
**Target:** Days of slip between first promised and actual ship date; probability of a further slip within the next 30 days.
**Evaluation metric:** Concordance and calibration of slip predictions on orders split by time; for the warning classifier, recall on slips over two weeks at a false-alarm rate the project manager will accept, since a missed switchboard slip costs the account and a false alarm costs a phone call.
**Scope:** Acknowledgement PDFs and portal pages need extraction before modelling. 1 ML engineer and 1 data engineer, 4 months for a first version on a distributor's top manufacturers; industry feeds such as IDEA's ProjectNexus would widen coverage.
**Data availability:** The distributor holds its own acknowledgements and ship history but rarely in structured form; promised-date revisions are often overwritten, so the history must be captured going forward.

---

## 4. Copper-Indexed Wire Pricing and Hold-Period Risk
#time-series-forecasting #exponential-smoothing #linear-regression #monte-carlo-methods #evaluation-metrics #revenue-impact

**Problem statement:** Set wire and cable quote prices and hold periods so that expected margin stays above floor given copper volatility over the hold window, and flag open quotes and unreleased orders whose margin has eroded.

**ML task:** Volatility forecasting of the copper reference over 1–30 day horizons, simulation of margin outcomes per quote, and regression of the manufacturer's price-sheet changes on copper moves
**Input data:** COMEX copper settlements, manufacturer price sheets and their effective dates, the distributor's reel costs and replacement costs, quote and order history with hold terms, release dates and realised margins, tariff changes.
**Target:** Distribution of margin at release for each open quote; recommended hold period and price per quote type.
**Evaluation metric:** Share of wire quotes and orders released below margin floor, and realised wire margin versus target, compared with the current manual practice over the same copper path; volatility forecasts scored by out-of-time log-likelihood.
**Scope:** Methods are standard; the work is in reconciling price-sheet timing, reel costs and project releases. 1 data scientist, 2–3 months.
**Data availability:** COMEX data is public; price sheets and reel costs are in the distributor's systems; hold terms are often unrecorded and must be captured.

---

## 5. SPA Claim Matching and Rejection Prediction
#k-nearest-neighbors #word-embeddings #logistic-regression #large-language-models #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Match every invoice line sold below standard cost to the SPA it belongs to, predict which 844 claim lines the manufacturer will reject on the 849, and route fixes before the claim window closes.

**ML task:** Entity matching of invoice lines to agreements (part aliasing, contractor and job matching), extraction of agreement terms from SPA documents, and binary classification of rejection risk by reason code
**Input data:** SPA documents and manufacturer portal exports, invoice lines with ship-to and job, IDEA part data for aliasing, historical 844 claims and 849 responses with reason codes, agreement expiries and quantity caps.
**Target:** Agreement match per line with confidence; rejection probability and most likely reason code per claim line.
**Evaluation metric:** Recovered SPA dollars per month and first-submission acceptance rate, against the current process on the same lines; rejection classifier scored by precision at the top of the review queue, since analysts can only work so many lines a day.
**Scope:** 1 ML engineer and a claims analyst as domain lead, 3–4 months; 849 histories provide supervised rejection labels directly.
**Data availability:** 844/849 histories and SPA records sit with the distributor and its EDI provider; agreement documents arrive as PDFs and portal pages.
