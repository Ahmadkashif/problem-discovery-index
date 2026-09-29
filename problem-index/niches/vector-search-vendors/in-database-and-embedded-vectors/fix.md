# Nobody Will Say When You Actually Need One

**Niche:** [[niches/vector-search-vendors/in-database-and-embedded-vectors/profile|In-Database & Embedded Vectors]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Teams adopt a dedicated vector database for a corpus their existing database would have handled, or stay on an extension well past the point it stopped working, because no vendor will publish the threshold.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #time-series-forecasting #data-integration #quick-win #automation #hypothesis-testing
**Contested on:** Every serious competitor in this sub-niche is fighting to be good enough inside the system the developer already runs — and whoever does that takes the market, because the buyer's real alternative is not another vendor, it is not adopting one.

## The Problem
A team with ninety thousand documents adopts a dedicated vector database because the content they read was written by vendors, and spends the next two years operating a second system for a workload their Postgres handled comfortably. Another team stays on an extension until queries take four seconds at forty million vectors, having had no signal that they crossed a threshold, and then migrates under pressure with the application already degraded. Both decisions were made without information that exists and is not published, because publishing it would tell a large share of prospects that they do not need the product.

## Why It's Still Broken
The vendors with the data have a direct interest in the threshold being lower than it is. The extension maintainers are volunteers without a marketing function. The honest answer is conditional on corpus size, dimensionality, query rate, filter selectivity and latency requirement, which makes it a calculator rather than a number — and nobody wants to build a calculator whose most common output is that you do not need us. And the team making the decision has no way to test at a scale they have not reached.

## What a Fix Looks Like
Publish the threshold and the warning signal. Build a calculator taking corpus size, dimensionality, query rate, filter selectivity and latency target, and returning whether an in-database index suffices — which is straightforwardly derivable from benchmarks the vendors already run and is the artefact this whole problem needs. State the crossover conditions explicitly, since they are knowable and currently obscured. Instrument the extension to warn when a deployment approaches its limits — index build time trending up, query latency approaching the target, memory pressure — so a team gets a signal before the wall rather than at it, which is the difference between a planned migration and an incident. Publish migration paths in both directions with realistic effort estimates, because the fear of being trapped is itself a reason teams over-provision early. Report what a deployment is actually using against what it provisioned, which lets an over-provisioned team find out. Be honest in documentation that most applications do not need a dedicated system, which costs some revenue and buys the credibility that wins the deployments that genuinely do. And let a customer run the same benchmark on both, which is the only fully trustworthy answer.

## Who Feels the Pain
Small teams operating a second system they did not need; teams that hit the wall with no warning and migrated in an incident; and vendors whose credibility suffers from advice everyone knows is interested.

## Impact If Fixed
The crossover is knowable from benchmarks vendors already run and is not published because its most common answer is that you do not need us. Instrumenting the extension to warn before the wall turns an incident migration into a planned one.
