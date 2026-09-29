# Buy: Model Monitoring Tooling Adapted to Employment Decisions

**Niche:** [[niches/talent-assessment-platforms/validity-and-bias/profile|Validity & Bias Measurement]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ML model monitoring and fairness tooling does drift detection and group metrics well; employment decisions have a legal standard, a censored outcome and a subject with rights.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #causal-inference #compliance #descriptive-statistics #automation #survival-analysis
**Contested on:** Whether general ML fairness tooling meets the specific legal and methodological standards of employment testing.

## The Problem

Model monitoring and fairness tooling has matured quickly. Drift detection, performance monitoring, group fairness metrics, explainability and audit logging are available from MLOps vendors and open-source libraries, and the fairness literature has produced well-understood metrics and their impossibility results.

Employment assessment is not a general ML problem. It sits under a specific legal framework with its own definitions, its own evidentiary standards and its own professional guidelines from the psychometrics tradition. The outcome is observed only for those hired. The subject has rights. And the generic fairness metric a library computes may not be the one the applicable standard asks about.

## What Already Exists

MLOps monitoring platforms with drift and performance tracking. Fairness libraries — Fairlearn, AIF360 and others — implementing a range of group metrics. Explainability tooling. The psychometrics tradition with its validation frameworks and professional standards. Bias audit service providers, growing under regulatory pressure.

## The Customization Gap

**The fairness metric is specified by the legal and professional framework, not chosen.** Employment selection has established conventions — impact ratio analysis and the associated professional guidelines — and a vendor's preferred fairness metric from the ML literature is not a substitute. The tooling has to compute what the standard asks about, which is narrower and more specific than a fairness library's menu.

**The outcome is censored by the decision itself.** Performance is observed only for those hired, who scored highly, which is a selection problem central to validation methodology and absent from generic model monitoring. Range restriction correction is standard in psychometrics and unknown in MLOps tooling.

**The criterion is contested, not given.** ML monitoring assumes a ground truth label. Here the criterion is job performance, measured by supervisor ratings that are noisy and themselves potentially biased. Using them uncritically as ground truth imports their bias into every conclusion, which is the most common analytical error in this area.

**Sample sizes are small and the tooling assumes they are not.** A requisition may hire twelve people. Monitoring designed for millions of predictions has no convention for honest inference at these volumes, and reporting a disparity from twelve observations without an interval is worse than reporting nothing.

**The audit trail is legal evidence.** Employment decisions are challengeable and discoverable. Retention, versioning, reproducibility and documentation standards are set by that context rather than by model governance convention, and the difference matters when someone asks what the model was on a specific date.

## Target Customer

Assessment vendors and large employers building monitoring, who will reach for MLOps fairness tooling and need to know where it does not meet the standard. Also the bias audit providers, for whom the methodological gap between a fairness library and an employment validation is where their professional value sits.

## Impact If Solved

The drift detection, monitoring infrastructure and audit logging get reused, and the standard-specified metrics, range restriction correction, criterion scepticism, small-sample inference and evidentiary documentation get built. Concretely: monitoring that would survive a challenge, rather than a dashboard of fairness metrics nobody asked for.
