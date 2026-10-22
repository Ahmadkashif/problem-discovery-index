# Machine Learning Opportunities — Life Insurance Carriers

**Industry:** [[life-insurance-carriers|Life Insurance Carriers]]
**Derived from:** [[problems/life-insurance-carriers/high-impact|High Impact]], [[problems/life-insurance-carriers/low-impact-1|Low Impact 1]], [[problems/life-insurance-carriers/low-impact-2|Low Impact 2]], [[problems/life-insurance-carriers/worker-life-1|Worker Life 1]], [[problems/life-insurance-carriers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Underwriter's Read of an APS
#tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #evaluation-metrics #feature-engineering #worker-facing

**Problem statement:** Senior life underwriters read attending physician statements and "see" risk the manual does not score: a trend across normal-range results, a specialist's hedged language, missed follow-ups, interacting mild impairments. The ML problem is to extract a structured medical timeline from the APS and learn, from senior underwriters' historical decisions and overrides, the adjustments they make beyond the manual's debits and credits.

**ML task:** Document understanding and medical entity extraction into a dated timeline (seq2seq / LLM extraction with page grounding), then multiclass classification of risk class with an auxiliary model of senior-underwriter debit adjustments
**Input data:** Scanned and faxed APS pages, lab panels, prescription and medical-claims histories, MIB codes, application disclosures, the carrier's underwriting manual, workbench decision records (final class, debits, requirements ordered), case notes, and the senior underwriters' overrides of junior or rules-engine proposals.
**Target:** Page-linked findings (diagnosis, value, date, trend); the risk class a panel of senior underwriters assigns; the size and direction of their adjustment versus the manual-only worksheet.
**Evaluation metric:** Extraction precision and recall on findings that change the class, with recall weighted higher, since a missed cardiac finding costs mortality and a spurious one costs a minute. For class prediction, agreement with a senior-underwriter consensus panel on held-out cases, reported against the panel's own test-retest agreement as the ceiling, plus the share of cases placed more than one class away (the expensive errors). Longer term, actual-to-expected mortality by predicted versus assigned class on early-duration and contestable claims.
**Scope:** The data collection challenge comes first. The workbench never stored the reasoning, so the system must capture it during the task, through low-effort confirm/edit actions on a proposed worksheet, and backfill history by aligning case notes to APS pages. The labelling challenge is that underwriters disagree with each other and with themselves, so a sample of cases must be re-underwritten blind by several seniors to measure intra- and inter-rater reliability before any model is trusted. Mortality labels are too sparse per impairment to train on directly. The deployment challenge is that the summary must arrive within minutes of the APS and be faster than the underwriter's own skim, or it is ignored. 2 ML engineers, 1 underwriting SME and a medical director, 9–12 months, with value arriving first as page-linked summarisation.
**Data availability:** Carriers hold years of APS images and decisions, though decision records are thin. Reinsurer facultative quotes give a second expert label on referred cases. HIPAA authorisations, state privacy law and New York's Circular Letter No. 7 govern use and require documented fairness testing.

---

## 2. Accelerated Underwriting Mortality Slippage Monitoring
#survival-analysis #causal-inference #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** Accelerated programmes issue cases without fluids or exams on the strength of data-driven triage. Estimate, by segment, the mortality cost of misclassification relative to full underwriting, using random-holdout and post-issue-audit samples, and detect drift in the triage model before it shows up in claims.

**ML task:** Causal estimation of class-shift impact from audited samples, projected to mortality through a survival model of class-specific hazard; drift detection on triage inputs and pass rates
**Input data:** AU decisions and triage scores; random-holdout cases fully underwritten in parallel; post-issue audits with APS and labs; early-duration claims and contestable investigations; lapse; reinsurer pricing assumptions.
**Target:** Class-shift matrix (AU versus full underwriting) by segment; implied mortality load (slippage) with interval; drift alarms.
**Evaluation metric:** Coverage of slippage confidence intervals in back-tests, and time-to-detection of a simulated deterioration. The cost is asymmetric: under-estimating slippage mis-prices a whole cohort for decades. The SOA's 2024 monitoring covered 33,000+ lives across 30 programmes, which shows how small audited samples are, so intervals matter more than point estimates.
**Scope:** Modest modelling, hard sampling design. The holdout must be truly random and large enough per segment. 1 actuary and 1 data scientist, 4–6 months, then continuous.
**Data availability:** Carriers and their reinsurers hold the holdout and audit data. Most programmes are reinsured, so analysis often needs the reinsurer's cooperation.

---

## 3. Dynamic Lapse and Surrender Prediction for Annuities
#gradient-boosting #survival-analysis #time-series-forecasting #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Predict policy-level surrender, partial withdrawal and income-rider election for fixed indexed, fixed-rate and registered index-linked annuities as functions of moneyness, surrender-charge schedule, crediting gap versus new-money rates and owner characteristics, for assumption-setting under LDTI and VM-22 and for retention outreach.

**ML task:** Competing-risks survival model (surrender, withdrawal, annuitisation, death) with gradient-boosted hazards and rate-sensitivity features
**Input data:** Policy histories from admin systems, crediting rates and caps by period, competitor new-money rates, surrender-charge schedules, rider status, distribution channel, owner age and state; pooled industry studies where licensed.
**Target:** Monthly hazard of each exit type; expected surrender at the end of the surrender-charge period.
**Evaluation metric:** Out-of-time calibration of aggregate surrender by cohort and moneyness bucket. The rate-shock period of 2022–2023 is the critical back-test. Calibration under stress matters more than discrimination, because reserves and hedges depend on tail behaviour.
**Scope:** Data are mostly internal and clean enough. The difficulty is regime change: few carriers have experience through a rising-rate shock at today's product mix. 2 data scientists with an actuary, 4 months.
**Data availability:** Internal admin data; pooled studies (Ruark, LIMRA, SOA) give industry benchmarks to participants.

---

## 4. Disability Claim Duration and Return-to-Work
#survival-analysis #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #worker-facing

**Problem statement:** From the first weeks of a long-term disability claim, predict expected duration and the probability of return to work within 6, 12 and 24 months, so examiners and nurse case managers intervene where it changes the outcome, and claim reserves reflect the file rather than a table.

**ML task:** Survival regression on claim duration with time-varying covariates extracted from medical records
**Input data:** Diagnosis codes, occupation and its demands, benefit amount and replacement ratio, offsets, age, employer, attending physician restrictions extracted from records, vocational assessments, prior claims.
**Target:** Time to recovery, return to work, settlement or death; probability of transition at the own-occupation change.
**Evaluation metric:** Concordance and time-dependent calibration. The operational metric is uplift: claimants flagged and contacted versus a randomised control, because a model that only predicts who would recover anyway adds nothing.
**Scope:** 1 data scientist, 1 NLP engineer, a clinical SME, 6 months. The uplift test needs operations' cooperation.
**Data availability:** Carriers hold closed-claim histories over decades; records are PHI under HIPAA authorisations.

---

## 5. Annuity Best-Interest Review Triage
#large-language-models #bert #transformers #k-nearest-neighbors #evaluation-metrics #compliance #automation

**Problem statement:** Classify each annuity application and replacement by suitability risk so reviewers spend time on the few files with real consumer harm, and detect boilerplate rationales repeated across a producer's files.

**ML task:** Document extraction plus binary classification of escalate/approve; near-duplicate detection on producer rationale text
**Input data:** Applications, consumer profile forms, producer rationale, replacement comparison forms, statements of surrendered contracts, prior review decisions and complaints.
**Target:** Escalate versus approve as reviewers decided; rationale similarity clusters by producer.
**Evaluation metric:** Recall on files reviewers escalated, held near 1.0; a missed unsuitable replacement is a regulatory and consumer harm. Then reviewer time per file and the auto-clear rate at that recall.
**Scope:** 1 ML engineer, 1 compliance SME, 4 months. The model triages and never approves alone.
**Data availability:** Carriers hold years of review decisions; reasons are thinly recorded and should be captured going forward.
