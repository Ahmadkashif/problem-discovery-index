# The Segments Nobody Breaks Out

**Niche:** [[niches/identity-verification-vendors/error-distribution-accounting/profile|Error Distribution Accounting]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The pass rate is reported as one number, and every segmentation that would be informative is available in the same table.
**Tags:** #descriptive-statistics #quick-win #evaluation-metrics #confidence-intervals #automation #compliance #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to be the first to publish how its error rates are distributed across the populations it decides about — and whoever produces that number defines the standard everyone else is then measured against.

## The Problem
Reporting aggregates everything into one figure. The same data supports breaking it down by document type, document age, device model, operating system, capture condition, time of day, jurisdiction, applicant age band and retry count — all of which are recorded on every attempt and none of which require any sensitive data at all. Any one of those breakdowns would tell a customer more about their gate than the aggregate ever will, and none are produced.

## Why It's Still Broken
The aggregate was what the first dashboard showed, so it became the metric — a number that is easy to compute and easy to compare becomes the one everyone asks for, and nothing displaces it. Segmentation invites questions nobody has prepared answers for. Customers do not know to ask. And nobody has framed these breakdowns as the uncontroversial first step they are.

## What a Fix Looks Like
Break out what is already there. Report pass and failure rates by document type and age, which is the fix and requires no new data, no demographic inference and no methodology debate. Add device class and operating system version, since the pattern there is stark and is a product issue rather than a policy one. Report by retry count and abandonment, as the applicant who failed twice and left is the outcome that matters and is entirely observable. Break out by jurisdiction, which surfaces coverage gaps immediately. Show the failure stage rather than only the outcome, because knowing whether people fail at capture, matching or data resolution determines what to fix. Report sample sizes and intervals, so small segments are read appropriately. Give customers the breakdown for their own population, since theirs differs from the vendor average. Flag segments performing materially below the rest, which is a short list and is the work queue. Do this before the harder demographic measurement, as it is uncontroversial, immediately useful and builds the practice. And set a cadence, because a one-off analysis decays.

## Who Feels the Pain
Customers with an uninterpretable aggregate; applicants failing in segments nobody looks at; product teams with no prioritisation signal; and policy functions unable to assess their own gate.

## Impact If Fixed
A number that is easy to compute and compare becomes the one everyone asks for, and nothing displaces it. Segmenting by document type, device and retry needs no new data and no methodology debate, and it is the uncontroversial first step toward the harder measurement.
