# Machine Learning Opportunities — Sales Finance Companies

**Industry:** [[sales-finance-companies|Sales Finance Companies]]
**Derived from:** [[problems/sales-finance-companies/high-impact|High Impact]], [[problems/sales-finance-companies/low-impact-1|Low Impact 1]], [[problems/sales-finance-companies/low-impact-2|Low Impact 2]], [[problems/sales-finance-companies/worker-life-1|Worker Life 1]], [[problems/sales-finance-companies/worker-life-2|Worker Life 2]]

---

## 1. Learning the Credit Buyer's Read
#tacit-knowledge-ml #gradient-boosting #large-language-models #survival-analysis #causal-inference #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Senior indirect credit analysts look at a dealer-submitted deal and recognise packed income, unsupported book values, straw-purchase shapes and dealers whose paper is drifting — and also borrowers the scorecard underrates. The ML problem is to learn those reads from the buyers' own decisions, counteroffers and cue labels joined to outcomes, and surface them to every analyst at decision time.

**ML task:** Multi-label cue classification on the deal file (income implausibility, collateral overstatement, identity or straw-buyer signals, structure risk) plus a time-to-early-default model conditioned on the deal, the dealer and the buyer's action, with reject inference for declined deals
**Input data:** Application and bureau attributes; the deal as submitted and as resubmitted through Dealertrack or RouteOne; VIN decode and the book value claimed; stipulations requested and received; the buyer's action, counter terms and reason codes; the dealer's recent submission and funding history; outcomes (first-payment and early payment default, 12-month performance, confirmed fraud, dealer buybacks); bureau-tracked outcomes for declined applicants where a permissible purpose exists.
**Target:** Cue labels in the senior buyers' vocabulary; probability and timing of early payment default; agreement between model and senior buyer on held-out files.
**Evaluation metric:** Out-of-time AUC and calibration for early default, reported separately for the manually decisioned slice where the read matters; cue-label agreement against senior buyers, benchmarked against each buyer's own test–retest agreement on re-presented files. Recall on fraud and early-default cues matters more than precision — a missed packed deal costs the advance, a false flag costs a stipulation — but false declines carry a dealer-relationship and fair lending cost, so approval-rate impact and disparate-impact ratios are reported for every release.
**Scope:** The data collection challenge comes first: the read must be captured while the buyer works, so the system drafts cue tags from the file and the buyer confirms with a click, and history is rebuilt by pairing past decisions with resubmissions and outcomes. The labelling challenge is that buyers disagree with themselves — tighter after a bad month, looser near volume targets — so a sample of files must be re-presented blind to measure intra-rater reliability, and outcomes exist only for deals the lender bought. The deployment challenge is speed and explanation: suggestions must appear inside the queue faster than the buyer's glance, and each must map to an adverse-action reason under Regulation B. 2 ML engineers, 1 credit risk modeller and a senior buyer seconded part-time, 6–9 months, starting with retrieval ("this dealer's last ten deals with this income pattern") before any classifier is trusted.
**Data availability:** Applications, decisions and outcomes are the lender's own and plentiful for any lender above a few thousand contracts a year. The cue labels do not exist and building them is most of the work. Declined-deal outcomes need bureau data under a permissible purpose and careful legal review.

---

## 2. Dealer Risk Graph
#graph-neural-networks #graph-theory #gradient-boosting #change-point-detection #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Fraud and early default cluster by dealer, by F&I manager and by networks of shared employers, phone numbers, addresses and co-borrowers that no single application reveals. Detect dealers and rings whose paper is deteriorating before the vintage shows it.

**ML task:** Graph-based link and node risk scoring across applicants, dealers, employers, contact points and vehicles, plus change-point detection on each dealer's submission profile
**Input data:** All applications submitted (funded and not), with entity-resolved identifiers; dealer and F&I manager identifiers; stated employers and incomes; VINs and claimed options; stipulation outcomes; early payment default, fraud confirmations and buyback history; consortium fraud signals where the lender participates.
**Target:** Dealer-level risk of elevated early default or fraud in the next 90 days; application-level ring membership.
**Evaluation metric:** Precision at the top of the dealer watch list (a dealer review team can examine perhaps twenty dealers a week, so the list must be right at the top), lead time over the vintage report, and dollars of early default avoided on dealers acted on. False accusations damage relationships, so every flag must show the evidence.
**Scope:** Entity resolution is half the work. 2 data scientists and 1 data engineer, 5–6 months; production depends on a dealer-risk team willing to act on the list.
**Data availability:** Internal application and outcome data; consortium data (Point Predictive and the bureaus' fraud products) on subscription. Confirmed-fraud labels are sparse and must be supplemented with early-default and buyback proxies.

---

## 3. Funding Package Verification
#transformers #large-language-models #cnns #object-detection #seq2seq #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Read every contract package in transit — retail installment contract, buyer's order, add-on contracts, stipulations, title documents — extract the terms, verify them against the approval, the state's rules and the dealer agreement, and return all defects at once.

**ML task:** Document classification, layout-aware field extraction, signature and initial detection, and rule evaluation over the extracted terms
**Input data:** eContracts and scanned paper packages; approval terms from the LOS; state RISC form libraries and fee caps; dealer agreement terms; historical funder kickback reasons as labels.
**Target:** Extracted, normalised terms; per-rule pass/fail with the rule cited; fund/kick-back recommendation.
**Evaluation metric:** Field accuracy at the threshold where packages clear without human review, and a zero-tolerance measure of silent errors (a funded package with an uncaught defect found in post-funding audit). Days-to-fund and kickback cycles per dealer are the operational metrics.
**Scope:** Extraction is buyable; the rules library per state and per dealer agreement is the build. 2 engineers and a funding subject-matter lead, 4–5 months for the lender's top states.
**Data availability:** Every funded package is archived with the funder's decisions, which supplies labels; state rules must be compiled and maintained.

---

## 4. Collections Treatment Uplift
#causal-inference #gradient-boosting #survival-analysis #markov-decision-processes #evaluation-metrics #worker-facing #compliance

**Problem statement:** Decide, for each delinquent account each day, which treatment — call, text, extension offer, due-date change, no contact — most reduces the chance of roll to repossession, not which account is most likely to pay anyway.

**ML task:** Uplift (heterogeneous treatment effect) modelling over contact and arrangement treatments, with time-to-cure survival outcomes and contact-frequency constraints
**Input data:** Servicing history, payment patterns, prior promises and arrangements, contact attempts and outcomes, pay-date signals, insurance status, collector notes; randomised or quasi-random variation in treatment from historical policy changes.
**Target:** Expected change in 60-day roll and repossession probability under each treatment.
**Evaluation metric:** Uplift measured in a held-out randomised test (Qini or uplift-at-k), not offline AUC of payment propensity — propensity models rank borrowers who would have paid without contact. Repossessions avoided per thousand accounts and complaint rates are the business metrics.
**Scope:** Requires a lender willing to randomise a slice of treatment for a quarter. 2 data scientists, 6 months to a first controlled test.
**Data availability:** Servicing data is internal and rich; treatment assignment has been policy-driven, so historical data is confounded and a test is needed.

---

## 5. Pool Loss and Recovery Forecasting for Warehouse and ABS
#markov-chains #time-series-forecasting #bayesian-inference #monte-carlo-methods #gradient-boosting #data-integration #evaluation-metrics

**Problem statement:** Forecast monthly delinquency roll rates, charge-offs and recovery proceeds for each warehouse pool and securitisation, so the lender sees trigger and excess-spread pressure months ahead and can show its banks and investors why.

**ML task:** Loan-level roll-rate transition modelling with vehicle-specific recovery value prediction, aggregated by Monte Carlo simulation to pool-level paths
**Input data:** Loan-level servicing history by month; vehicle VIN, age and mileage; wholesale price indices and auction results for repossessed units; macro series; deal and facility trigger definitions.
**Target:** Distribution of cumulative net loss, delinquency and trigger breach dates per pool.
**Evaluation metric:** Out-of-time accuracy of projected versus actual cumulative net loss at 6 and 12 months, and calibration of trigger-breach probabilities. Underestimating losses is the costly error.
**Scope:** 1–2 quantitative analysts, 4 months, reusable across facilities.
**Data availability:** Internal servicing and recovery data; public ABS-EE asset-level files for public deals across issuers give a benchmark panel.
