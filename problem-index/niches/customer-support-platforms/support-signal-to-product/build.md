# The Product Defect Signal With a Cost Attached

**Niche:** [[niches/customer-support-platforms/support-signal-to-product/profile|Support Signal to Product]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Support holds a continuous census of everything wrong with a product and delivers it to product teams as anecdotes in a meeting, because nobody has computed what any of it costs.
**Tags:** #bert #large-language-models #k-means-clustering #change-point-detection #evaluation-metrics #confidence-intervals #revenue-impact #causal-inference
**Contested on:** Every serious competitor with a support corpus is fighting to turn it into a product defect and friction signal the product organisation actually acts on — and whoever closes that loop takes a use of the data nobody currently serves.

## The Problem
A product manager prioritises a quarter. On the list: features from customer research, a strategic initiative, and technical work engineering has requested. Not on the list: the confusing flow that generated four thousand support contacts last quarter, the error message that produces a contact eighty percent of the time it appears, and the settings page that accounts for a fifth of all product-related tickets. Support knows all of it. Support's representation in the prioritisation conversation is a manager saying customers find this confusing, which loses to a feature with a revenue estimate — not because the product manager is unreasonable but because one side brought a number.

## Why Nobody Has Built This
Support categorisation exists to route, so the taxonomy describes which team handles a ticket rather than what in the product failed, and no amount of reporting on it produces a product signal. The organisational separation is the deeper cause: support tooling is bought by support and the product organisation is not a user, so no vendor has built for them. And computing the cost of an issue requires joining contact volume to handle time, escalation, refunds and churn, which crosses the same boundary.

## What to Build
A product-oriented classification over the support corpus, with a cost attached to every cluster. Tickets are classified against a taxonomy of what actually broke — this feature, this flow, this error, this integration, this document — derived from the corpus rather than from the routing categories, which is the foundational change and is a clustering problem with abundant data. Each cluster carries its cost: contacts, agent time, escalations, refunds and credits issued, and where the data supports it the churn associated with customers who raised it — which turns a qualitative complaint into a figure comparable with a feature's revenue estimate. Emerging clusters are detected as they appear rather than when they become large, which is the single most valuable output and is what lets a regression be caught in days rather than in a quarter. The output is delivered where product teams work rather than in a support dashboard, since a report in a system they do not open is the current state. And the whole thing is pointed at friction as well as defects, because the flows that generate contacts without anything being broken are the largest and least visible category.

## Target Customer
Product organisations, support platform vendors seeking a second buyer, and the voice-of-customer vendors whose input is currently surveys rather than the far richer corpus next door.

## Impact If Built
Support contact volume is the most honest measure of product friction that exists and it does not participate in prioritisation because it has no number. Attaching cost makes it comparable with everything else on the list, and emerging issue detection converts a quarterly anecdote into a days-old alert — which is the difference between catching a regression and explaining it.
