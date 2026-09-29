# The Report That Describes Last Week

**Niche:** [[niches/restaurant-tech-platforms/fsr-pos-operations/profile|Full-Service Restaurant POS & Operations]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every restaurant platform's analytics answer what happened, an operator's every question is about what to do next, and the gap between the two is filled by a manager doing arithmetic on a phone between shifts.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #workflow-orchestration #worker-facing #quick-win #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
The daily report arrives: net sales, covers, average check, labour percentage, item mix, comps and voids. All accurate, all about yesterday. The manager's questions are whether to cut a server at two o'clock, whether to run the special tonight, whether the salmon order should be increased before the weekend, and whether the labour percentage is bad because sales were soft or because the schedule was wrong. None of those are answered, and each is answerable from the same data with a different framing. So the manager exports to a spreadsheet, or more often does it in their head, and the platform's contribution to the decision is the number they started from.

## Why It's Still Broken
Reporting was built to satisfy the owner's question at the end of the day rather than the manager's question during it, and once a reporting suite exists, adding another chart is always cheaper than rethinking what a report is for. The decision-framing work also requires the vendor to have an opinion about restaurant operations — what a good labour deployment looks like on a Tuesday — which is a heavier commitment than displaying a number. And the customers ask for reports, because reports are what they know to ask for.

## What a Fix Looks Like
Reframe the same data as decisions with a recommended action and the reasoning behind it. Labour percentage becomes "you are two hours over on the floor for the pace you are running; the cut with the least service impact is the two o'clock busser," computed from the current sales pace against the same daypart historically. Item mix becomes a prep recommendation with the items most likely to run out flagged before service rather than after. Variance analysis decomposes a bad labour week into scheduling error versus sales miss, which is the distinction that determines what the manager should change and is never made. None of this needs a new model — it needs the existing numbers expressed as the choice being made, at the moment it is being made, which is a product decision the whole category has deferred.

## Who Feels the Pain
Managers doing arithmetic between shifts; owners who see a labour percentage and cannot tell whether to blame the schedule or the weather; and vendors whose reporting suites are comprehensive and unopened.

## Impact If Fixed
Decision framing converts existing reporting into something acted on during the shift rather than reviewed after it, which is where restaurant margin is actually made. The scheduling-versus-sales variance decomposition is the cheapest single improvement available and answers the most frequently argued question in restaurant management.
