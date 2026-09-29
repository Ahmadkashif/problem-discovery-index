# Inspector Judgment Is Recorded as a Percentage

**Niche:** [[niches/general-contractors/construction-fund-control-inspection/profile|Construction Fund Control & Draw Inspection]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** An inspector notices that the same three trades have been absent for two months and that the superintendent has changed twice, forms a view that the job is in trouble, and files a report containing percentages.
**Tags:** #tacit-knowledge-ml #bert #transformers #word-embeddings #evaluation-metrics #descriptive-statistics #k-means-clustering #data-integration #worker-facing #workflow-orchestration

## The Problem
The most valuable thing an experienced inspector produces is not the percentage complete — it is the judgment about whether a project is going well, formed from things that do not appear on the form: crew size trending down, materials not arriving, a contractor who has stopped returning calls, a site that is too clean for the stage it claims to be at. Some of that reaches the narrative section of the report; most of it stays with the inspector. So the firm's accumulated field intuition, which is the difference between an inspection service and a data-entry service, is neither captured nor transferable, and a lender reading a report with no adverse narrative cannot tell whether the inspector saw nothing or wrote nothing.

## Why It's Still Broken
Inspection forms were designed to support a draw calculation, which is a numeric output, and narrative is treated as optional colour. Inspectors are paid per inspection and measured on turnaround, so anything beyond the required fields is unpaid time. And the qualitative signals are exactly the kind that feel unprofessional to record without certainty — an inspector reluctant to write that a job feels wrong will say nothing rather than flag it.

## What a Fix Looks Like
Structured capture of the observational signals as checkboxes and short prompts rather than as free narrative: trade presence, crew size relative to stage, material staging, site organization, personnel changes, and a simple confidence-rated view on whether the project is tracking. Costing seconds, phrased so an inspector can record an impression without asserting a conclusion. Aggregated, those signals become the leading indicators the distress model needs and the thing that most distinguishes a good inspector from an adequate one — which is currently invisible and therefore untrainable. Consistency between inspectors on comparable sites becomes measurable. And a lender receives, alongside the percentages, a structured picture of what the inspector actually observed, which is the substance they are paying for and currently get only when an inspector chooses to write it down.

## Who Feels the Pain
Inspectors whose field judgment leaves no trace and cannot be developed; regional managers with no instrument to measure who is good; lenders receiving reports whose silence is ambiguous; and the firm, whose differentiating expertise is delivered as arithmetic.

## Impact If Fixed
Converts field intuition into a recorded, trainable, and modellable asset, which is the difference between a commodity inspection service and a risk intelligence one. It is also the prerequisite for the distress model — a prediction of project failure needs the signals experienced inspectors actually use, and today none of them are written down.
