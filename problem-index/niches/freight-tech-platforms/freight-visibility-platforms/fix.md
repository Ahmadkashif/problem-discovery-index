# Nobody Publishes Visibility Accuracy

**Niche:** [[niches/freight-tech-platforms/freight-visibility-platforms/profile|Freight Visibility Platforms]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Visibility platforms compete on coverage percentages and integration counts, and none of them publishes how accurate its ETAs are or how complete its tracking actually was, so a shipper selecting a platform is choosing on the wrong numbers.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #change-point-detection #compliance #quick-win #automation
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A shipper evaluates two visibility platforms. Both claim high coverage. Neither states what proportion of tracked shipments had continuous location versus a single ping, what proportion of ETAs fell within thirty minutes of actual arrival, or how those figures vary by carrier size, by lane and by mode. The shipper selects on integration count and brand, deploys, and discovers over six months that coverage on its small-carrier freight is poor and that its ETAs are not usable for dock planning — which was the reason it bought the product.

## Why It's Still Broken
Publishing accuracy means publishing a number that will sometimes be unflattering, in a market where the competitor does not, so the first mover is punished. The measurement is also genuinely ambiguous without a standard: coverage can mean a carrier is connected, or that a shipment received any ping, or that it was continuously tracked, and each vendor uses the definition that suits it. There is no industry standard definition, no neutral benchmark, and no shipper consortium demanding one — which is what allows the ambiguity to persist.

## What a Fix Looks Like
Define the measurements and publish them, and let a shipper verify them against their own freight. Coverage is decomposed into connected, pinged and continuously tracked, with the definitions stated. ETA accuracy is reported as the distribution of error against actual arrival, segmented by lane, mode, carrier size and lead time — because the aggregate hides exactly the cases where the product fails. Tracking gaps are reported as gaps rather than interpolated over. A shipper should be able to run the same computation on its own historical data and get the same answer, which is what makes the published figure credible. The vendor that publishes first takes a short-term competitive hit and gains the only defensible position in a market where everyone else is claiming coverage percentages nobody has defined.

## Who Feels the Pain
Shippers selecting platforms on numbers that do not describe performance; logistics coordinators who learned not to trust an ETA and plan around it; and the platform that is genuinely more accurate, which currently has no way to demonstrate it.

## Impact If Fixed
Published, verifiable accuracy changes the basis of competition in this category from coverage claims to performance, which is what shippers have wanted and been unable to obtain. It costs nothing to compute — every platform already holds actual arrival times against its own predictions — and the obstacle is entirely a willingness to be measured.
