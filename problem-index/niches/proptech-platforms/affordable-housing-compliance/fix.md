# The File Rebuilt the Week Before the Audit

**Niche:** [[niches/proptech-platforms/affordable-housing-compliance/profile|Affordable Housing Compliance]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A compliance review is announced, and a property spends the following week reconstructing tenant files that were complete when they were created and have not been checked since.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in affordable housing software is fighting to produce a tenant file that passes a compliance review without a specialist rebuilding it by hand — and whoever gets first-pass audit rate highest takes the portfolio.

## The Problem
A state agency schedules a review. The compliance team pulls the sample, opens each file, and finds the predictable things: a missing signature page, a verification form that expired before the certification was executed, a household composition change that was never documented, an annual recertification completed eleven days late. Each is fixable in principle and several are not fixable retroactively. The week before the review is spent in a state of controlled alarm, and the findings that emerge could all have been identified at any point in the preceding year by the same check being run continuously.

## Why It's Still Broken
File completeness is assessed by a specialist reading a file, and specialists read files when there is a reason to. Nothing runs the check automatically, because the check was never encoded — it lives in the specialist's knowledge of what a reviewer looks for. The system holds the documents and the dates and has no concept of a file being complete or incomplete. And the organisational rhythm reinforces it: compliance staff are fully occupied with current certifications, so retrospective checking never rises above the queue until an audit forces it.

## What a Fix Looks Like
Run the audit continuously against every file. Encode the completeness and timeliness criteria a reviewer applies — required documents present, signatures and dates in the correct order, verification validity windows respected, recertification within the required timeframe, household composition changes documented — and evaluate every file every night. Report a file-level status and a portfolio-level readiness figure, with the specific deficiency named and the ones that are still curable distinguished from the ones that are not. Alert on timeliness obligations before they lapse, which is the category of finding that is entirely preventable and entirely common. Keep the criteria as versioned content updated as programme guidance changes, in the same way court rules content is maintained. None of this needs modelling; it needs the reviewer's checklist written down in a form the system can run.

## Who Feels the Pain
Compliance specialists losing a week to reconstruction and carrying the anxiety of findings they cannot fix; owners facing findings with financial consequences; and residents whose files carry errors nobody caught.

## Impact If Fixed
Continuous file auditing converts an event into a standing condition and prevents the entire class of timeliness findings, which are the most common and the most avoidable. Portfolio readiness as a standing number is also the metric an owner and an investor both want and neither currently has.
