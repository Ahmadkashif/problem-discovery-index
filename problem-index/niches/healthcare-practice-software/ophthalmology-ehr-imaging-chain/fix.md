# The Unbilled Interpretation

**Niche:** [[niches/healthcare-practice-software/ophthalmology-ehr-imaging-chain/profile|Ophthalmology EHR — the Imaging-to-Code Chain]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Ophthalmic imaging codes require a documented interpretation and report, and practices routinely perform the test, form the judgment, act on it clinically, and never write the sentence that makes the test billable.
**Tags:** #large-language-models #evaluation-metrics #descriptive-statistics #compliance #revenue-impact #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor in ophthalmology EHR is fighting to make diagnostic images from every device in the lane arrive in the chart already bound to eye, date and the interpretation that justifies the code — and whoever closes that chain best takes the account.

## The Problem
A physician reviews an OCT on the lane screen, sees the retinal nerve fibre layer is stable, says so to the patient, and moves on. The chart records that an OCT was performed. It does not contain a separate, dated, signed interpretation and report, which is what the code requires and what an auditor looks for. The practice either bills and carries audit exposure, or does not bill and loses the revenue for work that was genuinely performed. Most practices do some of each, inconsistently, and no one can say which. The same physician will not be told about it until a payer audit samples a year of studies.

## Why It's Still Broken
The interpretation exists — it happened, out loud, at the lane — and the documentation requirement asks the physician to restate it in a specific place, in a specific form, at the moment they are least able to. Software has answered with a macro button that inserts boilerplate, which satisfies neither the auditor nor the clinician and which practices are rightly uneasy about, because identical text across hundreds of studies is the pattern an audit looks for. Nobody has instrumented the gap either: no ophthalmic platform reports how many performed studies have a compliant interpretation attached, so the problem has no size and therefore no owner.

## What a Fix Looks Like
Start with the measurement, which needs no modelling: for every billable imaging study performed in the last year, does a distinct, dated interpretation exist, is it separable from the exam note, and does it contain findings rather than a template sentence. That report is computable today and will surprise most practices. Then close the loop at the point of care — surface the study on the lane screen with the prior for comparison, capture the physician's spoken assessment where ambient capture is already deployed, and draft a study-specific interpretation from the measurements the device reported and the physician's own words, for signature rather than composition. Boilerplate detection belongs in the same feature: if the draft is too close to the last fifty, say so before it is signed.

## Who Feels the Pain
Physicians documenting from memory at the end of a clinic; billing staff who must decide whether to submit a code whose supporting documentation they cannot see; and practice owners carrying an audit exposure whose size nobody has measured.

## Impact If Fixed
The compliance report alone typically identifies a meaningful share of performed studies with inadequate or absent interpretations — recoverable prospectively and, more importantly, quantified. Capturing the interpretation at the lane rather than after clinic removes 20-40 minutes of end-of-day documentation per physician and replaces template text with study-specific findings, which is the only version of this that survives an audit.
