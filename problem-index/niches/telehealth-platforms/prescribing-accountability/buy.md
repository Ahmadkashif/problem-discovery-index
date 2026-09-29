# Buy: Payer Prescribing Analytics Adapted to a Platform Auditing Itself

**Niche:** [[niches/telehealth-platforms/prescribing-accountability/profile|Prescribing Pattern Accountability]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Payers have mature prescribing analytics pointed at network providers; here the analysis is pointed inward, at clinicians the platform pays and a model the platform profits from.
**Tags:** #descriptive-statistics #hypothesis-testing #bayesian-inference #confidence-intervals #evaluation-metrics #compliance #data-integration #gradient-boosting
**Contested on:** Whether analytics designed for a payer scrutinising providers can work when the analyst and the subject are the same organisation.

## The Problem

Prescribing pattern analysis is an established discipline on the payer side. Health plans, pharmacy benefit managers and state programmes routinely compute provider-level prescribing rates, identify outliers, adjust for case mix and run intervention programmes, with methodology developed over decades and considerable literature behind it.

Applying it inside a telehealth platform inverts the relationship. The payer analyses providers it does not employ, against an economic interest in reducing prescribing. The platform would analyse clinicians it contracts and pays, against an economic interest that in the direct-to-consumer segment frequently runs the other way. The methodology transfers; the institutional position does not, and the institutional position is what determines whether the analysis gets run and believed.

## What Already Exists

Payer and PBM prescribing analytics platforms. Academic detailing and provider profiling methodology. Case mix and risk adjustment models from the payer world. Guideline-concordance measure specifications from quality bodies. PDMP data and state prescribing dashboards. Statistical infrastructure for hierarchical outlier detection.

## The Customization Gap

**The analyst is the beneficiary of the behaviour being analysed.** Payer analytics carry credibility partly from the analyst's independence. A platform's own analysis of its own prescribing carries none, which means the programme needs structural independence — reporting to a medical director or an independent clinical committee rather than to the business — and external validation to be worth anything to a regulator.

**The data is encounter-level, not claims-level.** Payer analytics run on claims, which are standardised, coded and complete within the plan. Platform data is the encounter record, richer in clinical detail and unstandardised, with the presentation captured in intake responses and free text rather than in a diagnosis code. Defining cohorts from this is a different and in some ways better problem, and it is not what the bought models expect.

**The population is self-selected in a specific way.** Risk adjustment models are calibrated on plan populations. Telehealth users differ — often younger, often seeking same-day access, often without a usual source of care — and the adjustment has to be recalibrated or the comparison to in-person benchmarks is invalid in a direction that flatters nobody.

**The subjects are contractors without institutional protection.** Provider profiling in a health plan operates within a contracted network with dispute processes and professional representation. A contractor clinician flagged as an outlier has none of that, and the fairness apparatus — evidence standard, notification, appeal, what is retained and disclosed — has to be constructed.

**The output has an external audience it was not designed for.** Payer analytics inform internal intervention. Here the likely consumers include regulators, state boards, payers and potentially litigants. That changes the documentation standard, the retention policy and the care with which conclusions are worded, in ways no analytics vendor addresses.

## Target Customer

Platform compliance and medical leadership building a prescribing oversight programme, and the payers and employers contracting virtual care who want the reporting and will otherwise build it themselves from claims. Also the payer analytics vendors, for whom telehealth platforms are a new customer with an inverted use case.

## Impact If Solved

The cohort definitions, risk adjustment methodology and outlier statistics get reused, and the independence structure, encounter-level cohorting, population recalibration, contractor fairness process and external-audience documentation get built deliberately. The practical result is an oversight programme credible enough to be worth having.
