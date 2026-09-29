# Measurement-Based Care Instruments Wired to Level-of-Care Decisions

**Niche:** [[niches/healthcare-practice-software/behavioral-health-ehr/profile|Behavioral Health & SUD Practice Software]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** PHQ-9, GAD-7 and the rest of the measurement-based care battery are free, validated, universally available instruments that every behavioral health platform already collects and none of them connects to the decision the scores were designed to inform.
**Tags:** #survival-analysis #logistic-regression #time-series-forecasting #change-point-detection #evaluation-metrics #confidence-intervals #revenue-impact #worker-facing
**Contested on:** Every serious competitor in behavioral health software is fighting to share a patient record with a referring provider while withholding exactly the 42 CFR Part 2 material and proving it did so — and whoever makes that segmentation reliable takes the account.

## The Problem
A patient completes a PHQ-9 at intake and again every few weeks. The scores are stored, graphed on a tab nobody opens, and reported to a payer as evidence that measurement-based care is being practised. They do not influence anything. The clinician's judgment about whether this patient is improving, whether the treatment should change, and whether the level of care is right is formed from the session, and the instrument sits beside it as documentation. Meanwhile the utilisation reviewer who decides whether to authorise continued treatment is making the same judgment from a narrative note, with the quantitative series available and unused by both sides.

## What Already Exists
The instruments themselves are the most solved thing in behavioral health: validated, free, brief, with published clinically significant change thresholds and reliable change indices. Collection tooling is a commodity — Greenspace, Owl, Blueprint and the native modules in every major platform all do it. Payers increasingly require the scores. The entire apparatus for collecting is bought; the apparatus for using is missing.

## The Customization Gap
The adaptation is to treat the score series as a signal and connect it to the two decisions it can actually inform. It requires: (1) modelling each patient's trajectory rather than the latest value, with the practice's own population as the reference, so that "not improving" is a statement about an expected curve rather than about a threshold; (2) flagging non-response early enough to matter — the published literature on early change as a predictor of outcome is the basis, and the flag must arrive at week four rather than week sixteen; (3) attaching the trajectory to the level-of-care and continued-authorisation documentation automatically, so the reviewer sees the series rather than a sentence about it; (4) surfacing deterioration and risk-item responses as an alert rather than as a chart the clinician must open; and (5) presenting all of it as information to a clinician rather than as a rule, because an instrument-driven discharge criterion is a payer's dream and a clinical hazard, and the product should say so plainly.

## Target Customer
Behavioral health groups under value-based or authorisation-heavy contracts, and the platforms serving them that currently collect scores as a compliance artefact.

## Impact If Solved
Early non-response flagging is the single best-evidenced intervention available in this niche and is achievable with data the practice already holds. Attaching the trajectory to authorisation documentation shortens review cycles and reduces denials for medical necessity, which is the largest administrative cost in the setting. The clinical gain and the reimbursement gain point the same way here, which is rare in this industry and worth stating.
