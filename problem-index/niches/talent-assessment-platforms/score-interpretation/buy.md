# Buy: Decision Support Patterns Adapted to a Noisy Individual Estimate

**Niche:** [[niches/talent-assessment-platforms/score-interpretation/profile|Score Interpretation by Hiring Managers]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clinical and financial decision support has decades of practice in presenting uncertain scores to non-statisticians; assessment reports present a number and a colour.
**Tags:** #confidence-intervals #bayesian-inference #evaluation-metrics #descriptive-statistics #compliance #workflow-orchestration #worker-facing #hypothesis-testing
**Contested on:** Whether uncertainty communication practice from higher-stakes domains transfers to a hiring screen.

## The Problem

Communicating an uncertain quantitative estimate to a non-specialist decision-maker is a well-studied problem. Clinical risk communication, diagnostic test reporting, credit scoring disclosure and weather forecasting have all developed practice, evidence and conventions for it — how to render intervals, when to use frequencies rather than probabilities, how to prevent a threshold becoming a cliff, and how to phrase what the estimate does not say.

Assessment reporting has adopted none of it. The convention is a number, a percentile, a band and a colour, which is approximately the least informative rendering available and the most likely to be over-read.

## What Already Exists

Clinical risk communication research and its conventions. Diagnostic test reporting standards with sensitivity, specificity and predictive value framing. Credit score disclosure requirements. Decision support interface patterns from clinical systems. Uncertainty visualisation research. Behavioural work on how people misread thresholds and point estimates.

## The Customization Gap

**The decision-maker is untrained and transient.** A clinician has training in diagnostic reasoning and uses the system daily. A hiring manager makes a few hiring decisions a year and has no statistical training. The presentation has to work with no prior knowledge and no repetition, which pushes toward plain-language statements over visualisations requiring interpretation.

**The subject is a person being compared to other people.** Clinical risk communication concerns one patient. Here the manager is ranking a list, which invites exactly the fine distinctions the instrument cannot support. Ranking interfaces need design specifically to discourage over-reading — grouping into bands, randomising within bands, and resisting a sortable column.

**The consequence is exclusion, not treatment.** A misread clinical score leads to a different intervention. A misread assessment score means someone is not hired, with no feedback and no appeal, and the asymmetry argues for conservative presentation.

**Legal defensibility shapes the record.** The report is potentially evidence. What it said, what guidance accompanied it and how it was used need to be recorded in a way clinical decision support does not require.

**The combination problem is specific here.** Assessment plus interview plus resume screening, measuring overlapping constructs, weighted by intuition. Clinical decision support has multi-test combination methodology worth borrowing, and nothing in assessment reporting attempts it.

## Target Customer

Assessment vendors designing score reports, who should be reading the clinical risk communication literature and are not. Also employers' assessment functions specifying what they want from vendors, and the decision support and visualisation specialists for whom this is an unserved application.

## Impact If Solved

The uncertainty communication conventions, interval rendering practice and multi-test combination methodology get borrowed, and the untrained-transient decision-maker, ranking context, exclusion asymmetry, evidentiary record and assessment-interview combination get designed for. Concretely: a report that a hiring manager reads correctly without any training.
