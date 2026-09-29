# Source Evaluation Adapted to Marginal Linkage Contribution

**Niche:** [[niches/collections-agencies/identity-skip-trace-data-providers/profile|Identity Resolution & Skip Trace Data Providers]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data catalogue and quality platforms profile a source's completeness and freshness; the question that decides whether to license it is what it adds to a graph that already has a thousand others.
**Tags:** #graph-theory #graph-neural-networks #evaluation-metrics #feature-engineering #dimensionality-reduction #mutual-information #hypothesis-testing #confidence-intervals #data-integration #automation

## The Problem
Source acquisition is the largest recurring cost in the business and the decisions are made on weak evidence. A prospective source is evaluated on record count, coverage geography, refresh frequency, and price, sometimes with a sample match test against existing records. What actually matters is marginal contribution: how many identities does this source resolve that the existing graph cannot, how much does it improve confidence on links already present, and which population segments does it reach that current sources under-cover. Those questions are answered impressionistically, which means the portfolio accumulates overlapping sources whose combined value is far below their combined cost, and gaps persist in segments nobody has measured.

## What Already Exists
Data quality and catalogue tooling is a strong market. Collibra, Alation, Monte Carlo, and the open-source profiling libraries all handle source profiling, completeness and freshness monitoring, schema drift, and lineage well. Record matching test harnesses are straightforward to build on existing entity resolution platforms.

## The Customization Gap
All of that evaluates a source in isolation or against a schema. Marginal contribution is a question about a graph — how a new source changes the connected structure of an identity network with a thousand existing inputs — and no general tool has a representation for it. The adaptation is a graph-aware evaluation harness: a candidate source is ingested into a sandbox graph, and the measurement is the change in resolution rate, link confidence, and segment coverage relative to the production graph without it. Redundancy has to be measured as information overlap rather than as record overlap, since two sources with identical record counts can contribute very differently depending on which links they enable. Coverage must be reported by population segment, because the segments a source uniquely reaches — thin-file consumers, recent movers, populations under-represented in credit data — are precisely where the graph is weakest and where the marginal value is highest. And with field outcome data available, the harness can measure a source's contribution to accuracy rather than only to resolution rate, which is the distinction that matters and that no profiling tool can express.

## Target Customer
Heads of source acquisition and identity science at data providers, and the finance leaders approving eight-figure annual data spend on evidence that currently amounts to coverage counts.

## Impact If Solved
Turns the single largest cost line into a measured investment. Segment coverage measurement also directs acquisition toward the populations the graph resolves worst, which is where customers experience the most failure and where a competitor is unlikely to have looked either.
