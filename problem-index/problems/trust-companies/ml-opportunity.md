# Machine Learning Opportunities — Trust Companies

**Industry:** [[trust-companies|Trust Companies]]
**Derived from:** [[problems/trust-companies/high-impact|High Impact]], [[problems/trust-companies/low-impact-1|Low Impact 1]], [[problems/trust-companies/low-impact-2|Low Impact 2]], [[problems/trust-companies/worker-life-1|Worker Life 1]], [[problems/trust-companies/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Officer's Read of Distribution Requests
#tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #survival-analysis #evaluation-metrics #compliance #worker-facing

**Problem statement:** Senior trust officers read a discretionary distribution request and "know" whether it is ordinary support, a beneficiary in trouble, the start of exploitation, or a decision that will provoke the remainder beneficiaries — a judgement built over hundreds of requests that they cannot specify and that leaves when they retire. The ML problem is to learn that read from the company's own history of requests, memos, committee decisions and later outcomes, and surface it, with precedents, to whoever handles the next request.

**ML task:** Multi-label classification of each request (support versus discretionary purpose; escalation, exploitation, sibling-equalisation and spend-down risk flags) from the request text, the abstracted instrument standard and the account history; a calibrated probability of an adverse outcome within 24 months (complaint, written objection, petition, surcharge claim); and nearest-neighbour retrieval of precedent requests under similar instrument language.
**Input data:** Beneficiary emails and call notes; discretionary memoranda and committee minutes; the trust accounting distribution history; abstracted instrument provisions (entry 2); beneficiary contact and request cadence; complaint logs, litigation and legal-hold records; account terminations and where the assets went.
**Target:** Request-level labels in the senior officers' own vocabulary; the adverse-outcome event and its timing; and agreement between the model's flags and a senior officer's blind review.
**Evaluation metric:** Recall on requests that later produced an adverse outcome is the binding metric, because a missed exploitation or conflict case costs a family and a lawsuit while a false flag costs an officer a few minutes. Brier score and calibration of the 24-month probability, measured strictly out of time. For the flags, agreement with held-out senior-officer labels, reported against those officers' own test-retest agreement on re-presented cases as the ceiling. Consistency across officers and committee sittings is reported separately as a governance metric.
**Scope:** The data collection challenge comes first: the expert's read has to be captured as the officer works, so the system needs a near-zero-effort capture surface inside the memo and email workflow, including one-click logging of declines and informal screens, plus a back-fill of ~5 years of memos aligned to ledger entries. The labelling challenge is that adverse outcomes are rare, slow and noisy, and that officers disagree with themselves after a recent lawsuit; the plan needs repeated blind review of a sample by several senior officers to estimate intra- and inter-rater reliability, and survival models that use partial follow-up rather than waiting for final outcomes. The deployment challenge is speed and law: the output must arrive before the memo is written and faster than the officer's own recall, and it must inform rather than decide, because a trustee must exercise its own discretion. 2 ML engineers, 1 data engineer and a senior trust officer at least half-time, 9–12 months, with value arriving first as precedent retrieval ("the last six requests like this under a HEMS standard, and what happened") before any flag is trusted.
**Data availability:** Held entirely by each trust company, fragmented across the trust accounting system, the imaging system, email and CRM. Beneficiary data is customer information under the Gramm-Leach-Bliley Act and cannot be pooled across firms without agreements, so a single large trust company's history is the realistic training set; smaller firms would start from retrieval over their own files.

---

## 2. Trust Instrument Abstraction into a Fiduciary Schema
#large-language-models #transformers #bert #evaluation-metrics #feature-engineering #compliance #automation

**Problem statement:** Extract every administratively relevant provision from a scanned trust instrument and its amendments — parties and roles, beneficiary classes, distribution standards, powers, protector and directed-trust provisions, tax character, termination events — into a structured schema with page citations, and map it to the trust accounting system's setup codes.

**ML task:** Document-level information extraction and clause classification with amendment-chain resolution (which version of each provision is operative), plus classification of each distribution standard as ascertainable or not.
**Input data:** Scanned and native instruments, restatements, amendments, pour-over wills and court orders; historical account setups in the trust accounting system as weak labels; acceptance memos.
**Target:** A populated schema per trust with field-level citations and confidence, and the corresponding system codes.
**Evaluation metric:** Field-level F1 against officer-abstracted gold sets, with dispositive provisions (standards, beneficiaries, termination) held to a zero-silent-error rule: a wrong standard at high confidence is worse than a blank field. Time from receipt to approved setup.
**Scope:** The existing book of trusts provides thousands of instrument-to-setup pairs as weak supervision, noisy where historical setups were wrong. OCR quality on older typed and handwritten instruments is the hard tail. 2 engineers and a trust administration lead, 4–6 months to a reviewed-extraction workflow.
**Data availability:** Instruments are held by every trust company; labelling needs officers to correct a few hundred abstractions to build a gold set.

---

## 3. Exception-Ranked Annual Account Review
#gradient-boosting #feature-engineering #evaluation-metrics #hypothesis-testing #compliance #automation

**Problem statement:** Rank every discretionary account by the probability that its annual review under 12 CFR 9.6(c) would find an issue requiring action — concentration, mismatch with the instrument or the beneficiaries' needs, impartiality imbalance, cash drag, a special asset overdue for valuation — so reviewers spend their time where findings are.

**ML task:** Binary classification of review outcome (action required or not), with multi-label reasons, from account features.
**Input data:** Holdings and transactions; instrument investment provisions (entry 2); income versus remainder beneficiary profiles; distribution history; prior review outcomes and the actions taken; internal fiduciary audit and examiner findings.
**Target:** Whether the review produced a required action, and its category.
**Evaluation metric:** Recall at the review capacity the team has (share of action-required accounts in the top-k), because missing an account with a real issue is an examiner finding and potential surcharge, while over-ranking a clean account costs an hour. Calibration matters for the short-form clearance threshold, which must be defended to examiners.
**Scope:** Past review outcomes are recorded unevenly; 2–3 years of structured reviews are needed for a stable model, and the short-form clearance path must be agreed with compliance and the examiner before it is used. 1 data scientist and 1 engineer, 4 months to a first ranking.
**Data availability:** Internal and reasonably clean for holdings; review outcomes need back-coding from review documents.

---

## 4. Next-Generation Retention at Trust Termination
#survival-analysis #gradient-boosting #causal-inference #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** When a trust terminates or a grantor dies, the assets pass to beneficiaries who may move them elsewhere. Estimate, for each account approaching a known termination or succession event, the time until the assets leave, and which relationship actions change it.

**ML task:** Survival analysis of time-to-asset-departure after a termination or succession event, with heterogeneous-effect estimates for interventions (officer introductions, family meetings, continuity of officer).
**Input data:** Instrument termination provisions and beneficiary ages (entry 2); account histories; contact logs and meeting records; officer changes; distribution and complaint history; post-termination account openings and closures.
**Target:** Time from termination or succession to closure or transfer of each successor account; retained assets at 12 and 36 months.
**Evaluation metric:** Concordance index and calibration of retention curves out of time; for interventions, estimated uplift with confidence intervals, treated as suggestive because contact decisions were not randomised.
**Scope:** Termination events are known years in advance from instruments, which makes the planning horizon long and the business case clear. Effects of interventions are confounded by which families officers chose to cultivate. 1 data scientist, 3–4 months.
**Data availability:** Internal; successor-account data may sit in a separate wealth platform and needs joining by household.

---

## 5. Corrected-1099 and Late Tax Information Forecasting
#logistic-regression #gradient-boosting #time-series-forecasting #evaluation-metrics #feature-engineering #automation

**Problem statement:** Predict, at the start of tax season, which securities held across the trust book will issue corrected 1099s or late tax information, and when, so the tax unit can sequence 1041 preparation and minimise amended K-1s.

**ML task:** Security-level binary classification of correction risk plus a time-to-correction estimate, aggregated to trust-level exposure scores.
**Input data:** Each issuer's history of reclassifications and corrected forms; security type (RIC, REIT, MLP, partnership, foreign fund); income composition; prior-year correction dates; the trust book's holdings.
**Target:** Whether a corrected or late tax document arrives after the planned preparation date, and the date it arrives.
**Evaluation metric:** Recall on securities that issued corrections, weighted by the number of trusts holding them, because one missed fund can reopen hundreds of returns; reduction in amended K-1s against the prior season as the business metric.
**Scope:** Small model, high leverage. Several seasons of correction history are needed, collected from the tax unit's own records. 1 data scientist and the tax manager, 2–3 months.
**Data availability:** The trust company holds its received tax documents and dates; issuer-level history may also be licensable from tax information vendors.
