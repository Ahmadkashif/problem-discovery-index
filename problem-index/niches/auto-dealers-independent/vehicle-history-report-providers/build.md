# Source Coverage as a Measured Quantity, Not an Assumption

**Niche:** [[niches/auto-dealers-independent/vehicle-history-report-providers/profile|Vehicle History Report Providers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A clean history report means either that nothing happened to the vehicle or that nothing was reported, and the provider cannot tell the buyer which — because coverage is tracked as a source count rather than as a measured probability.
**Tags:** #probability-distributions #bayesian-inference #confidence-intervals #gradient-boosting #evaluation-metrics #hypothesis-testing #feature-engineering #causal-inference #data-integration #revenue-impact

## The Problem
The product's central weakness is silence. Every report that comes back clean carries an unstated claim — that the absence of events means the absence of history — and that claim is false to an unknown degree. Reporting is voluntary for most source types, uneven by state, patchy by shop, and thin in certain years and regions. A vehicle repaired at a shop outside the reporting network, or titled in a state with weak brand reporting, produces a clean report indistinguishable from a genuinely clean vehicle. The provider knows this in aggregate and cannot express it per vehicle. Coverage is managed as a business development metric — how many sources are contributing — rather than as a per-report statistical property, so the one number that would make the report honest is the one number it does not contain.

## Why Nobody Has Built This
Quantifying coverage means quantifying ignorance, and the commercial instinct has always been that a report expressing uncertainty is a weaker product than one that does not. There is also a real methodological difficulty: measuring what a source did not report requires knowing what happened, which is exactly the missing information. The tractable version requires triangulation — cross-source overlap, vehicles that appear in one feed and not another, and known-outcome sub-populations — and none of that is trivial to assemble. Because the naive version is impossible and the sophisticated version is hard, the question has stayed unasked.

## What to Build
A coverage model that estimates, for a specific vehicle, the probability that a material event would have been captured given where it has lived, when, and what kind of event it is. It is built from what the provider already holds: overlapping coverage between independent sources, which reveals each source's capture rate where they intersect; geographic and temporal reporting density; and calibration against sub-populations where ground truth is available — auction condition reports, insurance total loss records, fleet histories. The output is a per-report confidence characterization by event class, so a clean report on a vehicle that spent six years in a well-covered market says something genuinely different from a clean report on a vehicle titled across three thin-coverage states. Internally, the same model turns source acquisition from an opportunistic activity into a targeted one, because it identifies precisely which gaps most degrade report reliability and therefore which feeds are worth what to acquire.

## Target Customer
Chief data officers and heads of data acquisition at history report providers, and the dealer and lender clients who currently make inventory and collateral decisions on reports whose reliability is unstated.

## Impact If Built
Converts the product's biggest unaddressed weakness into a differentiator. A provider that can state confidence per vehicle is offering something a competitor with similar raw coverage cannot, and it is exactly what a lender underwriting collateral or a dealer buying sight-unseen actually needs. It also makes data acquisition spend measurable for the first time — currently the industry's largest recurring investment, justified by source count rather than by effect on report reliability.
