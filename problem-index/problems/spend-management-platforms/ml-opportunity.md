# Machine Learning Opportunities — Spend Management Platforms

**Industry:** [[spend-management-platforms|Spend Management Platforms]]
**Derived from:** [[problems/spend-management-platforms/high-impact|High Impact]], [[problems/spend-management-platforms/low-impact-1|Low Impact 1]], [[problems/spend-management-platforms/low-impact-2|Low Impact 2]], [[problems/spend-management-platforms/worker-life-1|Worker Life 1]], [[problems/spend-management-platforms/worker-life-2|Worker Life 2]]

---

## 1. Policy Grading and Novelty-Based Exception Routing
#gradient-boosting #k-means-clustering #k-nearest-neighbors #bert #confidence-intervals #evaluation-metrics #feature-engineering #automation

**Problem statement:** Spend rules generate exceptions, humans approve the overwhelming majority of them, and those judgements are stored as audit trail and used for nothing. The rules never change, reviewers learn to approve without reading, and the rare transaction that genuinely deserves attention arrives in the same queue at the same pace as the hundred that do not.

**ML task:** Per-rule outcome grading, threshold recommendation from approved-spend distributions, and novelty scoring to route only unfamiliar exceptions to humans
**Input data:** Every policy rule with its exception volume, approval rate and reviewer time; transaction context including merchant, amount, spender, department, timing and business circumstance; approval decisions with reviewer and latency; historical approved exceptions as a reference set; policies and exception behaviour across the platform's whole customer base.
**Target:** A cost-and-benefit assessment per rule; a recommended threshold with the supporting distribution; and a novelty score per exception.
**Evaluation metric:** For routing, the measure is the proportion of exceptions safely auto-approved at a fixed rate of missed problems, validated by post-hoc sampling of what was auto-approved — the control is preserved by sampling, not by review of everything, which is how mature control functions elsewhere already work. Rule grading needs no model metric at all: exception volume against approval rate is arithmetic, and a rule with a ninety-nine percent approval rate and four hundred monthly exceptions is a tax rather than a control.
**Scope:** Rule grading should ship first because it is trivial and immediately persuasive to a CFO who has never seen the numbers. Threshold recommendation gives the finance leader the justification that currently makes a policy change too expensive to bother pursuing. Cross-customer policy benchmarking — what a fifty-person software company's meal limit empirically should be — is available only to the platform and is currently guessed at by every customer independently. 2 ML engineers, 5 months.
**Data availability:** Complete and internal. Approval decisions with full context are recorded for audit reasons, which makes this one of the best-labelled judgement datasets in business software.

---

## 2. Spend Misuse Detection as a Rare-Event Problem
#gradient-boosting #k-means-clustering #autoencoders #graph-neural-networks #confidence-intervals #evaluation-metrics #feature-engineering #compliance

**Problem statement:** Genuine expense misuse is rare and looks nothing like a rule breach, so it does not fall out of exception review — a classifier trained naively on approval outcomes learns to approve everything, which is exactly what the humans already do. The specific patterns that matter are duplicates, splitting to stay under thresholds, personal spend concealed as business spend, and unusual vendor relationships.

**ML task:** Rare-event detection over transaction sequences with explicit pattern specifications, plus graph analysis of employee-vendor relationships
**Input data:** Full transaction histories per employee and department; receipt content and line items; timing and location; merchant identity and normalisation; submission and approval behaviour; vendor payment records; known confirmed misuse cases across the customer base.
**Target:** Ranked suspected misuse with the specific pattern named and the evidence attached.
**Evaluation metric:** Precision at the top of the ranking is the only metric that matters, because the output is an accusation about a named colleague and a false positive is genuinely costly to a working relationship. Recall is unmeasurable in the usual way since undetected misuse generates no label, so the honest evaluation is a deliberate audit of a random sample alongside the flagged set, which also produces the base rate nobody currently knows.
**Scope:** Several of the highest-value patterns need no learning: exact and near-duplicate submission, amounts clustering just under thresholds, and round-number splitting are deterministic detections that are simply not implemented as first-class checks. The graph component — employees with unusual concentration at a single small vendor — is where the genuinely serious cases live and is the part that needs real modelling. Output should always route to a human with the evidence shown, never to an automated consequence. 2 ML engineers, 5 months.
**Data availability:** Transaction and receipt data are complete. Confirmed misuse labels are scarce and scattered across customers, which argues for pattern specification over supervised learning as the primary approach.

---

## 3. GL Coding from Customer History with Cross-Chart Transfer
#bert #large-language-models #word-embeddings #k-nearest-neighbors #gradient-boosting #transfer-learning #evaluation-metrics #data-integration

**Problem statement:** Every transaction must be coded to an account, department, class and project in a chart of accounts unique to each customer, using rules that break on anything ambiguous, with the remainder coded by a controller at month end from memory.

**ML task:** Transaction-to-account classification trained on the customer's own ERP history, with semantic alignment across customers' charts of accounts enabling transfer to new customers
**Input data:** The customer's historical ERP journal entries with their coding, predating the platform; merchant identity, category, amount, spender, department and timing; receipt line items; chart of accounts names, hierarchies and descriptions across the customer base; controller corrections with reasoning where captured.
**Target:** A full coding assignment with confidence, and an aligned semantic identity for each account across customers.
**Evaluation metric:** Accuracy at the confidence threshold where coding posts without review, and the proportion of transactions requiring controller touch. The threshold must be set conservatively: a wrongly coded transaction that posts silently is discovered in an audit or a variance investigation months later, which costs far more than the review it avoided. Report accuracy separately for the long tail of rarely used accounts, where aggregate numbers hide the failures controllers actually notice.
**Scope:** The customer's pre-existing ERP history is a directly supervised training set for that customer's exact conventions and is usually ignored in favour of starting from rules and learning slowly from corrections. Cross-chart semantic alignment is what lets a new customer start informed by thousands of similar companies rather than from zero, and charts differ in naming far more than in meaning. Routing genuine ambiguity to the employee at the moment of spend, when they still remember what it was for, is a product change worth more than model accuracy. 2 ML engineers, 6 months.
**Data availability:** ERP history is available at onboarding with customer permission and is the single most valuable and most overlooked asset in implementation.

---

## 4. Cashflow Trajectory and Customer Distress Prediction
#gradient-boosting #survival-analysis #time-series-forecasting #change-point-detection #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Analysts extend card limits to companies with no meaningful credit file, from bank balances read off a chart, and learn whether they were right when the account reaches collections. Meanwhile the platform holds daily bank data and complete transaction detail for thousands of companies, which is a far earlier and richer signal than a balance decline.

**ML task:** Cashflow trajectory forecasting with survival modelling on customer failure, using spending pattern changes as leading indicators
**Input data:** Daily connected bank balances and flows; payment processor revenue where shared; payroll timing and size; full card transaction detail including vendor mix, renewal lapses and discretionary category behaviour; headcount proxies; funding events; industry; historical customers that failed, wound down or reached collections, with their full preceding data.
**Target:** Forecast runway and burn trajectory, and a hazard estimate for payment failure or wind-down.
**Evaluation metric:** Lead time at a fixed precision is the operative measure — a distress signal three weeks before a missed payment is worth far less than one four months out, when the limit can still be adjusted without precipitating the outcome. Backtest strictly by time and report the false positive cost honestly, since acting on a wrong distress signal by cutting a healthy customer's limit damages a good relationship and may cause the harm it predicted.
**Scope:** Spending pattern change is the signal nobody uses: vendor mix shifts, lapsed renewals and collapsing discretionary categories precede balance deterioration by months. Cross-customer base rates are the context an analyst most lacks when looking at a single company, and only the platform can supply them. Continuous limit adjustment within guardrails removes most of the request queue and makes limits responsive in both directions. The decision-outcome join is the precondition and gives the function its first ever accuracy measurement. 3 ML engineers, 7 months.
**Data availability:** Excellent and internal. Bank feeds, transactions and collections outcomes are all held; the join between limit decisions and eventual outcomes is the missing artefact.
