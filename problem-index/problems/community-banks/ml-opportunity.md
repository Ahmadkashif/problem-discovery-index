# Machine Learning Opportunities — Community Banks

**Industry:** [[community-banks|Community Banks]]
**Derived from:** [[problems/community-banks/high-impact|High Impact]], [[problems/community-banks/low-impact-1|Low Impact 1]], [[problems/community-banks/low-impact-2|Low Impact 2]], [[problems/community-banks/worker-life-1|Worker Life 1]], [[problems/community-banks/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Credit Officer's Read of a Drifting Borrower
#tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #feature-engineering #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Senior credit officers at community banks read a borrower's returns, deposit behaviour and lender's notes and "know" a commercial credit is deteriorating quarters before the risk grade moves, a judgement they cannot specify and that leaves when they retire or the bank is sold. The ML problem is to predict migration of a pass-rated commercial loan to special mention or worse within the next 12 months, using the officer's own historical annotations as supervision alongside outcomes, and to explain each flag in the officer's terms.

**ML task:** Time-to-event modelling of grade migration (discrete-time survival with competing risks of payoff and refinance-away), plus gradient-boosted classification of 12-month migration and LLM-extracted features from memos and site-visit notes
**Input data:** Monthly core extracts per borrower relationship (operating account balances and volatility, line utilisation, overdrafts and NSF events, payment timing, returned ACH); spread history and covenant tests from the lending system; annual review dates and whether returns arrived on extension; credit memos, annual review narratives, loan committee minutes and site-visit notes; grade history with dates; collateral type and loan-to-value; industry and local economic series.
**Target:** Migration to special mention, substandard or worse; 60-day past-due; modification or troubled-borrower designation; charge-off. Secondary target: agreement with the senior officer's blind regrade of a historical sample.
**Evaluation metric:** Time-dependent concordance and recall at a fixed watch-list size (the top 5% of relationships by risk), measured strictly out of time. Lead time matters as much as accuracy: report the median number of months between the model's first flag and the actual downgrade. Recall on migrations outranks precision: a missed deterioration costs a charge-off, a false flag costs an analyst an hour. Report the officer's own test-retest agreement on regraded files as the ceiling for the annotation target.
**Scope:** The data collection challenge comes first: the officer's read has to be captured as they perform it, through a structured comment at annual review and loan committee that takes seconds, plus a one-off session in which the officer regrades a few hundred historical files blind and states the reason. The labelling challenge is that defaults are rare at any one bank, the officer disagrees with their own earlier grades, and loans the officer worried about were managed more closely, which biases naive training; intermediate events, repeated regrading and treatment of intervention as a censoring event address each in turn. The deployment challenge is that the flag must arrive between annual reviews, faster than the officer's own recall, with the specific signals shown, and must pass model risk review that a small bank cannot staff. 2 ML engineers and a credit-risk lead, 6–9 months for one bank; a vendor pooling 50+ banks under permissive contracts gets a usable default sample in a fraction of the time.
**Data availability:** Behavioural data sits in the core and is clean; spreads sit in the lending system; memos are unstructured documents. Officer annotations do not exist and must be created. Borrower and guarantor data is customer information under the Gramm-Leach-Bliley Act, so pooling across banks requires a vendor whose service agreements permit model training on de-identified data.

---

## 2. Entity-Aware Tax Return Extraction and Global Cash Flow
#large-language-models #transformers #graph-theory #seq2seq #evaluation-metrics #automation #data-integration

**Problem statement:** Extract line items from business and personal tax returns and their schedules, link every K-1 and related-party flow to the entity it belongs to, and assemble a borrower's global cash flow under the bank's credit policy without double counting.

**ML task:** Form-structured extraction (document layout model plus LLM schema mapping) followed by entity resolution across returns into an ownership-and-cash-flow graph
**Input data:** Forms 1120, 1120-S, 1065 and 1040 with all schedules and K-1s, often scanned; personal financial statements; prior-year spreads for the same borrower as supervised mapping examples; the bank's credit policy adjustments.
**Target:** Spread line items per entity with source links; an entity graph with ownership percentages, distributions and intercompany rents; global debt service coverage.
**Evaluation metric:** Field-level accuracy at the confidence threshold where values are written without review, and graph-level accuracy on ownership and flows. A silent error in a large figure is worse than a blank, so measure high-confidence errors separately. End-to-end: analyst minutes per complex borrower before and after.
**Scope:** Extraction of IRS forms is largely solved; the build is the entity graph and the policy layer. 2 engineers and a former credit analyst, 4–6 months; each bank's policy adjustments become configuration.
**Data availability:** Each bank holds years of returns and the spreads its analysts produced from them, a ready supervised corpus. Returns contain taxpayer data, so training stays inside the bank or with a processor permitted to use it.

---

## 3. BSA Alert Disposition Ranking and Narrative Drafting
#gradient-boosting #random-forests #graph-theory #large-language-models #evaluation-metrics #compliance #worker-facing

**Problem statement:** Rank transaction-monitoring alerts by probability that an investigator would escalate them to a case or SAR, and draft the disposition rationale for low-risk alerts, so a small BSA team spends its time where SARs come from.

**ML task:** Binary classification of alert outcome with calibrated probabilities, plus graph features over customers, accounts, counterparties and shared identifiers, plus LLM drafting of the disposition and SAR narrative
**Input data:** Alert records and their dispositions from the monitoring system; customer due diligence profiles and risk ratings; 12–24 months of transactions; prior SARs filed (internally only); counterparty and address links.
**Target:** Escalate versus close; for escalated alerts, SAR filed versus not.
**Evaluation metric:** Recall on alerts that became SARs at the volume of alerts the model would auto-prioritise to the bottom of the queue; a missed SAR is an examination and legal risk, a false escalation is an analyst's twenty minutes. Measure disposition-drafting quality as the share of drafts accepted without material edit. Examiners will test any automated closure, so the model ranks and drafts and a human decides.
**Scope:** A single bank's labels are few thousand a year; the signal is in the bank's own customers' seasonality, which a consortium model misses. 1 ML engineer and the BSA officer, 4–5 months, with a validation report the examiner can read.
**Data availability:** Dispositions sit in the monitoring system, often with thin rationales. SAR existence is confidential under the Bank Secrecy Act and cannot leave the bank, which keeps this an in-bank or vendor-hosted model.

---

## 4. Deposit Beta and Runoff Forecasting by Relationship
#bayesian-inference #survival-analysis #time-series-forecasting #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Forecast, by account and relationship, how much of each deposit balance will stay and at what rate when the policy rate moves, replacing the single portfolio-level decay and beta assumptions in the interest rate risk model with estimates the CFO can price against.

**ML task:** Hierarchical Bayesian estimation of deposit betas by product and segment, plus survival modelling of balance attrition conditional on rate gaps to competitors
**Input data:** Monthly account-level balances and rates from the core across at least one full rate cycle (2022–2025 is ideal); customer tenure, relationship breadth (loans, treasury services), account type; competitor rates from a benchmark service; the policy rate path.
**Target:** Balance retained and rate paid per account at 3, 6 and 12 months after a rate change.
**Evaluation metric:** Out-of-sample error in total deposit cost and balances over the 2022–2024 hiking period, held out and back-tested, compared with the assumptions the bank's ALM model actually used. Under-predicting runoff is the costly error.
**Scope:** The data is in the core and the method is standard; the hard part is getting account-level history out of the core vendor and reconciling product code changes. 1 data scientist, 3–4 months.
**Data availability:** Every bank holds its own history; benchmark vendors and ALM vendors hold pooled versions.

---

## 5. Product Matching for Core Conversions
#k-nearest-neighbors #large-language-models #word-embeddings #evaluation-metrics #data-integration #automation

**Problem statement:** Map each of an acquired bank's deposit and loan products, fee codes and GL accounts to the acquirer's equivalents by their economic behaviour, and identify the customers whose terms change enough to need notice.

**ML task:** Similarity matching over product parameter vectors and account-level behaviour, with LLM reading of product descriptions and disclosures to resolve ambiguous cases
**Input data:** Product parameter files from both cores (rate tiers, minimums, fee triggers, compounding, statement cycle); account-level balances and fee histories; disclosures; past conversion maps from the same vendor pair.
**Target:** Product-to-product mapping with confidence; per-account delta in fees and interest; notice-required flag.
**Evaluation metric:** Share of mappings accepted unchanged by the conversion team, and post-conversion fee and interest reconciliation breaks per thousand accounts against the bank's previous conversion.
**Scope:** Modest modelling, heavy domain configuration per core pair. 1–2 engineers with a conversion manager, 3–4 months for one vendor pair.
**Data availability:** Core vendors and conversion consultancies hold hundreds of past maps; banks hold only their own one or two conversions.
