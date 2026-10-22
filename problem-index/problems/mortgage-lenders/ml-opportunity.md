# Machine Learning Opportunities — Mortgage Lenders

**Industry:** [[mortgage-lenders|Mortgage Lenders]]
**Derived from:** [[problems/mortgage-lenders/high-impact|High Impact]], [[problems/mortgage-lenders/low-impact-1|Low Impact 1]], [[problems/mortgage-lenders/low-impact-2|Low Impact 2]], [[problems/mortgage-lenders/worker-life-1|Worker Life 1]], [[problems/mortgage-lenders/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Underwriter's Income Read
#tacit-knowledge-ml #gradient-boosting #large-language-models #transformers #survival-analysis #evaluation-metrics #feature-engineering #compliance

**Problem statement:** Senior underwriters read a self-employed borrower's returns, a stack of paystubs or a bank-statement history and "know" when a qualifying income will not hold or a document is not what it seems, a judgement the Selling Guide leaves to them and the defect data says is where losses sit. The ML problem is to learn that read from their historical flags and conditions and the later outcome, and surface it as a pointed second read on the next file.

**ML task:** Document-level flagging of income evidence (trend break, deposit-to-revenue mismatch, document-integrity concern, unstable income type) plus a calibrated probability that the loan draws an income-related critical QC finding, agency defect notice or early payment default within 12 months
**Input data:** Income worksheets and Form 1084 cash-flow analyses; the documents themselves (returns, K-1s, paystubs, W-2s, bank statements, written verifications, IRS transcripts); conditions issued and cleared with timestamps; underwriter notes and letters of explanation; AUS findings; prefunding and post-closing QC findings with severity; agency defect notices and resolutions; payment history for the first 12 months; underwriter identity and tenure.
**Target:** Flag labels mirroring the senior underwriters' vocabulary; binary income-defect or early-default outcome at 12 months; agreement between model and senior underwriter on held-out files.
**Evaluation metric:** Recall on income-related critical defects at a fixed review budget (flags on no more than ~10–15% of files), because a missed defect costs ~$32,000 in a buyback and a false flag costs minutes. Calibration (Brier score) of the outcome probability, measured out of time across a rate-cycle change, since files from a refinance boom differ from a purchase market. For the flags, agreement with senior underwriters reported against their own test-retest agreement on re-presented files as the ceiling.
**Scope:** The data collection challenge comes first: the expert's doubt must be captured as they review, so the system needs a near-zero-effort way for senior underwriters to tag what they noticed while they work, plus reconstruction of historical doubts from conditions and notes. The labelling challenge is that QC findings are themselves judgement calls, repurchases are rare (~0.24–0.49% of loans) and selected by agency sampling, and underwriters treat the same evidence differently under turn-time pressure; repeated blind review of a sample is needed to measure intra-rater reliability, and outcomes should be modelled as time-to-event with censoring. The deployment challenge is speed and evidentiary risk: the flag must land before conditions are issued, point at the specific line, and be logged in a way the lender is comfortable producing in a repurchase dispute. 2 ML engineers, 1 senior underwriter seconded half-time and a QC lead, 9–12 months; value appears first as retrieval ("files like this with this deposit pattern, and what happened to them") before any score is trusted.
**Data availability:** Every lender holds its own files, conditions, QC findings and defect notices, but in separate systems with no common loan key beyond the loan number. A mid-size lender has a few thousand QC-reviewed files a year and only dozens of income defects, so pooled learning across lenders needs data-sharing terms that respect GLBA and FCRA; a QC outsourcer or LOS vendor is the natural pooling point.

---

## 2. Lock Pull-Through and Fallout Forecasting
#survival-analysis #gradient-boosting #logistic-regression #time-series-forecasting #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Forecast, for every locked loan, the probability and timing that it funds, falls out or renegotiates, so the secondary desk hedges the right share of the pipeline and prices lock extensions and renegotiations against real fallout risk rather than a stage-based table.

**ML task:** Time-to-event modelling with competing risks (fund, withdraw, deny, renegotiate) at loan level, aggregated into a pipeline pull-through forecast with uncertainty
**Input data:** Lock records (date, term, price, product, purpose), loan status history from the origination system, appraisal and condition milestones, the market rate move since lock against the loan's locked rate, loan officer and branch history, borrower credit and LTV bands, channel.
**Target:** Funded, withdrawn, denied or renegotiated, and days to each event.
**Evaluation metric:** Out-of-time calibration of the pipeline pull-through forecast by week, and hedge slippage attributable to forecast error compared with the incumbent stage-based table. Errors are asymmetric by market direction: overestimating pull-through when rates fall leaves the lender over-hedged as borrowers leave to relock elsewhere.
**Scope:** Well-understood statistics; the work is the data join between lock desk, origination system and hedge records. 1 data scientist and 1 engineer, 4 months; a hedge advisor serving dozens of lenders can build a pooled prior that a single lender cannot.
**Data availability:** Each lender holds its own lock and status history; hedge advisors and pricing engines hold the cross-lender view in de-identified form.

---

## 3. Risk-Ranked Discretionary QC Sampling
#random-forests #gradient-boosting #bayesian-inference #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** Choose which closed loans to review beyond the required random sample so that each month's discretionary selections find the most material defects, while keeping the random sample clean as an unbiased estimate of the defect rate.

**ML task:** Binary classification of critical-defect risk per closed loan, with selection optimised under a fixed review budget and a Bayesian estimate of the overall defect rate
**Input data:** Loan attributes and AUS findings; data-integrity signals (changes to income or assets after AUS submission, late conditions, overridden fraud-tool alerts); underwriter, processor, loan officer and branch; past QC findings with severity; agency defect notices.
**Target:** Critical defect found in full QC review (binary), by category.
**Evaluation metric:** Critical defects found per hundred discretionary reviews against rule-based selection, measured on randomly sampled loans to avoid only ever labelling what the model chose. Report the random-sample defect rate separately with its confidence interval, since the agencies rely on it.
**Scope:** A modest model; the discipline is keeping a random holdout so the model is not trained only on its own selections. 1 data scientist with QC, 3 months.
**Data availability:** QC platforms and outsourcers hold years of findings; agency defect notices are in the lender's portal history.

---

## 4. Income Document Extraction into Cash-Flow Analysis
#large-language-models #transformers #seq2seq #cnns #evaluation-metrics #automation #worker-facing

**Problem statement:** Read tax returns, K-1s, business returns, paystubs and bank statements and populate the lender's cash-flow analysis (Fannie Mae Form 1084 or equivalent) line by line, with every figure linked to its source and low-confidence cells flagged.

**ML task:** Layout-aware document extraction and schema mapping from IRS forms and payroll documents into worksheet fields, plus rule-based calculation
**Input data:** Scanned and native PDFs of personal and business returns, schedules, K-1s, W-2s, paystubs and bank statements; IRS transcripts for reconciliation; historical completed worksheets as supervised mapping examples.
**Target:** Populated worksheet fields with source references and confidence.
**Evaluation metric:** Field-level accuracy at the threshold where fields are accepted without review, and zero tolerance for silent errors: a confident wrong add-back is worse than a blank. Time from document upload to completed worksheet.
**Scope:** Standard forms are tractable; handwritten amendments, multi-entity borrowers and pass-through income are the hard tail. Commercial tools (Ocrolus, LoanBeam) cover much of it; the gap is mapping to the lender's own worksheet and overlays. 2 engineers, 4 months.
**Data availability:** Every lender holds completed worksheets paired with source documents, which is ideal supervision.

---

## 5. Warehouse Line Allocation and Dwell-Time Optimisation
#convex-optimization #time-series-forecasting #monte-carlo-methods #gradient-boosting #optimization-fundamentals #revenue-impact

**Problem statement:** Allocate each day's closings across warehouse lines to minimise net carry and haircut cash subject to each line's eligibility, sublimits and aging rules, using a per-loan forecast of days until investor purchase.

**ML task:** Dwell-time regression per loan feeding a constrained allocation optimisation, with Monte Carlo simulation of line usage under volume and exception scenarios
**Input data:** Funding and purchase dates by loan, product, investor, closing type, exception history, line terms and balances, daily closing schedule.
**Target:** Days from funding to purchase; daily line allocations.
**Evaluation metric:** Haircut cash and aged-loan count against treasury's manual allocation over the same months; forecast error on dwell by investor.
**Scope:** Small: 1 analyst-engineer, 3 months, once funding and purchase data are joined.
**Data availability:** Internal origination and warehouse bank data; line terms are in facility agreements.
