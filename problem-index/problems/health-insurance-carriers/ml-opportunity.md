# Machine Learning Opportunities — Health Insurance Carriers

**Industry:** [[health-insurance-carriers|Health Insurance Carriers]]
**Derived from:** [[problems/health-insurance-carriers/high-impact|High Impact]], [[problems/health-insurance-carriers/low-impact-1|Low Impact 1]], [[problems/health-insurance-carriers/low-impact-2|Low Impact 2]], [[problems/health-insurance-carriers/worker-life-1|Worker Life 1]], [[problems/health-insurance-carriers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Reviewer's Approve-on-Sight Read
#tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #causal-inference #evaluation-metrics #compliance #worker-facing

**Problem statement:** Experienced utilization management nurses recognise approvable authorization requests within minutes from patterns in the clinical packet that they cannot fully specify. The ML problem is to learn that read from the plan's history of reviewer determinations and later outcomes, approve or fast-track what an experienced reviewer would approve, and grade denials against what happened afterwards, without ever producing an automatic denial.

**ML task:** Criterion-level evidence extraction from clinical documents (span extraction against each applicable guideline element), then a calibrated probability that an experienced reviewer would approve on first review; separately, a denial-durability model estimating the probability that a denial would be overturned if appealed
**Input data:** Authorization requests with attached clinical documents (faxed and scanned notes, imaging and lab reports, therapy notes), the criteria set applied, reviewer and medical director determinations with timestamps, peer-to-peer outcomes, appeals and their results, resubmissions, and subsequent claims (service delivered, readmission, emergency visits) for the same member
**Target:** Approve-on-first-review (binary, calibrated); criterion elements met or not met with supporting page references; overturn-if-appealed probability for each denial
**Evaluation metric:** For fast-track approvals, precision against senior-reviewer adjudication at the plan's chosen operating point, and the share of approvals routed to fast-track (coverage). A wrong fast-track approval costs money; a missed one costs only reviewer time, so the operating point should be conservative at first. For denial durability, calibration (Brier score) on appealed denials, plus inverse-propensity weighting to estimate overturn rates on unappealed ones. Report model–reviewer agreement against the reviewers' own test–retest agreement on a re-reviewed sample, which is the ceiling.
**Scope:** The data collection challenge comes first. The reviewer's deciding evidence is not recorded today, so the review screen must let nurses mark the decisive pages with a click while they work, and historical cases need retrospective annotation by senior reviewers on a sample. The labelling challenge is that reviewers disagree with themselves on borderline cases, and appeal labels exist for only about one denial in nine and are skewed toward well-resourced providers. Both need repeated review and propensity correction. The deployment challenge is that the output must be faster than the nurse's own read and legally safe: the model may only approve or route to a human, every fast-track needs the evidence attached, and state laws such as California's SB 1120 bar algorithm-only denials. A team of 2 ML engineers, 1 clinical informaticist and 2 part-time senior nurse reviewers, 9–12 months for one service category (advanced imaging or elective orthopaedics), before any extension to post-acute review.
**Data availability:** Plans hold years of authorization records and attached documents inside their UM platforms, under HIPAA. Determinations and appeals are structured; documents are mostly images that need OCR. Downstream outcomes require joining claims, which most plans can do internally but rarely have.

---

## 2. HEDIS Hybrid Evidence Extraction
#bert #transformers #large-language-models #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Find, in each retrieved medical record, the specific dated evidence that closes a hybrid HEDIS measure numerator or establishes an exclusion, and present it to the abstractor with its location, so that a nurse confirms rather than searches.

**ML task:** Clinical named-entity and relation extraction (blood pressure readings with dates and settings, HbA1c values with dates, screening procedures with results, exclusion diagnoses) plus measure-rule evaluation over the extracted facts
**Input data:** Retrieved records (faxes, scanned PDFs, CCDA and EHR exports); measure specifications; the plan's prior years' abstraction results with the pages abstractors cited; auditor over-read outcomes
**Target:** For each sampled member and measure: numerator met, not met, or excluded, with the supporting text spans and page numbers
**Evaluation metric:** Recall on numerator-qualifying evidence measured against senior abstractor review, because a missed hit lowers the reported rate. Precision is nearly as important: a false hit that fails the auditor's medical record review validation can cost the whole measure. Report both per measure, plus time per chart before and after.
**Scope:** 2 ML engineers and 1 quality subject-matter lead, 6 months to cover the highest-volume hybrid measures. OCR quality on faxed records is the practical limit. NCQA's shift of hybrid measures to electronic clinical data reporting narrows the long-run market, but the same extraction applies to records used for supplemental data and care-gap closure year-round.
**Data availability:** Plans and their HEDIS vendors hold multi-year abstraction histories with page citations, which are excellent labels if they were stored. Records are protected health information and stay inside the plan or its business associate.

---

## 3. Directory Listing Error Prediction
#gradient-boosting #logistic-regression #survival-analysis #feature-engineering #data-integration #compliance

**Problem statement:** Predict, for every directory listing (clinician × location × network × field), the probability that it is wrong today, so verification outreach and roster follow-up go to the listings most likely to fail a secret-shopper check.

**ML task:** Field-level binary classification with time-to-change survival modelling (how long since this listing was last confirmed, and how quickly listings like it go stale)
**Input data:** Rosters and their submission history; CAQH attestations; credentialing records; claims billed by the clinician at each location by date; outreach call outcomes; returned mail; regulator and internal secret-shopper results
**Target:** Listing wrong or right on each field (location active, phone, accepting new patients, network participation), as established by successful verification or audit
**Evaluation metric:** Precision at the outreach budget (of the listings the team can call this month, how many were actually wrong) and the error rate in a random audit sample before and after. Errors on "accepting new patients" and network participation matter most because they create ghost networks.
**Scope:** 1 data scientist and 1 data engineer, 4 months. Most of the work is linking clinician, location and contract identities across systems; the model itself is standard.
**Data availability:** All inputs sit inside the plan. Labels come from outreach outcomes, which plans log but rarely keep in analysable form.

---

## 4. Payment Policy Edit Simulation and Billing Outlier Detection
#large-language-models #autoencoders #gaussian-mixture-models #evaluation-metrics #revenue-impact #automation

**Problem statement:** Translate a written reimbursement policy into candidate claim-edit logic, simulate its effect on the plan's historical paid claims before it goes live, and separately surface provider billing patterns that diverge from peers but are not caught by any existing edit.

**ML task:** Policy-to-rule generation with a language model constrained to the edit engine's rule grammar; unsupervised outlier detection on provider-level billing profiles (code mix, modifier rates, units per visit) against specialty peers
**Input data:** Reimbursement policy documents; existing edit configuration; a year or more of paid and denied claims; provider specialty and contract data; post-payment audit findings and provider dispute outcomes
**Target:** Executable candidate edits with a link to the policy paragraph; a ranked list of provider-code combinations whose billing departs from peers, with the dollars involved
**Evaluation metric:** For generated edits, the share accepted by configuration analysts without rework, and agreement between simulated and actual post-launch denial volumes. For outliers, the hit rate when the top-ranked leads are reviewed by payment integrity analysts, and the share upheld on provider dispute. False leads cost analyst time and provider goodwill, so precision in the top ranks matters most.
**Scope:** 2 ML engineers and a payment integrity analyst, 6–8 months. Generated edits always pass through human configuration and testing.
**Data availability:** Claims, edits and audit outcomes are internal. Dispute outcomes are often in email and need structuring.

---

## 5. Member Call Reason Classification and Denial Explanation
#bert #large-language-models #k-nearest-neighbors #evaluation-metrics #worker-facing #workflow-orchestration

**Problem statement:** Classify each member contact by reason and regulatory category (inquiry, grievance, appeal request, coverage determination request), assemble the claim and authorization facts behind it, and draft a plain-language explanation of the denial and next steps for the rep to edit.

**ML task:** Multi-class intent and regulatory-category classification on live transcripts; retrieval of similar resolved cases by embedding similarity; grounded text generation from structured claim, authorization and benefit data
**Input data:** Call transcripts and chat logs; denial reason codes and letters; claim, authorization and benefit records; grievance and appeal case files with outcomes
**Target:** Contact category (including whether the call legally constitutes a grievance or appeal request); a draft explanation citing the specific reason and the member's rights and deadlines
**Evaluation metric:** Recall on calls that are legally grievances or appeals, because a missed one starts a regulatory clock nobody is tracking. For explanations, factual accuracy against the record on a reviewed sample (zero tolerance for invented benefits), plus handle time and repeat-call rate.
**Scope:** 2 ML engineers, 5 months, inside the plan's contact centre platform. Generation is grounded only on retrieved records, with no free-form benefit answers.
**Data availability:** Plans record and transcribe calls already; grievance and appeal classification decisions are logged by case teams and make usable labels.
