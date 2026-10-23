# Machine Learning Opportunities — Aircraft MRO & FBO Shops

**Industry:** [[aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Derived from:** [[problems/aircraft-mro-shops/high-impact|High Impact]], [[problems/aircraft-mro-shops/low-impact-1|Low Impact 1]], [[problems/aircraft-mro-shops/low-impact-2|Low Impact 2]], [[problems/aircraft-mro-shops/worker-life-1|Worker Life 1]], [[problems/aircraft-mro-shops/worker-life-2|Worker Life 2]]

---

## 1. A Second Reader for the Borescope Call
#tacit-knowledge-ml #cnns #semantic-segmentation #transfer-learning #survival-analysis #evaluation-metrics #worker-facing

**Problem statement:** Experienced borescope inspectors look at blade, vane and combustor damage and "know" whether it is coating loss or a burn, whether it will progress before the next look, and whether it means pulling the engine. The ML problem is to learn that judgement from inspectors' marked images and from the later teardown truth, and to give every inspector a consistent second read at the engine.

**ML task:** Per-frame semantic segmentation of damage type (nick, dent, burn, coating loss, crack, tip loss) with extent measurement, then blade-level classification into serviceable / reduced interval / unserviceable, plus a survival model for time-to-limit given damage, cycles and engine type
**Input data:** Borescope video and stills with blade index from the turning tool; probe type and calibration; stereo or 3D phase measurements where taken; inspector findings and dispositions from the work order; engine serial, type, thrust rating, cycles since shop visit, exhaust-gas-temperature margin trend; shop-visit teardown findings for the same blade positions when the engine is next opened.
**Target:** Damage masks and measured extent; the inspector's disposition; the teardown-confirmed condition (repairable, scrap, within limits) and the cycles at which a limit was crossed.
**Evaluation metric:** Recall on unserviceable damage, set against inspector-confirmed and teardown-confirmed positives, is the binding metric, since a missed crack is a safety event and a false flag costs a minute of re-inspection. Report agreement with held-out expert marks against the inspectors' own repeat-read agreement as the ceiling (the 2022 University of Canterbury work quoted at ~70% human accuracy sets the bar). For the survival model, use time-dependent concordance and calibration of crossing probability at the next scheduled interval.
**Scope:** The data collection challenge comes first: inspectors must mark findings on screen at the moment of the call, which needs a capture interface that is faster than writing the finding up, and historical stills must be matched to blade positions after the fact. The labelling challenge is that inspectors disagree with each other and with themselves on borderline coating loss and cracks. Labels need repeated reads on a sample to estimate intra- and inter-rater reliability, and the honest label is the teardown finding, which arrives months later from a different shop. The deployment challenge is that the inspector signs, the OEM sets the limits, and the tool must run on a tablet or the borescope screen faster than the next blade rotation. Plan on 2–3 ML engineers, one powerplant engineer and one partner MRO or operator for 9–12 months per engine family before anyone trusts the second read. Measurement consistency and retrieval of past calls on the same stage come first.
**Data availability:** Video exists at modern shops but is poorly indexed. Teardown findings sit with engine MROs and lessors and must be joined by engine serial and blade position under a data agreement. OEMs hold the richest libraries and the limits, and are building their own tools.

---

## 2. AD Applicability and Work-Card Compliance Checking
#large-language-models #transformers #bert #evaluation-metrics #compliance #automation

**Problem statement:** Given an aircraft's configuration (model, serials, installed part numbers, embodied service bulletins) and a draft work package, determine which airworthiness directives apply, whether each work card cites the current revision and an approved method of compliance, and which recurring intervals are due, with the AD paragraph behind every finding.

**ML task:** Structured extraction of AD applicability, compliance and interval clauses into a rule representation; entity matching of work-card text to AD paragraphs; a deterministic rule engine for applicability and due computation with LLM-drafted explanations
**Input data:** AD text from the FAA's Dynamic Regulatory System and the Federal Register (317 final ADs in 2025, 280 in 2024, plus the historic library); referenced service bulletins where licensed; the aircraft's configuration and AD status records; the shop's work cards and engineering orders; AMOC letters on file.
**Target:** Per AD: applies / does not apply / cannot determine (missing configuration fact); per work card: cites current revision, cites approved method, interval correct; a ranked list of gaps.
**Evaluation metric:** Recall on applicable ADs is the binding metric, since a missed applicable AD makes the aircraft unairworthy, while a false "applies" costs a records check. Measure against packages already audited by experienced inspectors and against seeded errors (superseded revisions, wrong baselines). Report the "cannot determine" rate separately, because a checker that refuses honestly is safer than one that guesses.
**Scope:** The extraction is tractable because ADs follow a fixed Federal Register structure. Applicability against configuration is the hard tail, because "except aircraft modified by SB 32-0145" needs the aircraft's own records. Two engineers and an IA-holding inspector, 4–6 months to a checker for one fleet type, then type by type. This is the owner's MVP: it can be demonstrated on public ADs and a synthetic work package before any shop shares data.
**Data availability:** ADs and SDRs are public and free. Work cards and configuration records belong to the shop's customers and need permission. Tracking vendors (CAMP, Traxxall) hold AD status for their fleets.

---

## 3. Non-Routine Findings and Redelivery Forecasting
#gradient-boosting #survival-analysis #feature-engineering #confidence-intervals #workflow-orchestration #revenue-impact

**Problem statement:** At quote and induction, forecast the non-routine labour hours and parts a heavy check or engine shop visit will generate by zone or module; during the event, forecast the remaining duration as cards are raised and blocked.

**ML task:** Quantile regression of non-routine hours and parts cost per zone/ATA chapter; time-to-completion survival model with time-varying covariates (open cards, blocked-on-parts count, inspector availability)
**Input data:** The shop's historical work packages with routine and non-routine cards, hours and parts; aircraft type, age, cycles, operator and environment (coastal, desert); prior check findings on the same tail; parts lead times and stores availability; manpower rosters.
**Target:** Non-routine hours and parts value per zone (10th, 50th, 90th percentile); days to redelivery from each day of the check.
**Evaluation metric:** Pinball loss and interval coverage for the quote forecast, since the planner needs an honest range more than a point estimate. Mean absolute error in days at 25%, 50% and 75% of elapsed check time for redelivery, against the planner's own estimate as baseline.
**Scope:** A gradient-boosting baseline on the shop's own history is achievable in 3 months with one data scientist. The difficulty is data hygiene: non-routine cards coded inconsistently by zone and cause, and parts waits not timestamped. Value grows with the number of checks per type; a shop doing ~50 checks a year on one type has enough after two years.
**Data availability:** Held by the MRO in its maintenance system, though often incompletely structured. Customer-specific findings may be covered by service agreements.

---

## 4. Emerging Failure Detection in Service Difficulty Reports
#bert #word-embeddings #change-point-detection #dbscan #hypothesis-testing #compliance

**Problem statement:** Detect part numbers, ATA chapters and failure modes whose report rate in the FAA's Service Difficulty Reporting data is rising faster than fleet exposure explains, and surface the relevant cluster to a mechanic working on the same part.

**ML task:** Text embedding and clustering of free-text discrepancies into failure modes; change-point detection on exposure-adjusted report rates per part number and mode
**Input data:** SDR yearly files (67,652 reports for 2025, with make, model, part number, JASC code, condition, time and cycles, and a free-text discrepancy averaging ~200 characters); fleet size by type from the FAA registry; the shop's own findings and part removals.
**Target:** Failure-mode cluster labels; alerts for statistically significant rate increases; per-work-card list of related SDRs.
**Evaluation metric:** Precision of alerts as judged by reliability engineers. Lead time against later ADs and service bulletins on the same part, measured retrospectively, is the most persuasive test: did the reports rise before the FAA acted?
**Scope:** One data scientist, 3 months for a first version. The hard parts are inconsistent part-number entry and the heavy skew to air carriers. Boeing and Airbus aircraft account for over three-quarters of 2025 reports, while Cessna has only 1,348, so general aviation signals are thin.
**Data availability:** Public, free and downloadable by year. The shop's own removal and finding data enrich it.

---

## 5. Back-to-Birth Chain Reconstruction for Life-Limited Parts
#large-language-models #graph-theory #k-nearest-neighbors #feature-engineering #data-integration #compliance

**Problem statement:** From a pile of scanned engine records, reconstruct each life-limited part's installation history and cycles back to manufacture, and name every gap that breaks the chain.

**ML task:** Document classification and field extraction (serials, part numbers, dates, cycles, thrust ratings); entity resolution of part identities across superseded part numbers and transcription errors; graph construction with rule-based validation of cycle monotonicity and coverage
**Input data:** Engine log books, operator utilisation statements, shop visit reports, certificates of conformity, 8130-3 and EASA Form 1 tags, LLP status sheets, thrust-rating change records.
**Target:** A per-LLP timeline with cycles used and remaining, a source page for every number, and a gap list (missing period, conflicting cycles, unexplained part-number change).
**Evaluation metric:** Field-level extraction accuracy with zero tolerance for silent errors on cycles and serials. Gap recall against packs already audited by records specialists. Analyst hours per engine before and after.
**Scope:** Two engineers and a records specialist, 5–6 months for one engine family. Handwriting and inconsistent operator formats are the long tail. The graph validation is simple once extraction is trustworthy.
**Data availability:** Records belong to the engine owner (operator or lessor) and are shared with the MRO for each shop visit. Building a training set needs permission from owners or synthetic packs built from public formats.
