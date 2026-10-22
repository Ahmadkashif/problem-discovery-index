# Machine Learning Opportunities — Pension Funds

**Industry:** [[pension-funds|Pension Funds]]
**Derived from:** [[problems/pension-funds/high-impact|High Impact]], [[problems/pension-funds/low-impact-1|Low Impact 1]], [[problems/pension-funds/low-impact-2|Low Impact 2]], [[problems/pension-funds/worker-life-1|Worker Life 1]], [[problems/pension-funds/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Investment Officer's Read of a GP
#tacit-knowledge-ml #large-language-models #gradient-boosting #survival-analysis #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced private markets officers read a GP's annual meeting, quarterly letters, capital account statements and LPAC conduct and "know" that a team is drifting, that marks are stale or that a key person is disengaging, often years before fund performance shows it. They cannot specify the read, and it leaves with them. The ML problem is to learn that read from the officers' own annotations and the eventual fund outcome, and surface it at the next re-up.

**ML task:** Multi-label classification of GP communications and statement histories into the officers' concern categories (key-person risk, style or size drift, stale marks, fee-term creep, governance friction), plus a calibrated probability that the next fund lands below the median of its vintage and strategy on a public-market-equivalent basis
**Input data:** Quarterly GP letters and annual meeting materials; capital account statements and cash-flow histories; the plan's re-up memos, annotations and meeting notes with dates; team-change disclosures; fund terms by vintage; eventual net IRR, TVPI and PME per fund; declined re-ups and their subsequent funds' outcomes from public pension disclosures.
**Target:** Concern labels in the officers' own vocabulary; next-fund relative performance band; agreement between model and officer.
**Evaluation metric:** Calibration (Brier score) of the next-fund probability, measured strictly by vintage so no future vintage informs a past one, and reported against a baseline that uses only the prior fund's interim IRR quartile. For the concern labels, agreement with held-out officer annotations, set against the officers' own test–retest agreement as the ceiling. Recall on deteriorating managers matters more than precision. A missed warning costs a ten-year commitment, while a false one costs an extra reference call.
**Scope:** Data collection is the hardest part. The officer's read has to be captured as they perform the task, which needs a near-zero-effort annotation surface during or right after GP meetings, plus back-annotation of historical memos aligned to the documents the officer saw. Labelling is hard because officers disagree with themselves: the same GP is read more harshly after a disappointment elsewhere in the programme. So labels need repeated annotation on a sample to measure intra-rater reliability, and outcomes must be vintage- and strategy-adjusted. Deployment is hard because the output must arrive inside the fundraising window and before the board packet closes, faster than the officer's own recall, and in a form a public board will not read as "the model said no". 2 ML engineers and 1 investment-domain lead embedded with a private markets team, 9–12 months. Value appears first as retrieval ("the last three times this GP's team changed, here is what happened") before any classifier is trusted.
**Data availability:** GP documents and cash flows are held by every LP, and fund-level outcomes for many funds are public through pension disclosures. The decisive asset, dated officer annotations, exists only in fragments and must be built. One plan makes too few commitments to train alone, so a multi-plan consortium or a vendor holding many LPs' documents is the realistic path, subject to GP confidentiality terms.

---

## 2. Capital Call and Distribution Forecasting for Commitment Pacing
#time-series-forecasting #monte-carlo-methods #bayesian-inference #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Forecast the private markets programme's capital calls, distributions and NAV by quarter under market scenarios, so the plan can set next year's commitment budget without the allocation breaching its policy range or forcing sales of liquid assets in a drawdown.

**ML task:** Fund-level probabilistic forecasting of contributions and distributions (hierarchical Bayesian extension of the Takahashi–Alexander model, conditioned on vintage, strategy, fund age, public-market path and GP-specific pacing), aggregated by Monte Carlo to programme level
**Input data:** The plan's own fund cash-flow histories; unfunded commitments; fund terms; public-market index paths; peer cash-flow benchmarks for vintage and strategy priors; the plan's liquidity needs (benefit payments, contributions).
**Target:** Quarterly calls, distributions and NAV per fund and in aggregate, with intervals; probability of breaching the policy range under each scenario.
**Evaluation metric:** Out-of-time pinball loss and interval coverage of quarterly aggregate net cash flow, plus accuracy of the breach probability. Under-forecasting calls in a drawdown is the costly error, because it forces sales at the bottom, so coverage of the downside tail matters more than the median.
**Scope:** Well-trodden statistics with a data problem. Fund histories are short and the 2020–2022 cycle is unlike earlier ones. 1 quantitative analyst and 1 engineer, 4–6 months to a model the investment committee can use.
**Data availability:** Each plan holds its own cash flows. Peer priors come from benchmark providers. Fund-level GP pacing behaviour needs the plan's full history across funds.

---

## 3. LPA Term Extraction and Fee and Carry Recompute
#large-language-models #transformers #seq2seq #feature-engineering #evaluation-metrics #compliance #automation

**Problem statement:** Turn each limited partnership agreement and side letter into executable fee and waterfall terms, recompute each quarter's management fee, offsets, expenses and carried interest from the capital account statement, and flag differences in dollars for the annual fee disclosure.

**ML task:** Clause extraction and normalisation into a fee-and-waterfall schema (sequence-to-structure), then deterministic recomputation with a learned reconciliation layer that classifies differences (timing, basis, offset, expense category, carry)
**Input data:** LPAs, amendments, side letters and MFN elections; quarterly capital account statements; capital call and distribution notices; ILPA reporting templates where GPs supply them.
**Target:** Structured terms per fund; recomputed fee, expense and carry amounts; classified variances with source citations.
**Evaluation metric:** Field-level accuracy of extracted terms against a lawyer-reviewed sample, weighted by dollar impact, and variance-detection recall on seeded and historical errors. A missed offset or premature carry is the costly miss; a false variance costs an analyst a query.
**Scope:** Extraction is tractable with current language models; the waterfall engine and the long tail of bespoke terms are the work. 2 engineers and a private funds specialist, 6 months for a programme of ~200 funds.
**Data availability:** Every LP holds its own documents. GP confidentiality clauses restrict pooling across LPs, so the model must work per plan.

---

## 4. Pensionable Pay Anomaly Detection in Employer Reports
#gradient-boosting #change-point-detection #k-means-clustering #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Flag, in the pay period they are reported, member pay records likely to be non-pensionable or mis-tiered: final-average-salary spikes, new or misused pay codes, leave cash-outs reported as base pay, and service days inconsistent with earnings.

**ML task:** Supervised classification of pay records against historical compensation-review and audit outcomes, combined with per-member change-point detection on earnings and clustering of employer pay-code vocabularies
**Input data:** Employer payroll submissions by pay period and pay code; member tier, bargaining unit and position; historical compensation reviews, audit findings and disallowed-compensation determinations; plan rules by tier.
**Target:** Probability that a pay record would be found non-compliant; flagged employer pay codes; member-level spike alerts in the final-average window.
**Evaluation metric:** Precision at the review capacity of the employer reporting team (records reviewable per period), with recall on historical disallowed-compensation cases as the second measure. Cost asymmetry favours recall near the final-average window, where errors become benefit cuts.
**Scope:** Labels exist where the system has run compensation reviews and audits, though they are sparse and skewed to the employers that were audited. 1 data scientist, 1 engineer and an employer-audit lead, 5 months.
**Data availability:** Fully held by the retirement system. Rules must be encoded by plan staff; audit outcomes need structuring.

---

## 5. Payee Change Fraud and Unreported Death Detection
#gradient-boosting #logistic-regression #graph-theory #evaluation-metrics #compliance #automation

**Problem statement:** Score every direct deposit, address and contact change, and every continuing payee, for the risk that the payment is being redirected by a fraudster or is going to a deceased payee, before the monthly payroll closes.

**ML task:** Binary classification of change requests, with features from a linkage graph of shared phone numbers, bank routing numbers, addresses and devices across members, plus a death-match confidence model combining external death records with payment and contact behaviour
**Input data:** Change-request logs with channel and timing; portal authentication events; bank account and routing data; prior contact history; external death-record matches; confirmed fraud and overpayment cases.
**Target:** Fraud probability per request; probability that a payee is deceased; clusters of linked suspicious requests.
**Evaluation metric:** Recall on confirmed redirection attempts at a fixed hold rate (the share of legitimate changes delayed), because both errors hurt a retiree. Report the false-hold rate on legitimate requests separately.
**Scope:** Fraud labels are rare, so the first version is rules plus anomaly scoring with clerk feedback. Cross-plan sharing of fraud indicators would multiply value. 1 data scientist and 1 engineer, 4 months.
**Data availability:** Change logs and payroll data are internal. Death data is licensed from vendors and limited-access federal files. Confirmed fraud cases are few per plan.
