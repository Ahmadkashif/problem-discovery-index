# Watching a Customer Walk Into a Known Failure

**Niche:** [[niches/database-platform-vendors/fleet-corpus-anti-patterns/profile|Fleet Corpus & Anti-Patterns]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same anti-patterns recur across thousands of customers, each discovers them independently during an outage, and the vendor watching all of them uses the corpus for capacity planning.
**Tags:** #k-means-clustering #graph-theory #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor that gets here is fighting to warn a customer about a failure thousands of other customers have already had — and whoever does that holds a corpus of how databases actually fail that no single organisation can assemble.

## The Problem
A customer's schema has a pattern the vendor has seen thousands of times: a table with a particular index arrangement and growth rate whose dominant query will flip to a sequential scan at a predictable size. The vendor's fleet contains hundreds of instances of this exact situation, with the outcome in every case. The customer is four months from the failure. Nothing warns them. In four months they will open a ticket describing an incident the vendor could have predicted with a confidence interval, and a support engineer will explain a pattern they have explained many times.

## Why Nobody Has Built This
Cross-customer analysis of schemas and workloads is sensitive, and no vendor has done the work to define a form that customers would accept — so the topic is avoided rather than designed, even though structural patterns disclose nothing about any customer's data. The fleet is also organised operationally rather than analytically: the telemetry exists for capacity and health rather than as a corpus, and turning it into one requires a deliberate investment with no immediate demonstrable output. And support knowledge remains prose, which cannot be executed against anybody's system.

## What to Build
Turn the fleet into a pattern library that executes. Represent every customer's schema, index structure, query shapes, growth rates and configuration structurally — with no data content, which is both sufficient and what makes the governance position defensible and statable publicly. Mine for recurring configurations that precede incidents, joining structure to subsequent outcomes across the fleet, which produces an empirically grounded anti-pattern catalogue rather than a documented opinion. Attach a timeline to each pattern, since the useful warning is not that this design is risky but that it fails at approximately this data volume, which the fleet's observations supply directly. Run the catalogue against every customer continuously and warn with the evidence and the remedy, which is the whole product. Publish the recurrence rates, because knowing that a pattern affects a large share of customers is both a public good and a strong reason for a customer to act. Feed the catalogue into the developer-facing checks and the degradation detection in this industry's other niches, since it is the same knowledge delivered at different moments. And build the governance in: structure only, aggregation thresholds before publishing a pattern, customer opt-in, and a public statement of what is analysed.

## Target Customer
Managed database vendors, primarily; and the platform teams who would receive warnings months before an incident they cannot currently anticipate.

## Impact If Built
The corpus is unique, the patterns are structural, and the vendor currently watches customers walk into failures it has observed a thousand times. Attaching an empirical timeline to each pattern is what converts generic best practice into an actionable warning with a date.
