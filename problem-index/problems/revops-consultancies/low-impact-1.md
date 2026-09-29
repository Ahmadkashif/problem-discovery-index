# CRM Data Quality as a Measured Quantity

**Industry:** [[revops-consultancies|RevOps Consultancies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Everyone agrees CRM data is bad, every vendor sells enrichment and validation, and almost nobody measures the specific distortions that actually break the analysis built on top of it.
**Tags:** #gradient-boosting #change-point-detection #hypothesis-testing #dbscan #confidence-intervals #evaluation-metrics #data-integration #feature-engineering

## The Problem
CRM data quality is discussed as completeness — missing fields, stale contacts, duplicate accounts — because that is what enrichment vendors sell against. The distortions that matter for revenue analysis are different and behavioural.

Stages are advanced when a manager asks for movement rather than when the customer does something. Close dates are pushed by a fortnight repeatedly because a larger push triggers a conversation, which produces a characteristic sawtooth that any analyst can see and few quantify. Opportunities are created near period boundaries to satisfy activity expectations. Amounts are entered as round placeholders and never corrected. Deals are marked closed-lost with a reason picked from a dropdown in under a second.

Every model built on this inherits the behaviour. A stage-based forecast learns that stage four means a manager asked for an update. An attribution model learns which campaigns were running when someone remembered to fill in a field. And because the distortion is never measured, it is never adjusted for and never even stated as a caveat.

## What Already Exists
Enrichment and validation vendors — ZoomInfo, Clearbit, Apollo, Openprise, Insycle — handle completeness, deduplication and formatting well. CRM-native validation rules enforce required fields. Revenue intelligence platforms like Gong and Clari infer deal state from activity and conversation data rather than from field entry, which is a genuine advance and addresses a slice of the problem. Data observability tooling from Monte Carlo and Bigeye monitors warehouse pipelines rather than behavioural entry patterns.

## The Customisation Gap
The measurable behavioural distortions are specific, computable, and absent from every product: the distribution of close date changes and its sawtooth structure, stage dwell times and skips, the clustering of opportunity creation and stage movement around period boundaries and forecast call days, the proportion of amounts that are round numbers, the time taken to select a loss reason.

Each of these is a number with a trend, and reporting them turns an unfalsifiable complaint into a tracked metric. More importantly, they can be attached to the analysis: a forecast for a segment whose stage data shows heavy manager-driven movement should carry wider intervals than one whose stage transitions follow customer events.

The customisation is that healthy patterns differ by business. A ninety-day enterprise sales cycle and a fourteen-day transactional one have completely different normal dwell time distributions, and a threshold set generically will flag one and miss the other. Each client needs its own baseline, learned from its own history, with drift detection against it.

And the reporting has to be careful. These metrics describe individuals' behaviour and can be read as surveillance, which is both an ethical concern and a practical one — a data quality programme that becomes a performance management tool produces better-looking data and worse-quality data, because people optimise the metric. Reporting at team and process level rather than by individual is the design that actually works.

## Impact If Solved
Every analytical claim in revenue operations rests on this data, and its distortions are known qualitatively and measured nowhere. Turning them into tracked metrics with per-business baselines lets models be adjusted rather than silently biased, lets forecast confidence reflect the quality of the underlying data, and gives a consultancy a diagnostic that opens an engagement with evidence rather than with an assertion everyone already agrees with and nobody acts on.
