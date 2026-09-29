# Machine Learning Opportunities — Neobanks

**Industry:** [[neobanks|Neobanks]]
**Derived from:** [[problems/neobanks/high-impact|High Impact]], [[problems/neobanks/low-impact-1|Low Impact 1]], [[problems/neobanks/low-impact-2|Low Impact 2]], [[problems/neobanks/worker-life-1|Worker Life 1]], [[problems/neobanks/worker-life-2|Worker Life 2]]

---

## 1. Restriction Decision Grading and Precision Estimation
#logistic-regression #gradient-boosting #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #compliance

**Problem statement:** A neobank restricts accounts by model and rule, reviews a subset of them, and never joins the decision to its outcome. The institution therefore knows its alert volume and its manual review cost and does not know the precision of any individual rule or vendor score.

**ML task:** Supervised evaluation of existing decision rules against reconstructed outcome labels, with explicit correction for review-selection bias
**Input data:** Every restriction event with its triggering reason codes and vendor scores; the review case record including documentation requested and supplied; the final disposition; the member's ninety-day post-reinstatement behaviour from the core ledger; complaint records; confirmed fraud losses.
**Target:** Per-decision correctness, and per-rule precision and recall against it.
**Evaluation metric:** Precision per rule is the headline, but the honest metric is precision with an uncertainty interval that reflects how much of the population was never reviewed. Report the estimated false-positive rate among unreviewed freezes separately, because that population is systematically different from the one that complained, and a point estimate that ignores it is the specific error this work exists to correct.
**Scope:** The first deliverable is not a model but the join: one row per decision carrying the trigger, the review, the disposition and the subsequent behaviour. Rule-level grading against it usually retires a meaningful fraction of a legacy rule library immediately, which is the cheapest available reduction in false positives and requires no learning. Propensity weighting on complaint likelihood, plus a deliberately randomised audit sample of unreviewed freezes, is what makes the estimate defensible. 2 data engineers and 1 data scientist, 4 months.
**Data availability:** All of it exists inside the institution across three systems. Nothing needs to be purchased and nothing needs to be collected; the obstacle is ownership of the join, not access.

---

## 2. Dispute Classification and First-Party Misuse Separation
#bert #large-language-models #gradient-boosting #k-nearest-neighbors #evaluation-metrics #feature-engineering #compliance #revenue-impact

**Problem statement:** Disputes arrive as a member's free-text description and must be classified into regulatory and network categories that carry different obligations, then filed under the correct reason code before a deadline. A substantial minority are first-party — the member or someone in their household did authorise the transaction — and separating those on evidence rather than on prior claim count is the judgement the process turns on.

**ML task:** Multiclass classification of dispute type from member narrative and transaction context, plus a calibrated first-party misuse score
**Input data:** Historical claim narratives with their eventual disposition; the disputed authorisation record including device, location, channel and merchant descriptor; the member's transaction and device history; merchant relationship history; prior claim frequency and outcomes; representment results.
**Target:** Dispute category and network reason code; and the probability that the transaction was authorised by the member or a household member.
**Evaluation metric:** For classification, accuracy weighted by the cost of the specific misrouting, since sending a merchant dispute down the unauthorised path changes the institution's obligations. For first-party misuse, calibration matters far more than discrimination: the score is used to justify a denial that a member may contest, so a stated 80% must mean 80%, and the operating threshold must be set where a wrongly denied claim is treated as more costly than a wrongly paid one.
**Scope:** Tens of thousands of historical claims with known dispositions make this directly supervised. Evidence assembly per reason code is mechanical and should ship alongside, because representment success depends almost entirely on it. Queue forecasting from the institution's own transaction data — a merchant failure is visible days before the claims arrive — is a small addition with real staffing value. 2 ML engineers, 5 months.
**Data availability:** Excellent and internal. Narratives, dispositions and authorisation records are all retained; the main gap is that denial reasons are often recorded as a code without the analyst's reasoning.

---

## 3. Review Document Extraction and Case Similarity Retrieval
#large-language-models #bert #object-detection #cnns #k-nearest-neighbors #word-embeddings #evaluation-metrics #worker-facing

**Problem statement:** Risk analysts open each case with a set of photographs — a licence at an angle, a pay stub, a screenshot of a screen — and manually read, cross-check and judge them under a handle-time target. The cases themselves repeat in a few dozen recognisable patterns that each analyst re-derives from raw material every time.

**ML task:** Document field extraction from low-quality photographs with cross-document consistency checking, plus nearest-neighbour retrieval over historical cases
**Input data:** Uploaded identity, income and address documents; the case record and reason codes; account and transaction history; counterparty and device fingerprints; historical cases with their dispositions and post-decision outcomes.
**Target:** Extracted fields with confidence; consistency and plausibility flags; and a ranked set of similar prior cases with their dispositions.
**Evaluation metric:** Extraction is measured by field-level accuracy at the confidence threshold where a field is shown without review, and by how much analyst handle time falls — but the decisive metric is that extraction must never assert a field it has not read correctly, since an analyst trusting a wrong name is worse than an analyst reading the image. For retrieval, measure whether analysts agree the surfaced cases are genuinely similar, and whether decision consistency across analysts improves.
**Scope:** Retrieval is the higher-value half and the easier one: it makes the tacit pattern knowledge of experienced analysts available to everyone in their first week. Campaign-level clustering — grouping the forty queue items that are actually one scam — is a direct extension and lets an analyst decide once. Authenticity signals should stay advisory; a template mismatch is a reason to look harder, not a finding. 2 ML engineers, 5 months.
**Data availability:** Documents and case outcomes are retained for regulatory reasons. Historical extraction labels do not exist and are the main annotation cost, though analyst corrections generate them once the tool is in use.

---

## 4. Sponsor Reporting Obligation Extraction and Mapping Validation
#large-language-models #bert #word-embeddings #evaluation-metrics #feature-engineering #data-integration #compliance #workflow-orchestration

**Problem statement:** Sponsor bank reporting obligations arrive as prose in oversight agreements and emails, are interpreted once into queries by a compliance analyst, and drift silently as the underlying data model changes. Programmes reporting to two sponsors during a migration have no way to check that the two versions of the same figure agree.

**ML task:** Extraction of structured reporting obligations from agreement text, and semantic reconciliation of metric definitions across sponsors and over time
**Input data:** Oversight agreements, reporting schedules and examiner request emails; historical submitted workbooks and their underlying queries; the programme's data model and its change history; the mapping between obligation and query where it has been documented.
**Target:** A structured obligation record — metric, definition, grain, frequency, format — and an alignment between obligations expressed differently by different sponsors.
**Evaluation metric:** Extraction precision judged by the compliance team, with a deliberate bias toward flagging ambiguity rather than resolving it: an obligation confidently extracted wrongly is worse than one marked as needing a human read. For reconciliation, the metric is detection of genuine definitional divergence between two sponsors' versions of the same figure, validated against cases the team already knows about.
**Scope:** The highest-value component is the smallest: a regression test that recomputes last period's submitted figures against the current data model and flags any that moved, which catches broken mappings before an examiner does. Provenance capture — storing the query that produced every submitted number — needs no machine learning and answers the question sponsors actually ask three months later. 1 ML engineer and 1 data engineer, 4 months.
**Data availability:** Agreements and historical workbooks are held by every programme. The obligation-to-query mapping is mostly undocumented, which is the point of the work.
