# The Medical Visit Billed as a Routine Exam

**Niche:** [[niches/optometry-practices/routine-vs-medical-visit-billing/profile|Routine-vs-Medical Visit Billing]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Practices leave medical revenue on the table by sending visits with real medical findings to the vision plan by default, and no report shows them how often it happens.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to bill each eye exam to the payer its findings support, vision plan or medical, and whoever collects the most revenue per exam that survives payer audit takes the account.

## The Problem
A patient with a vision plan reports flashes, or the doctor finds early cataract, dry eye or a retinal finding and orders a scan. The visit still goes to the vision plan for its fixed exam fee, and the OCT is written off or charged to the patient. The doctor assumes billing handled it. Billing assumes the doctor would have said.

## Why It's Still Broken
Nobody owns the gap. The OD documents findings, the biller follows habit, and the EHR reports claims submitted, not claims that should have been medical. Fear of audit pushes practices toward the vision plan, and the plans have no reason to point out the difference.

## What a Fix Looks Like
A weekly retrospective report that scans finished visits for medical complaints, diagnoses and tests billed only to a vision plan. It estimates the revenue difference and lists the visits still inside the medical plan's filing window for correction. Over time the same signals move upstream into a checkout prompt.

## Who Feels the Pain
Owner optometrists, whose medical revenue never grows, and billing staff, who are blamed when an audit eventually finds the opposite error.

## Impact If Fixed
If a practice finds ~5 such visits a week at ~$50–$80 each, the report recovers ~$13,000–$20,000 a year (estimate) and shows the owner exactly which doctors and complaints drive the loss.
