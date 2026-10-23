# Machine Learning Opportunities — Professional Employer Organizations

**Industry:** [[professional-employer-organizations|Professional Employer Organizations]]
**Derived from:** [[problems/professional-employer-organizations/high-impact|High Impact]], [[problems/professional-employer-organizations/low-impact-1|Low Impact 1]], [[problems/professional-employer-organizations/low-impact-2|Low Impact 2]], [[problems/professional-employer-organizations/worker-life-1|Worker Life 1]], [[problems/professional-employer-organizations/worker-life-2|Worker Life 2]]

---

## 1. Capturing the New-Business Underwriter's Read of a Small Group
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #survival-analysis #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced PEO underwriters look at a prospect's census, questionnaires, morbidity score, carrier renewal and comp loss runs and "know" whether the group will run hot. That read is built over thousands of quotes and is never written down. The ML problem is to learn it from the underwriter's own past decisions and stated reasons, joined to what each admitted client later cost, and to surface it at quote time.

**ML task:** Client-level regression of first- and second-year health loss ratio and workers' comp loss ratio (credibility-weighted), plus classification of the underwriter's decision category (accept, rate-up, workers' comp only, decline) to measure agreement, with reject inference for declined prospects and survival modelling for early termination
**Input data:** Quote files: census (age, sex, zip, salary, coverage tier), group and personal health questionnaire answers, prescription-history morbidity scores, incumbent renewal and claims experience where available, workers' comp loss runs and mods, NAICS code, broker, effective date, price relative to manual rate, override flags and approver. Underwriter notes and emails. For admitted clients: monthly health claims net of large-claim pooling, workers' comp incurred losses by accident year, unemployment charges, and termination date and reason.
**Target:** Credibility-weighted client loss ratio by line over the first 12 and 24 months; probability that a group lands in the plan's worst cohort (e.g. above 125% MLR); and the underwriter's own decision and reason tags.
**Evaluation metric:** Lift and calibration of the predicted loss ratio on later underwriting years, scored strictly out of time. Report the share of total claims captured by the predicted worst decile, against the underwriters' own decisions as the baseline. The underwriter's test-retest agreement on re-presented files is the ceiling for decision agreement. A missed high-cost group costs far more than an unnecessary rate-up, but declines also lose broker goodwill, so measure both at the operating threshold.
**Scope:** The data collection challenge is that the expert's reasoning has to be captured as they work. That means a one-click reason-tagging step inside the underwriting workbench, plus LLM extraction of reasons from historical notes and emails to seed the ledger. The labelling challenge is that a small group's loss ratio is dominated by a few claimants: the PrestigePEO deck reports 25 of every 165 groups running far worse than forecast. Labels need pooling and credibility weighting, outcome windows long enough to develop comp losses, and reject inference because declined groups are never observed. Underwriters also disagree with themselves across the quote season. The deployment challenge is that guidance must appear before the quote leaves, in the underwriter's terms, and survive a sales override. A team of 2 data scientists, an actuary and an underwriting lead, 9-12 months, with value first as retrieval ("the twelve most similar groups we admitted, and how they ran") before any score is trusted.
**Data availability:** Large PEOs hold years of quote files and client-level claims, though in fully insured plans the claims detail sits with the carrier and arrives as reports. Questionnaires and prescription histories are protected health information under authorisations, so the work must run inside the PEO's HIPAA controls. Small PEOs lack the volume and would need a pooled or vendor model.

---

## 2. Client-Level Credibility Pricing at Renewal
#bayesian-inference #maximum-a-posteriori-estimation #monte-carlo-methods #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Set each in-force client's health renewal from one or two years of its own claims, too few to trust alone, blended with the experience of similar clients and the plan, so that low-claim clients are not overcharged into leaving and high-claim clients are not undercharged into staying.

**ML task:** Hierarchical Bayesian model of client claims cost per member per month, with partial pooling by size, industry, region and plan design, and simulation of the renewal distribution under alternative rate actions
**Input data:** Client-month enrolment and claims (paid and incurred, large claims capped and pooled), plan design, demographics, prior rate actions and whether the client renewed, left or changed plans, and competing quotes where the account team recorded them.
**Target:** Next-year claims cost per member with a credible interval, and the probability of retention at each candidate rate.
**Evaluation metric:** Out-of-time accuracy and interval coverage of next-year cost by client size band. The business test is plan-level loss ratio and retention of low-claim clients at the recommended rates against the current method.
**Scope:** The statistics are standard actuarial credibility in Bayesian form. The work is data plumbing and agreeing a pooling point with the actuaries. 1 actuary and 1 data scientist, 4-6 months for one plan.
**Data availability:** Held by the PEO (in self-funded or minimum-premium arrangements) or reported by the carrier. Competing-quote data is sparse and mostly anecdotal.

---

## 3. Client Attrition and Termination-Cause Modelling
#survival-analysis #random-forests #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Predict which clients will terminate, when, and why (price shock at renewal, service failure, outgrowing the PEO, acquisition, business failure) so account teams intervene where it can change the outcome.

**ML task:** Competing-risks survival model of time to termination by cause
**Input data:** Client tenure, size and growth, renewal rate changes by line, service tickets and payroll correction counts, specialist turnover on the account, benefits participation changes, workers' comp claims, broker identity, and termination reasons coded from exit notes.
**Target:** Hazard of termination by cause over the next 3, 6 and 12 months.
**Evaluation metric:** Time-dependent concordance and calibration by cause; precision at the top of the list matters most because account managers can call only so many clients.
**Scope:** 1 data scientist, 3-4 months. The hard part is coding termination reasons consistently from free-text exit notes, which an LLM can do with human review on a sample.
**Data availability:** Fully internal. Insperity reports retention of about 83% in 2025, so a large PEO observes thousands of terminations a year.

---

## 4. Workers' Comp Class Code Assignment from Job Descriptions
#bert #transformers #large-language-models #k-nearest-neighbors #evaluation-metrics #compliance #automation

**Problem statement:** Assign each worksite employee's NCCI (or independent bureau) class code, and split payroll where the rules allow, from job titles, duties, client NAICS code and state, so premium and client-level reporting are right from onboarding.

**ML task:** Multi-class text classification with retrieval of similar historical assignments and the bureau's phraseology, with a confidence threshold for human review
**Input data:** Job titles and duty descriptions from onboarding forms, client business descriptions, state, past class assignments, premium audit adjustments and carrier reclassifications.
**Target:** Class code per employee per state, plus a flag where governing-class or split rules need an underwriter.
**Evaluation metric:** Accuracy against audited classes at the confidence level used for auto-assignment, with a separate error rate on high-hazard classes, where misclassification under-prices risk.
**Scope:** 1 ML engineer and a classification specialist, 3-4 months. Premium audit adjustments provide the labels.
**Data availability:** Internal assignment history plus audit outcomes. Bureau manuals are licensed.

---

## 5. Rate Notice Extraction and Unemployment Tax Reconciliation
#large-language-models #seq2seq #change-point-detection #decision-trees #evaluation-metrics #compliance #automation

**Problem statement:** Read every state unemployment rate notice, for the PEO and for each client account, extract the account, rate, wage base and effective date, and reconcile it against the rate the payroll system is using and the state's reporting regime for that client.

**ML task:** Document extraction into a fixed schema, rule-based reconciliation, and detection of unexplained shifts in a client's effective tax rate between quarters
**Input data:** Rate notices (PDF, portal downloads, scanned mail), state reporting-regime rules, client-state account register, quarterly filings and payroll tax ledgers.
**Target:** Structured notice records, mismatch flags with the likely cause, and alerts on rate changes not backed by a notice.
**Evaluation metric:** Field-level extraction accuracy on rate and account number, aiming for near-zero silent errors, and the share of rate mismatches caught before the first quarterly return.
**Scope:** 1 engineer and a payroll tax analyst, 3 months for the top twenty states. The regime rules matter more than the model.
**Data availability:** All internal. Notices number in the thousands each January for a mid-sized PEO (estimate).
