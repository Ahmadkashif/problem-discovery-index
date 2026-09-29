# The Stream Nobody Came To

**Niche:** [[niches/live-commerce-platforms/stream-discovery/profile|Stream Discovery]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A seller prepares for hours, goes live to eleven viewers, sells nothing, and is given no reason and no second chance by a system that has already decided.
**Tags:** #evaluation-metrics #survival-analysis #descriptive-statistics #revenue-impact #confidence-intervals #worker-facing #quick-win #hypothesis-testing
**Contested on:** This niche is not terminal — the fight over cold-start ranking and the fight over the ranking objective are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A seller sources inventory, photographs it, schedules a show, and performs for two hours to eleven people. Nothing sells. They are told nothing about why — whether the time was wrong, the category saturated, the opening minutes weak, or whether the system simply never surfaced them. They try twice more and stop. The platform records this as a seller who churned, and the ranking that caused it was optimising a viewer-side metric that improved slightly. Supply is the scarce side of a live marketplace and the discovery system is quietly destroying it without the loop ever being measured.

## Why It's Still Broken
Discovery is evaluated on viewer engagement, and seller outcomes are a different team's metric if they are anyone's. The feedback a seller would need is a ranking explanation, which platforms avoid giving because it invites gaming. Cold-start starvation is statistically invisible in aggregate — the median stream looks fine. And churned sellers do not complain, they leave.

## What a Fix Looks Like
Close the loop between ranking and supply. Measure impressions delivered per new seller as a first-class metric, which is the fix's foundation and is not currently reported anywhere — a cohort that receives no distribution is identifiable on day one. Guarantee a minimum exploration allocation to new sellers, funded explicitly as supply acquisition rather than left to the ranker's discretion. Tell the seller what happened in terms they can act on: how many viewers were shown the stream, how many entered, how long they stayed, where they left — which is diagnostic rather than an explanation of the ranking and so does not invite gaming. Recommend a schedule from actual category demand by hour, since time slot is the seller's largest controllable variable and they currently guess. Flag the recoverable cases — a stream with good entry and poor retention is a content problem, one with no impressions is a distribution problem, and the two get opposite advice. Track seller survival by cohort against distribution received, which makes the marketplace cost of the ranking visible. Intervene before the third failed show, since that is where churn concentrates. And report seller retention alongside viewer engagement in the discovery team's own dashboard, because a metric owned elsewhere is a metric that loses.

## Who Feels the Pain
New sellers who invest and are never surfaced; the platform losing the scarce side of its marketplace invisibly; and viewers seeing an increasingly concentrated set of the same hosts.

## Impact If Fixed
Cold-start starvation is invisible in aggregate and fatal per seller, and churned sellers leave without complaining. Impressions per new seller is measurable on day one, and distinguishing a distribution failure from a retention failure gives the two cases opposite advice.
