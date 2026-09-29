# Machine Learning Opportunities — Lending Marketplaces

**Industry:** [[lending-marketplaces|Lending Marketplaces]]
**Derived from:** [[problems/lending-marketplaces/high-impact|High Impact]], [[problems/lending-marketplaces/low-impact-1|Low Impact 1]], [[problems/lending-marketplaces/low-impact-2|Low Impact 2]], [[problems/lending-marketplaces/worker-life-1|Worker Life 1]], [[problems/lending-marketplaces/worker-life-2|Worker Life 2]]

---

## 1. Per-Lender Approval Surface Estimation
#gradient-boosting #logistic-regression #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering #compliance #revenue-impact

**Problem statement:** The ranking that decides which lender a borrower sees is trained on click-through, because approve-or-decline is held by the lender and returned inconsistently or not at all. Borrowers are therefore routed to lenders who will decline them, spending a hard inquiry each time, and the marketplace cannot distinguish its good matches from its bad ones.

**ML task:** Estimation of per-lender approval probability and offered terms conditioned on borrower profile, learned from sparse returned decisions and inferred from funding patterns where decisions are absent
**Input data:** Borrower profiles as submitted, including soft-pull bureau attributes where available; routing decisions and lender rankings; returned decisions and terms where partnerships provide them; funding notifications; repeat visits by the same borrower across lenders and time; lender-published eligibility criteria; observed approval rate shifts by profile band.
**Target:** Probability of approval per lender per profile, and the distribution of terms actually offered conditional on approval.
**Evaluation metric:** Calibration on the subset of lenders that do return decisions, held out by lender rather than by row — the useful question is whether the model transfers to a lender whose decisions it has never seen, since that is the operating condition for most of the network. Downstream, the metric that matters is realised approval rate per routed borrower and inquiries spent per funded loan, both of which the marketplace can measure without any lender's cooperation.
**Scope:** The binding constraint is commercial rather than technical: decision return has to become a condition of participation, with better-matched traffic as the consideration. Even sparse returns across large volume produce a usable approval surface, and the model transfers across lenders with similar published criteria. Inquiry cost should enter the objective explicitly, because every routing decision spends a fraction of the borrower's credit profile and nothing currently accounts for it. 3 ML engineers, 7 months.
**Data availability:** Profiles and routing are complete internally. Decisions and terms are the missing piece and the entire point; funding notifications exist wherever the fee depends on them, which provides a partial label even today.

---

## 2. Lead Conversion Prediction from Submission Behaviour
#gradient-boosting #logistic-regression #k-means-clustering #change-point-detection #bert #evaluation-metrics #feature-engineering #compliance

**Problem statement:** Leads are priced on traffic source and credit band before anyone knows whether they convert, while the behavioural evidence of the submission itself — how the form was completed, on what device, with what revisions and at what pace — distinguishes a serious applicant from a fabricated or co-registered one far better than the source label does.

**ML task:** Conversion prediction at submission from session behaviour, plus drift detection on traffic source quality
**Input data:** Session behaviour including time to complete, field revision patterns, navigation path, device and network characteristics; submitted profile; traffic source and affiliate chain; historical leads with funding outcomes; consent capture records; complaint and litigation history by source.
**Target:** Probability of funding, and a per-source behavioural fingerprint whose drift indicates an upstream change.
**Evaluation metric:** Ranking quality on funding outcome measured within traffic source rather than across it, since source explains much of the variance and the value here is discriminating inside a source. For drift detection, the metric is lead time before aggregate conversion moves — a partner whose behaviour profile has shifted is detectable days or weeks before the revenue impact appears, which is the difference between a bad week and a bad quarter.
**Scope:** Fabricated lead detection falls out of the same behavioural model and is worth separating in reporting, since the remedy is contractual rather than pricing. Contact burden modelling belongs here too: the number of calls a consumer receives after one submission is knowable, is the largest single driver of complaints and litigation exposure, and is currently nobody's optimisation target. 2 ML engineers, 5 months.
**Data availability:** Excellent. Session telemetry, submissions and funding outcomes are all held; consent records are captured through certification vendors in a replayable form.

---

## 3. Lender Catalogue Extraction and Silent Change Detection
#large-language-models #bert #k-nearest-neighbors #change-point-detection #word-embeddings #evaluation-metrics #data-integration #workflow-orchestration

**Problem statement:** Hundreds of lender products with eligibility criteria, rate grids and state restrictions are maintained by hand against lenders who change pricing and criteria without notice. A stale entry means a borrower is shown an offer that does not exist, which is both a bad experience and a disclosure problem.

**ML task:** Extraction of structured eligibility and pricing from lender-published material, plus statistical detection of undisclosed criteria changes from outcome distributions
**Input data:** Lender product pages, rate sheets and terms documents; existing catalogue entries and their revision history; state licensing registries; observed approval and funding rates by profile band over time; displayed offers versus terms actually received where decisions return.
**Target:** Structured catalogue entries with provenance, and an alert when a lender's realised behaviour diverges from its stated criteria.
**Evaluation metric:** Extraction accuracy per field against the human-maintained catalogue, with a strong preference for flagging ambiguity over asserting a value, since a wrongly extracted minimum score misroutes borrowers silently. For change detection, the operative metric is how many days earlier the system identifies a criteria change than the lender's own notification, measured against historical cases the partner team already knows about.
**Scope:** Silent change detection is the higher-value half and needs no document processing at all — a collapse in approval rate for a specific profile band is visible in the marketplace's own outcome data before any email arrives. The advertised-versus-received rate gap is the most useful statistic the marketplace could compute about a lender and is currently computed by nobody, including regulators. State eligibility should be validated against public licensing registries rather than maintained as an unverified matrix. 1 ML engineer and 1 data engineer, 4 months.
**Data availability:** Lender material is public. Outcome distributions are internal. Licensing registries are public and machine-readable.

---

## 4. Approval Rate Change Decomposition for Partner Management
#causal-inference #gradient-boosting #hypothesis-testing #confidence-intervals #change-point-detection #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** A lender complains that lead quality has fallen. Often the real cause is that the lender tightened its own underwriting, and the partner manager suspects this and cannot demonstrate it, because the decisions live in the lender's system. Every renewal negotiation is conducted without the evidence that would settle it.

**ML task:** Decomposition of observed approval and funding rate changes into traffic composition effects and lender behaviour effects
**Input data:** Delivered lead profiles over time with full attribute distributions; funding and decision returns where available; source mix; seasonality; comparable lenders' conversion on similar profiles; lender-side events such as published rate changes; bid and acceptance behaviour.
**Target:** An attribution of any period-over-period change in approval or funding rate to composition versus lender behaviour, with a confidence interval.
**Evaluation metric:** Validated against cases where the lender later confirmed an underwriting change — a small but real set that every partner team can assemble from memory and email. The standard to meet is that the decomposition would have correctly identified the cause before the confirmation arrived. Reweighting-based estimates should be reported with their overlap diagnostics, since the composition adjustment is only meaningful where the profile distributions genuinely overlap.
**Scope:** This is the artefact the role most needs and is computable from data the marketplace already holds, without any lender's cooperation. Cohort-consistent reporting — comparing like traffic across periods — removes most disputes before they start, because most of them are uncontrolled composition effects. Anonymised cross-lender benchmarking tells a lender whether their problem is the traffic or themselves and should be handled with care about what is competitively disclosable. 1 ML engineer and 1 analyst, 4 months.
**Data availability:** Complete internally for the composition side. The lender-behaviour side is inferred rather than observed, which is precisely why the decomposition is valuable.
