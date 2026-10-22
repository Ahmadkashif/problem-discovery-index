# Machine Learning Opportunities — Title Insurance Carriers

**Industry:** [[title-insurance-carriers|Title Insurance Carriers]]
**Derived from:** [[problems/title-insurance-carriers/high-impact|High Impact]], [[problems/title-insurance-carriers/low-impact-1|Low Impact 1]], [[problems/title-insurance-carriers/low-impact-2|Low Impact 2]], [[problems/title-insurance-carriers/worker-life-1|Worker Life 1]], [[problems/title-insurance-carriers/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Claims Counsel's Read at Intake
#tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #transformers #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced title claims counsel read a new claim and know whether it will be cured cheaply, litigated or paid as a full loss of title. The read draws on servicers, counties, defect types and the smell of fraud, and they cannot write it down. The ML problem is to learn that read from closed claims and counsel's own recorded predictions, and to surface it at intake with precedents attached.

**ML task:** Multi-class classification of resolution path (cure, defend, negotiate, pay, decline as excluded) from the notice and underwriting file; quantile regression of total cost (indemnity plus loss adjustment expense); survival model of time to close; nearest-neighbour retrieval of similar closed claims
**Input data:** Claim notices and correspondence; the policy, endorsements and Schedule B exceptions; the commitment and any underwriter approval; the agent's examination file where obtainable; recorded documents for the parcel; claim notes, coverage letters, panel-counsel invoices and payment history; state, county, transaction type, policy year and agent identifiers; root-cause codes where they exist.
**Target:** Resolution path; total cost at close; days to close; root cause (examination error, undiscoverable fraud or forgery, survey or access, agent defalcation, other); and agreement between the model and counsel's recorded intake prediction.
**Evaluation metric:** Calibration and pinball loss of the cost quantiles on claims closed after a strict time cut, with the top decile of severity weighted most heavily. A missed full-loss-of-title claim costs far more than an over-reserved minor one, so recall on the high-severity band matters more than precision. For resolution path, macro-F1 against held-out outcomes, reported beside counsel's own test-retest agreement on a re-annotated sample as the realistic ceiling.
**Scope:** Data collection comes first and is the hardest part. Counsel's read has to be captured at the moment of intake through a near-zero-effort form (path, severity band, confidence), and historical claims must be reconstructed from notes, letters and invoices across claim systems that have changed over the years. Labelling is the second problem: counsel disagree with each other and with themselves, and cure options vary by state, so labels need repeated annotation on a sample and outcomes need a careful definition of "cost" that includes legal spend. Deployment is the third. The prediction must arrive inside intake, faster than counsel's own read of roughly ten minutes (estimate) and with the precedents that justify it, and it must never decide coverage, because coverage positions carry bad-faith exposure. Plan on 2 ML engineers, 1 data engineer and a senior claims counsel at 30% for 9–12 months. Retrieval of similar claims delivers value in the first quarter, well before any severity model is trusted.
**Data availability:** Each of the four families holds tens of thousands of closed claims (Milliman analysed over 127,000 claims on 2013–2022 policies for ALTA), but in claim systems built for payment, not analysis. The underwriting file is often with the agent. Counsel's intake predictions do not exist and must be captured going forward.

---

## 2. Agent Defalcation Early Warning
#autoencoders #change-point-detection #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Detect agents whose escrow accounts are drifting toward a shortage early enough to audit, freeze CPL issuance or intervene, by combining reconciliation data, remittance behaviour and policy and CPL issuance patterns.

**ML task:** Unsupervised anomaly scoring of each agent's monthly behaviour against its own history and peers (autoencoder reconstruction error); change-point detection on remittance lag and reconciliation timeliness; supervised hazard model of time to a confirmed shortage, trained on past defalcations
**Input data:** Three-way reconciliations and bank feeds supplied under underwriting agreements; CPLs issued, commitments and policies reported; remittance amounts and dates; audit findings; licensing, E&O and ownership changes; complaints; volume by county and transaction type.
**Target:** Anomaly score per agent-month; detected change points; probability of a confirmed escrow shortage within 6 and 12 months.
**Evaluation metric:** Recall on historical defalcations at a fixed audit budget (the share of past shortages that would have been in the top-N agents flagged in the preceding six months), plus lead time gained. False positives cost audit days and agent goodwill, so precision at the audit capacity is the operating constraint.
**Scope:** Positives are rare, so most of the signal comes from unsupervised scoring and expert-built features, with the hazard model calibrated on a few dozen to a few hundred confirmed events per family (estimate). Plan on 1–2 data scientists and an agency audit lead for 6 months. The data contract with agents is the slowest part.
**Data availability:** Remittance, CPL and policy data are the underwriter's own. Reconciliation and bank data depend on what each underwriting agreement lets the underwriter demand, and on whether agents' reconciliation vendors will share it.

---

## 3. Policy-Year Loss Development by Defect and Channel
#bayesian-inference #mcmc-sampling #time-series-forecasting #confidence-intervals #maximum-likelihood-estimation #evaluation-metrics

**Problem statement:** Estimate ultimate loss rates by policy year, state, channel (direct, affiliated agent, non-affiliated agent) and claim type, where claims emerge over a tail in which only 65–75% of amounts are known by year six and a single fraud wave can distort a year.

**ML task:** Hierarchical Bayesian loss development, with partial pooling across states and channels and separate emergence patterns for fraud and forgery, agent defalcation and ordinary defects; posterior predictive intervals on IBNR
**Input data:** Paid and incurred triangles by policy year and claim type; policy counts and premium by state and channel; known-claim reserves; economic covariates (refinance share, home price change); claim-type tags from entry 1.
**Target:** Ultimate loss rate and IBNR by segment, with intervals.
**Evaluation metric:** Out-of-time accuracy of predicted development on held-back diagonals, and coverage of the posterior intervals. A reserve range that is too narrow is worse than a wide, honest one, because statutory reserving and the appointed actuary's opinion depend on it.
**Scope:** Methodologically standard for actuaries, and new mainly in its segmentation and in feeding claim-type tags back from intake. Plan on 1 actuary and 1 data scientist for 4–6 months. First American's disclosure that 50 basis points on six policy years equals $162.7M of IBNR shows what tighter intervals are worth.
**Data availability:** Fully internal to each underwriter. Claim-type coding is inconsistent historically and is the main cleaning job.

---

## 4. Approval Precedent Retrieval and Risk Scoring
#large-language-models #word-embeddings #k-nearest-neighbors #logistic-regression #evaluation-metrics #worker-facing #compliance

**Problem statement:** For each agent request for underwriter approval, retrieve the governing bulletin and the company's most similar prior approvals with their conditions and outcomes, and estimate the claim propensity of approving on the proposed terms.

**ML task:** Information extraction from requests and commitments; dense retrieval over bulletins, manuals and past approvals; regularised logistic regression of later claim on request features (risk type, state, liability, conditions imposed, agent)
**Input data:** Approval requests and responses (email, portal), commitments and documents at issue, underwriting manuals and bulletins by state, policy and claim records.
**Target:** Ranked precedents; drafted conditions; probability of a claim within N years.
**Evaluation metric:** Retrieval precision at 5 judged by counsel. For the propensity model, AUC and calibration on approvals old enough to have matured, reported with wide intervals because claims on approved risks are rare.
**Scope:** Retrieval and drafting are quick wins: 1 engineer and counsel time, 3 months. The propensity model needs years of approvals joined to claims and may only ever be indicative.
**Data availability:** Approvals live in email and portal logs that are seldom joined to policy numbers. Linking them is the main job.

---

## 5. Remittance Extraction and Premium Verification
#large-language-models #seq2seq #decision-trees #evaluation-metrics #automation #data-integration

**Problem statement:** Extract policy lines from agents' remittance reports in any format, match them to CPLs and commitments, recalculate premiums against each state's rate manual, and rank the exceptions by money at risk.

**ML task:** Document and table extraction to a policy schema; record linkage to CPL and commitment records; a rules engine for premium recalculation with a learned decision-tree model to classify exception causes (wrong bracket, missed reissue credit, simultaneous-issue error, unreported policy)
**Input data:** Remittance reports (portal files, spreadsheets, PDFs), CPL and commitment logs, state rate manuals, historical exception resolutions.
**Target:** Structured policy records with match status; recalculated premium; exception cause and priority.
**Evaluation metric:** Field-level extraction accuracy at the threshold where records post without review, with zero tolerance for silent premium errors. Recall on unreported policies (CPLs aged past threshold with no policy) is the safety metric.
**Scope:** Rate-manual encoding per state is the tedious core. Plan on 2 engineers for 4–6 months for the top ten states by premium.
**Data availability:** All internal. Historical exception notes provide labels for cause classification.
