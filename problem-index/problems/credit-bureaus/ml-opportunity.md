# Machine Learning Opportunities — Credit Bureaus

**Industry:** [[credit-bureaus|Credit Bureaus]]
**Derived from:** [[problems/credit-bureaus/high-impact|High Impact]], [[problems/credit-bureaus/low-impact-1|Low Impact 1]], [[problems/credit-bureaus/low-impact-2|Low Impact 2]], [[problems/credit-bureaus/worker-life-1|Worker Life 1]], [[problems/credit-bureaus/worker-life-2|Worker Life 2]]

---

## 1. Learning the Data-Reporting Analyst's Read of a Furnisher Load
#tacit-knowledge-ml #autoencoders #change-point-detection #gradient-boosting #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Experienced data-reporting analysts look at a furnisher's monthly load summary and "know" whether a large shift is an error (a system conversion that reset delinquency dates, a dropped product line, duplicated collection accounts) or a real event (a forbearance programme, a portfolio sale). The ML problem is to model each furnisher's normal file, surface shifts at field and segment level, and learn from the analysts' past decisions and later outcomes which shifts are errors.

**ML task:** Per-furnisher multivariate change-point and distribution-shift detection on load profiles, followed by binary classification of each flagged shift as error or legitimate change, with a ranked review queue
**Input data:** Monthly load profiles per furnisher: record counts, distributions of account status, payment-history transitions, date of first delinquency, balances, special comments and ECOA codes, by product and segment; furnisher metadata (type, size, servicing platform, known conversions); historical hold and accept decisions with analyst notes; mass corrections received after posting; disputes and complaints by furnisher and month.
**Target:** Per load: probability that a flagged shift is a reporting error, the fields and segments responsible, and the most similar past case with its resolution.
**Evaluation metric:** Recall on loads that later produced a mass correction or a dispute cluster, at a fixed analyst review budget per cycle — a missed bad load from a large furnisher reaches millions of files, while a false flag costs an analyst a few minutes. Report precision at that budget and time-to-decision against the analyst's unaided review, and measure model–analyst agreement against analysts' own test–retest agreement on re-reviewed loads.
**Scope:** The data collection challenge comes first: the analyst's judgement must be captured while they review, so the work starts by instrumenting the review screen to log what was examined, what was flagged and a one-line reason, and by reconstructing history from tickets and correction records. The labelling challenge is that outcomes are late, partial and biased toward errors consumers notice, and analysts read the same shift differently depending on recent experience, so a sample of loads must be re-reviewed blind to estimate intra-rater reliability. The deployment challenge is the posting window: flags must arrive within minutes of the load with an explanation an analyst can act on, or the file posts unreviewed. 2 ML engineers, 1 data engineer and a senior data-reporting analyst, 6–9 months to a first production queue, with value appearing first as per-furnisher drift dashboards before any classifier is trusted.
**Data availability:** Load profiles and dispute records sit inside each bureau; analyst decisions survive mostly as free-text tickets. Mass corrections and dispute clusters provide delayed labels. The bureau owns its load history; no outside party has it.

---

## 2. Dispute Triage: Genuine Error, Template, Mixed File or Identity Theft
#bert #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #compliance #workflow-orchestration

**Problem statement:** Classify each incoming dispute by type and disputed items so genuine errors, identity theft claims and possible mixed files reach investigators with time on the FCRA clock, while templated volume is handled consistently and never dismissed wrongly.

**ML task:** Document understanding of scanned letters and uploads; multi-label classification of dispute reason; item-level linking of disputed text to tradelines; near-duplicate detection of templated submissions
**Input data:** Dispute submissions (scanned letters, web forms, call notes, CFPB referrals); the consumer's file at receipt; historical dispute codes sent on ACDVs; furnisher responses; investigation outcomes (modified, deleted, verified); identity theft documentation flags.
**Target:** Disputed tradelines, reason category, third-party or template indicator, mixed-file or identity theft flag, and a drafted ACDV dispute code and narrative.
**Evaluation metric:** Recall on disputes whose investigation led to modification or deletion is the binding metric; a genuine error routed as a template is the costly failure. Track agreement with expert agents on reason codes, the share of ACDVs carrying a specific narrative rather than a generic code, and days remaining on the clock when a case reaches an investigator. Any automated "frivolous" determination must be measured separately and kept rare, because it carries its own FCRA notice duty and litigation exposure.
**Scope:** Historical dispute outcomes provide large weak labels; expert agents must label a stratified sample for reason and item linkage. Templated text drifts quickly as credit repair firms adopt language models, so near-duplicate detection needs continual refresh. 2 ML engineers and 1 operations lead, 4–6 months.
**Data availability:** Each bureau holds millions of disputes and outcomes (estimate); the furnisher's investigation evidence is not visible to the bureau beyond the ACDV response.

---

## 3. Mixed-File Detection
#graph-neural-networks #gradient-boosting #k-nearest-neighbors #feature-engineering #evaluation-metrics

**Problem statement:** Detect files that contain another person's records (often a relative with a similar name, or a shared address) and identities split across two files, before a lender pulls the wrong history.

**ML task:** Link prediction on an identity graph of names, SSN variants, dates of birth, addresses and tradelines; anomaly scoring of records inconsistent with the rest of a file
**Input data:** Identity elements and their history per file; tradeline-to-identity attachment events; address and phone histories; confirmed mixed-file dispute outcomes; file merge and split operations performed by investigators.
**Target:** Probability that a record belongs to a different person than the file's subject; probability that two files describe the same person.
**Evaluation metric:** Precision on split recommendations must be very high, because a wrong split destroys a real history; recall on records later removed through mixed-file disputes measures value. Report both by demographic proxy (shared-surname households, generational suffixes) because errors concentrate there.
**Scope:** Labels come from resolved mixed-file disputes, a small and biased set; synthetic perturbation of known-good files helps. 2 ML engineers, 6 months. Matching logic is the bureau's core asset and changes go through heavy testing.
**Data availability:** Internal to each bureau; investigator merge and split actions are the best labels and are often logged only as system events.

---

## 4. Thin-File Scoring From Rent, Utility and Cash-Flow Data
#gradient-boosting #logistic-regression #survival-analysis #causal-inference #evaluation-metrics #revenue-impact

**Problem statement:** Estimate default risk for applicants with thin or no bureau files using rent payments, utility and telecom accounts and consumer-permissioned bank cash flow, correcting for the fact that only approved applicants have observed outcomes.

**ML task:** Binary default prediction over a fixed horizon with reject inference; time-to-default survival modelling; incremental-lift testing against a traditional-score baseline
**Input data:** Rent and utility payment histories furnished or permissioned; cash-flow features (income regularity, balance volatility, overdrafts, recurring obligations); bureau file where present; booked-loan performance; declined-applicant follow-up through later bureau records.
**Target:** 12–24 month serious delinquency on booked loans; inferred outcome on declines.
**Evaluation metric:** Lift in the approval rate at a constant expected loss rate among thin-file applicants is the headline business metric; Gini and calibration by segment underneath. Adverse-action reason codes must be stable and explainable, and disparate-impact testing is part of evaluation, not an afterthought.
**Scope:** Hard because outcomes need 12–24 months and approved samples are selected. A lender partnership is required for performance data. 2 data scientists and a model-validation reviewer, 9–12 months including validation documentation.
**Data availability:** Cash-flow data requires consumer permission per application; rent data covers only properties and tenants that report; performance data belongs to lenders. CFPB estimates ~7 million adults were credit invisible in 2020.

---

## 5. Cross-Bureau Tradeline Matching for Merged Reports
#word-embeddings #k-nearest-neighbors #gradient-boosting #feature-engineering #evaluation-metrics #automation

**Problem statement:** Decide which tradelines on three bureau files are the same account so a mortgage merged report lists each obligation once and correctly.

**ML task:** Pairwise match classification with candidate generation over creditor-name embeddings and account attributes; clustering into accounts
**Input data:** Tradelines from three bureau files per applicant: creditor names, masked account numbers, open dates, original amounts, balances with reporting dates, payment histories, ECOA codes; historical processor corrections and supplements.
**Target:** Same-account clusters with a confidence per merge.
**Evaluation metric:** Pairwise precision and recall weighted by monthly payment, because a missed duplicate inflates debt-to-income and a false merge hides an obligation; supplement and re-pull rate per loan as the operational metric.
**Scope:** Resellers' merge corrections provide labels; 1–2 engineers, 3–4 months on top of an existing merge engine.
**Data availability:** Held by mortgage credit resellers under bureau agreements; usable for the reseller's own merge logic.
