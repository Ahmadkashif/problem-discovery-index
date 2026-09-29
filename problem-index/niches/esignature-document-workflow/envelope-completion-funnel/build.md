# Diagnosing the Stall While It Can Still Be Saved

**Niche:** [[niches/esignature-document-workflow/envelope-completion-funnel/profile|Envelope Completion Funnel]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A large share of agreements sent for signature never complete, for ordinary reasons the platform can see, and every vendor reports only that the envelope is outstanding.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #decision-trees #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to know why an envelope has stalled while it can still be saved and to act on that reason automatically — and whoever raises completion rate takes the account, because completion is the number the buyer already reports.

## The Problem
An envelope goes out on the fourth. It is opened twice on the fifth and not signed. Three automatic reminders follow on the seventh, eleventh and fifteenth. On the twenty-ninth someone in deal desk phones the recipient and learns that the signer left the company in July, that the person now responsible never received it, and that in any case procurement would have needed to review clause nine before anyone signed. The platform recorded the opens, the silence, the reminders and the eventual void, and at no point had a view about what was wrong — despite the pattern being one of a handful that account for most stalls and being distinguishable in the data by the end of the first week.

## Why Nobody Has Built This
The category's commercial model is per-envelope, so a sent envelope is already revenue and completion is the customer's problem rather than the vendor's. The product surface grew around the sending workflow, and outcome analytics were built as reporting — counts of outstanding — rather than as diagnosis. Stall reasons are not labelled anywhere: no platform asks why a voided envelope was voided, so the target variable for the interesting model does not exist as a field even though the evidence for it sits in the event stream. And the intervention is the awkward part, because acting on a diagnosis means contacting the counterparty, which vendors have been reluctant to do on the sender's behalf.

## What to Build
Stall diagnosis as a first-class product surface. Classify every in-flight envelope into a small set of actionable stall types — wrong recipient, unavailable recipient, no-context abandonment, internal approval block, term under dispute, technical or delivery failure — each of which has a different remedy and each of which has a distinguishable signature: never opened at all is a deliverability or context problem; opened repeatedly and not signed is a content problem; opened, forwarded and silent is a routing problem; signed by two of four and stopped is a sequencing problem. Predict stall risk at send time from the envelope's own characteristics — length, number of signers, routing order, recipient domain, whether the recipient has signed for this sender before, time of week — so that a high-risk send can be corrected before it goes out. Replace the fixed reminder schedule with the remedy the diagnosis implies: re-route, escalate internally, surface the disputed clause to the sender, or send a contextual note rather than a fourth identical nudge. And close the loop by asking, once, what happened to voided envelopes, which creates the labelled data the whole capability needs and which nobody currently collects.

## Target Customer
Revenue operations and legal operations at companies with meaningful agreement volume, and the signature platforms themselves, for whom completion rate is the most defensible differentiator left in a commoditising category.

## Impact If Built
Completion is the industry's own metric and nobody works it. The stall types are few, distinguishable and each has a specific remedy, which makes this an unusually well-shaped problem; the improvement lands directly on revenue recognised in the period rather than on a productivity abstraction.
