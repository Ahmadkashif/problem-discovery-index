# The Customer Notices Before the Vendor Does

**Niche:** [[niches/data-labeling-services/delivery-manager-diagnosis/profile|The Delivery Manager]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** A quality problem develops over a week of production, is visible in the vendor's own agreement and timing data throughout, and is first raised by the customer.
**Tags:** #change-point-detection #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #worker-facing
**Contested on:** Every serious competitor that takes this seriously is fighting to turn a customer complaint that the data is bad into a diagnosis with a cause — and whoever does that takes delivery, because the escalation is currently a week of working backwards through a pipeline that records everything except why.

## The Problem
A new cohort joins a project. Their agreement with established annotators is lower from the first day, their completion times are shorter, and their revision rate is near zero — all three visible in the platform from the first batch. Nothing alerts. The pattern continues for eight working days. The customer, reviewing a delivery, notices the quality difference and raises it. The vendor's first indication of a problem in their own production process arrives from outside, which is both operationally poor and the worst possible way for the customer to find out.

## Why It's Still Broken
Monitoring reports throughput and aggregate agreement, and a cohort-level deviation is invisible in an aggregate dominated by the established population. Nobody set thresholds on the leading indicators because nobody identified them as leading indicators. The platform's dashboards are oriented to project progress, which is what delivery management is measured on, and quality is assessed at the review stage rather than monitored during production. And a vendor detecting their own quality problem creates work, which is a mild disincentive that compounds the absence of the mechanism.

## What a Fix Looks Like
Monitor production, not just progress. Track the leading indicators per annotator and per cohort — agreement with established annotators, completion time relative to the task's norm, revision rate, review rejection rate — each of which moves before quality is assessed downstream and each of which is recorded. Alert on cohort-level deviation rather than on aggregates, since a new cohort is a batch and its deviation is exactly what aggregate monitoring hides. Alert on individual deviation too, but distinguish it from a cohort pattern, since the remedies differ completely. Baseline per task type, because the norms differ and a global threshold will fire constantly on hard tasks and never on easy ones. Intervene early with coaching rather than with rejection, since a cohort deviating on day one is a training problem and is cheap to fix then and expensive later. Report the vendor's own detection rate — what proportion of quality issues the vendor identified before the customer — which is the honest operational measure and is currently unmeasured because it has never been claimed. And tell the customer when a problem is found and handled, since a vendor who reports their own issues is in a far stronger position than one who is told.

## Who Feels the Pain
Delivery managers learning about their production problems from a customer; annotators who could have been corrected on day one and are rejected on day eight; and customers whose confidence erodes with each issue they had to raise themselves.

## Impact If Fixed
The leading indicators are recorded and unmonitored, and cohort-level alerting catches the classic batch problem that aggregate monitoring structurally hides. Early coaching costs a fraction of a week of rejected work, and the vendor-detection rate is the operational measure that would make this anybody's priority.
