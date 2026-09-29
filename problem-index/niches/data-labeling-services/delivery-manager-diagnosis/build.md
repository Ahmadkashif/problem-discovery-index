# A Complaint, Five Examples and No Cause

**Niche:** [[niches/data-labeling-services/delivery-manager-diagnosis/profile|The Delivery Manager]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Delivery managers receive a customer complaint that the data is bad, with a handful of examples and no diagnosis, and spend the week working backwards through a pipeline that records everything except why.
**Tags:** #k-means-clustering #gradient-boosting #descriptive-statistics #bayesian-inference #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to turn a customer complaint that the data is bad into a diagnosis with a cause — and whoever does that takes delivery, because the escalation is currently a week of working backwards through a pipeline that records everything except why.

## The Problem
An email arrives on Tuesday: the last batch is unusable, here are five examples. The delivery manager looks at the five. Two are genuinely wrong, two are defensible readings of an ambiguous guideline, and one is the customer misunderstanding their own specification. Establishing that takes two days. Establishing whether the batch as a whole is affected, and by what, takes the rest of the week: querying annotator assignments, comparing against earlier batches, checking whether the guideline changed, and finding that a cohort onboarded three weeks ago was trained on a superseded version. Every one of those facts was in the pipeline on Tuesday morning.

## Why Nobody Has Built This
The pipeline was built to route work and record outcomes, and diagnosis was not a use case, so the events exist and are not joined. Guideline versions are frequently not recorded against the items annotated under them, which makes the most common cause unprovable. The delivery manager is an operations role without analytical tooling, and the analysis is bespoke every time. And the escalation is experienced as a relationship problem, which routes it to account management rather than to instrumentation.

## What to Build
Diagnose from the pipeline automatically. Link the customer's examples to their full pipeline history — annotator, time taken, revisions, reviewer, guideline version, training cohort — in one action, which turns the first two days into a screen. Test the candidate causes systematically: is the affected set concentrated in particular annotators, a particular cohort, a particular task subtype, a particular guideline version, a particular reviewer, or a particular period — each of which is a straightforward comparison and collectively covers nearly every real cause. Report the cause with its evidence and its scope, so the conversation with the customer is about a specific finding and a specific remedy rather than about whether the data is bad. Version the guideline against every item, since guideline drift is among the commonest causes and is currently unprovable. Distinguish a vendor cause from a specification cause, because a meaningful share of these escalations are the customer's criteria not having been agreed, and establishing that early changes the conversation entirely. Detect the pattern before the customer does, which the fix note addresses. And accumulate the diagnoses, since the same causes recur and a delivery organisation that knows its own failure distribution can prevent rather than diagnose.

## Target Customer
Delivery organisations and the managers carrying escalations, and the customers who would rather receive a diagnosis than a week of silence.

## Impact If Built
Every fact the diagnosis needs is recorded and unjoined, which is why a knowable answer takes a week. Linking examples to their pipeline history and testing the standard causes systematically converts an escalation from a relationship event into a finding.
