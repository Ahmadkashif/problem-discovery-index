# Buy: Rater Calibration From Assessment Science

**Niche:** Severity Calibration
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Educational assessment and clinical research solved the problem of many humans rating the same kind of thing consistently, and bounty triage treats each rating as an independent act of judgement.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #expectation-variance-covariance #maximum-likelihood-estimation #data-integration
**Contested on:** Whether a finding's severity can be referenced against how comparable findings were rated across the whole market, or remains one programme's private judgement.

## The Problem

Many people rating many items against a common scale, where the ratings have consequences and the raters differ systematically, is a thoroughly studied problem. Educational assessment faced it with essay scoring, clinical research with diagnostic and outcome adjudication, and both developed the same apparatus: model rater severity explicitly, model item difficulty explicitly, calibrate raters against reference items with known values, detect drift, and report scores adjusted for who happened to do the rating.

Bounty triage does none of it. Each severity assignment is treated as an independent judgement by a competent person. Rater severity is not modelled, so a researcher's outcome depends partly on which triager picked up their submission. Nobody calibrates against reference items. Drift is undetected. And the resulting rating is reported as a property of the finding rather than as a joint product of the finding and the rater.

The techniques transfer almost directly. The data exists. The gap is that nobody in this industry has treated triage as a rating problem.

## What Already Exists

Assessment science: item response theory and many-facet Rasch measurement, which jointly estimate item difficulty and rater severity and are standard in high-stakes testing; rater certification and calibration against benchmark items; drift monitoring across a scoring window.

Clinical research: adjudication committees with defined criteria for endpoint classification, blinded independent review, and inter-rater reliability reporting as a standard part of trial conduct.

Annotation tooling for machine learning: Labelbox, Scale, Surge and Prolific, with gold-standard injection, annotator agreement statistics and calibration feedback — the most operationally similar existing tooling, built for a different industry with the same structure.

Security-specific: CVSS with its defined vector, EPSS for exploitation likelihood, SSVC for decision-oriented triage — vocabularies that exist and are applied loosely.

## The Customization Gap

**No gold-standard items anywhere.** The single most transferable idea. A maintained set of findings with adjudicated reference severities, seeded into triage workload, would give immediate per-triager calibration data. Annotation platforms have done this for a decade; no bounty platform does it.

**Rater severity is not modelled or corrected.** Many-facet models would separate the triager's disposition from the finding's actual severity, and the correction is the part researchers would care about most — their outcome currently depends on queue assignment.

**Difficulty has an analogue and no name.** Some findings are genuinely contested and some are obvious. Treating a disagreement on a borderline case the same as one on an unambiguous case is the same error assessment science corrected with difficulty modelling.

**Blinding is possible and unused.** Clinical adjudication blinds the assessor to information that would bias them. A triager who can see the researcher's reputation and the programme's remaining budget is exposed to both, and neither should influence a severity assessment.

**Context must be a covariate, not noise.** Assessment models assume items are comparable. Here the same finding legitimately differs by asset context, so the model needs conditioning rather than the straightforward rater-item decomposition.

**Volume and latency.** Assessment calibration runs over a scoring window of days. Triage runs continuously with same-day service levels, so the calibration has to be online rather than batch.

## Target Customer

The annotation platforms are the most credible adapters — their calibration, gold-standard and agreement tooling is almost exactly right, they operate at volume, and security triage is an adjacent market they already touch.

The bounty platforms are the buyers, and the internal argument is quality and dispute reduction: a large share of severity disputes originate in rater variance nobody has measured.

Assessment science vendors would bring the modelling rigour and would need the operational context, which makes a partnership the likely shape.

## Impact If Solved

Gold-standard items are cheap, immediate and would reveal per-triager severity differences that currently contaminate every rating in the system. This is the fastest available improvement.

Correcting for rater severity would remove the dependence of a researcher's payout on which analyst happened to open their submission, which is an unfairness nobody has ever measured.

And blinding triagers to reputation and budget would remove two influences that should not touch a severity assessment and almost certainly do.
