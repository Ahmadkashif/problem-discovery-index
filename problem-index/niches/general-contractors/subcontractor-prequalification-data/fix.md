# Qualification Is a Point-in-Time Snapshot of a Moving Business

**Niche:** [[niches/general-contractors/subcontractor-prequalification-data/profile|Subcontractor Prequalification Data]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** A subcontractor is qualified on an annual statement and then takes on three large jobs, loses a key superintendent, and runs out of working capital — none of which is visible until the next annual review.
**Tags:** #change-point-detection #survival-analysis #gradient-boosting #evaluation-metrics #confidence-intervals #time-series-forecasting #feature-engineering #data-integration #compliance #revenue-impact

## The Problem
Qualification runs on an annual cycle because financial statements are annual. Contractor risk does not move annually — it moves when a firm wins more work than it can staff, when a large customer stops paying, when a bonding line is pulled, when key people leave. A subcontractor qualified in March on last year's statement can be materially different by September, and the general contractor awarding work in September is relying on the March assessment. The failures that hurt most — a sub going under mid-project — are almost always visible in the months beforehand to somebody, and the qualification platform is not looking.

## Why It's Still Broken
The annual statement is the anchor artefact and everything was built around it. Continuous signals — liens filed, judgments, bonding changes, hiring and layoff activity, payment behaviour reported by other contractors — are available but scattered, and none is individually conclusive, so acting on them requires a model rather than a rule. And the commercial framing is a qualification event rather than a monitoring service, which shapes both the product and what customers expect to pay for.

## What a Fix Looks Like
Continuous monitoring between qualification cycles, built on signals that move faster than statements: lien and judgment filings, bonding and insurance changes, workforce indicators, backlog growth reported through the platform, and payment behaviour where contributed. Individually weak, jointly informative, evaluated as a change from the qualified baseline rather than as absolute thresholds. A material deterioration triggers a re-qualification request rather than an alarm, which keeps the platform in its assessment role. The most valuable output is the one general contractors would act on immediately: a watchlist of currently engaged subcontractors whose risk has moved since they were qualified, which is the question a project executive asks constantly and nobody can answer.

## Who Feels the Pain
General contractors awarding work on stale assessments; project teams discovering a subcontractor's distress when crews stop appearing; sureties and lenders exposed to the same failures; and the platform, whose product is a snapshot in a business that changes quarterly.

## Impact If Fixed
Turns an annual event into a continuous service, which changes both the product and its revenue shape. It also directly addresses the failure the whole category exists to prevent — a subcontractor collapsing mid-project — which annual qualification structurally cannot catch.
