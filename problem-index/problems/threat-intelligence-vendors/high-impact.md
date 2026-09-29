# Selling Intelligence Whose Value Cannot Be Checked

**Industry:** [[threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** High Impact
**One-liner:** The success case is an attack that did not happen, so the category is sold on collection breadth and analyst credentials and renewed on whether the customer feels informed.
**Tags:** #causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #survival-analysis #gradient-boosting #evaluation-metrics #compliance

## The Problem
A customer buys intelligence and receives indicators, finished reports, adversary profiles and alerts. At renewal, the question is whether it was worth the spend, and there is no way to answer it. An indicator that blocked something might have blocked an attack or a stale address reassigned to a legitimate service. A report that was read might have changed a decision or been filed. The absence of a breach is not evidence, because most organisations do not have breaches most years.

The proxies used instead are activity measures. Volume of indicators, number of reports, coverage of adversary groups, speed of publication. All describe the vendor's output and none describes the customer's outcome, which is the same failure that runs through every assurance business in this cluster.

The relevance problem compounds it. Most of what a broad feed contains has no bearing on a given organisation, and the portion that does is not distinguished — so the customer pays for volume, filters it with their own scarce analyst time, and cannot tell whether the useful fraction justified the cost.

Two proxies are available and unused. Whether an indicator ever matched anything in the customer's own telemetry is directly observable. Whether the match was a true positive is observable too, from the investigation outcome. A vendor could report, per feed and per customer, the match rate and the precision — and essentially none do, because the numbers would be low and because a vendor without telemetry access cannot compute them at all.

The vendors bundled with endpoint products can compute both across a large installed base. That is a structural advantage they use for collection and not for measurement.

## Why It's Unsolved
The counterfactual is genuinely unobservable and that has been accepted as a reason not to measure anything. It is a reason not to measure prevented incidents; it is not a reason to avoid measuring match rate, precision, timeliness relative to the customer's own detection, or whether a report was read and acted upon.

Telemetry access is the practical barrier for standalone vendors. Measuring whether an indicator matched requires seeing the customer's logs, which customers are reluctant to share with an intelligence vendor and which the endpoint-bundled competitors get by default.

The commercial incentives are the usual ones. Published precision numbers would be uncomfortable, would enable comparison between vendors, and would move the market from breadth toward accuracy — which advantages some vendors and disadvantages others, and nobody wants to go first.

And the buyer's position is weak. Security leaders buy intelligence partly because their peers do, partly because a framework or an insurer expects it, and partly for genuine reasons — and none of those purchase drivers demands a measurement, so none is supplied.

## What a Solution Looks Like
Measure match rate and precision per feed and per customer segment. How often a feed's indicators appear in an organisation's telemetry, and what share of those matches turned out to be real, are computable wherever telemetry is available and are the closest thing to a product measurement this field can have. Publishing them by segment — this feed matches at this rate with this precision for organisations of your size in your sector — would change how the category is bought.

Measure timeliness against the customer's own detection. Intelligence that arrives after the customer's own tools flagged the activity added nothing; intelligence that arrived first added lead time. That comparison is directly computable and is the clearest available evidence of value.

Track whether finished reporting changed anything. Reports that were read, reports that generated a hunt, hunts that found something — a chain the customer can record and the vendor can learn from, converting finished intelligence from a publication into a measurable input.

Report relevance honestly at the point of delivery. A vendor that told a customer which fraction of a feed is applicable to their stack, sector and exposure would sell less volume and more value, which is the trade the category has avoided making.

## Impact If Solved
This is a multi-billion-dollar market whose product quality is undemonstrable and therefore unpriced, so it competes on collection breadth and reputation. Match rate, precision, timeliness against the customer's own detection, and report-to-action tracking are all computable and would give buyers the first basis for comparison the category has ever had — and the endpoint-bundled vendors could publish them tomorrow from telemetry they already hold.
