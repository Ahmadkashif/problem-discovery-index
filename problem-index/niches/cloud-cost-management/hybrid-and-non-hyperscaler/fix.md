# Migration Cases Built on an Incomplete Comparison

**Niche:** [[niches/cloud-cost-management/hybrid-and-non-hyperscaler/profile|Hybrid & Non-Hyperscaler Estates]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Fix (Pain Point)
**One-liner:** A migration business case compares a fully-loaded cloud estimate against an on-premise figure that omits the licences, the facilities and the people, and the answer is therefore predetermined.
**Tags:** #descriptive-statistics #linear-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #revenue-impact #compliance
**Contested on:** Every serious competitor here is fighting to produce one total cost for a workload that spans cloud, colocation, licensed software and owned hardware — and whoever does that takes the enterprise, because no tool currently sees more than a fraction of it.

## The Problem
A migration case compares the projected cloud bill — complete, itemised, provided by a tool — against the current on-premise cost, which somebody assembles from the hardware refresh budget and a share of the facilities line. It omits the licences that will not transfer, the ones that become more expensive per core in the cloud, the network circuits that stay, the staff who do not leave, and the hardware whose depreciation continues regardless. Three years later the cloud spend exceeds the projection and the on-premise cost did not fall as expected, and the retrospective blames execution rather than the comparison. The same arithmetic, applied in reverse, produces equally unreliable repatriation cases.

## Why It's Still Broken
The cloud side has a tool and the on-premise side has a spreadsheet, so the two sides of the comparison are assembled with entirely different rigour. Nobody owns the methodology, so each case is built by whoever is making it, with assumptions chosen by someone who usually has a preferred conclusion. Committed costs that survive a migration are the most commonly omitted item and the least obvious. And nobody revisits a completed migration against its case, so the errors never feed back.

## What a Fix Looks Like
Standardise the comparison and make both sides equally complete. A defined cost taxonomy applied identically to both options — infrastructure, licences, facilities, network, operations, support — so that omission on one side is visible rather than silent, which is the core fix and requires no new data. Explicit treatment of committed and stranded costs: what continues regardless, what ends at a renewal date, what can be avoided immediately, since this is the most commonly omitted category and frequently reverses the conclusion. Licence treatment modelled properly, because the cost of the same software can differ substantially between deployment models and this is regularly discovered after the decision. Sensitivity analysis on the two or three assumptions that dominate, with the break-even stated, which is more useful than a point estimate and is what an executive should be shown. A stated time horizon consistent with the depreciation and the contracts, rather than one chosen to suit the answer. And a retrospective against the case after the fact, which is the only mechanism by which the organisation's estimates improve and which essentially nobody does.

## Who Feels the Pain
Executives approving cases built on asymmetric comparisons; infrastructure teams held to projections that were never achievable; and organisations that migrated or repatriated on arithmetic nobody has revisited.

## Impact If Fixed
A common taxonomy applied to both sides makes omissions visible and requires no new data, and the committed-cost treatment frequently changes the conclusion outright. The retrospective is what makes the next case better and is skipped almost universally.
