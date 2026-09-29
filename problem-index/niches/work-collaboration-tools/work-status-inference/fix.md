# Nobody Measures Whether the Status Was True

**Niche:** [[niches/work-collaboration-tools/work-status-inference/profile|Work Status Inference]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Fix (Pain Point)
**One-liner:** Every report, dashboard and portfolio view in the category rests on self-reported status fields, and no organisation has ever measured how often those fields were accurate.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #change-point-detection #quick-win #automation #worker-facing
**Contested on:** Every serious competitor in work management is fighting to say what is actually happening from the activity the tools already captured rather than from what somebody typed — and whoever makes status observed rather than reported takes the category's founding promise.

## The Problem
A portfolio review shows sixty initiatives with statuses, dates and confidence indicators. Everyone in the room knows the data is approximate and nobody knows by how much. A green initiative may be green because it is fine or because nobody has updated it since kickoff. The meeting proceeds to make resource and sequencing decisions on the basis of it. The measurement that would characterise the reliability — how often a status was correct, how stale fields are, how far in advance a slip was flagged — is computable from the platform's own history and has never been produced.

## Why It's Still Broken
Nobody owns status quality. The project managers who maintain it are measured on delivery rather than on data, the platform vendor treats the field as customer data, and leadership treats the report as the best available. Measuring it would show that a substantial share of the portfolio view is stale, which reflects on the process everybody is participating in and is therefore a finding nobody commissions.

## What a Fix Looks Like
Measure staleness and accuracy from the platform's own record. Field age — how long since each status was updated, distributed across the portfolio — is a single query and is the cheapest possible improvement, because a dashboard that greys out items untouched for three weeks tells a reviewer immediately which parts of the picture to trust. Retrospective accuracy: for every task and initiative that completed, what did the status say at intervals beforehand, and how far in advance was a slip first reflected — which produces the one number that matters, lead time on bad news. Analyse it by team and by initiative type, since the pattern is usually structural rather than individual: some kinds of work reliably report late. And show the divergence between reported status and observed activity, which is the same signal the build note produces and is useful immediately even without a full inference model. None of this requires new data; it requires the history of a field to be treated as data rather than as a current value.

## Who Feels the Pain
Leaders making decisions on a portfolio view of unknown reliability; project managers blamed for surprises that the reporting structure guaranteed; and teams whose genuine early warnings are lost among stale green indicators.

## Impact If Fixed
Field staleness is a query and immediately changes how a portfolio view is read. Lead time on bad news is the metric this whole category should be judged by and is currently unmeasured anywhere — and it is computable retrospectively from any organisation's existing history, which means the first measurement can be made this week.
