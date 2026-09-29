# Rejected by a Reviewer Whose Reasoning You Never See

**Niche:** [[niches/data-labeling-services/the-annotator/profile|The Annotator]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Annotators are paid per task and can have work rejected by a reviewer whose reasoning they never see, on tasks where reasonable experts disagree, with an appeals process that is a form and a wait.
**Tags:** #bayesian-inference #descriptive-statistics #bert #evaluation-metrics #confidence-intervals #worker-facing #compliance #hypothesis-testing
**Contested on:** Every serious competitor that takes this seriously is fighting to make rejection explicable and contestable for the person whose pay depends on it — and whoever does that keeps the capable contributors, which at the expert tier is the whole business.

## The Problem
A contributor spends fourteen minutes on a careful assessment. It is rejected. They see a status change and a category code. They do not know what the reviewer thought was wrong, cannot tell whether the reviewer was right, and have no way to improve because they do not know what to change. The amount at stake is small enough that the appeal — a form, then several days — is not worth their time, so they absorb it. After the third occurrence they take the same expertise somewhere that treats them better, which is a real option for somebody qualified enough to be doing expert annotation.

## Why Nobody Has Built This
The review workflow was built for volume work, where rejections are usually obvious, individually trivial and high in number, and explaining each would be uneconomic. At the expert tier none of those hold and the workflow has not changed. Reviewer accountability is absent because reviewers are also contributors being paid per review, and adding a justification requirement costs their throughput. The appeal process exists to satisfy a policy rather than to resolve disputes, which is visible in its latency. And the contributor's departure is recorded as churn with no cause.

## What to Build
Make rejection informative and contestable. Require a specific reason with the evidence — which part, against which guideline provision, and why — which costs the reviewer a little and is the difference between a contributor who can improve and one who can only leave. Distinguish a rejection for error from a disagreement on an ambiguous item, since the second should not be a rejection at all and currently is, and that distinction requires the ambiguity estimation the quality niche builds. Review the reviewers, comparing their verdicts against the strongest available assessors and against each other, since a reviewer who rejects systematically more than their peers on the same material is a finding and is currently undetectable. Make the appeal fast and cheap, with a decision in hours rather than days and a visible outcome rate, since a slow appeal is a denial with extra steps. Pay for the work when the rejection is overturned, including the appeal effort. Show the contributor their own performance in terms they can act on — where they diverge from strong assessors, on which task types — which is both fair and the fastest route to improvement. And measure churn against its causes, since the departure of capable contributors is the largest cost in expert delivery and its drivers are recorded and unexamined.

## Target Customer
Delivery organisations and marketplaces whose expert supply is their constraint, the contributors themselves, and the customers whose data quality depends on capable people staying.

## Impact If Built
Capable contributors leave over an experience that is cheap to fix, and they leave disproportionately from the careful end, which is the population the expert tier depends on. A specific reason with evidence is a small reviewer cost and the difference between improvement and departure.
