# The Only Asset a Competitor Cannot Copy

**Niche:** [[niches/cloud-cost-management/cross-organisation-benchmarking/profile|Cross-Organisation Benchmarking]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These vendors observe what thousands of organisations actually run, at what utilisation and what effective rate, and use it to render each customer's own bill back to them.
**Tags:** #k-means-clustering #dimensionality-reduction #gradient-boosting #descriptive-statistics #hypothesis-testing #confidence-intervals #compliance #revenue-impact
**Contested on:** Every serious competitor that gets here is fighting to tell a customer what a workload of this shape should cost and what comparable organisations actually pay — and whoever does that holds the only asset in this category a competitor cannot obtain from the same billing export.

## The Problem
A customer asks whether their effective rate is good. The vendor can see the effective rates of eleven hundred other organisations and answers that it depends. A customer asks whether their observability spend as a share of infrastructure is reasonable. The vendor holds that ratio for every customer they serve and cannot say. A customer asks what a workload of this shape ought to cost. The vendor has thousands of comparable workloads with their configurations, utilisations and costs. Every one of these questions is answerable from the corpus the vendor has already ingested, and none is answered, which is why the customer treats the product as a reporting tool and compares it on price.

## Why Nobody Has Built This
Cross-customer analysis of billing data is sensitive and nobody has done the work to define a form of it that customers would accept — so the topic is avoided rather than designed, exactly as it is in every other corpus opportunity in this vault. There is also a specific commercial hesitation here: publishing effective-rate benchmarks strains the vendors' relationships with the hyperscalers, whose discount structures the benchmark would expose. And building it requires workload normalisation across organisations, which is genuine data work with no immediate demonstrable output.

## What to Build
The corpus as a product, governed properly. Normalise workloads into comparable shapes — a web tier of this size, a database of this class, a data pipeline of this throughput — using configuration and utilisation rather than customer-specific identifiers, which is the enabling work and is what turns thousands of bills into a dataset. Benchmark the questions customers actually ask: effective rate against comparable organisations, commitment coverage, utilisation by instance family, spend composition by category, and cost per unit of workload. Report each as a distribution with the customer's position marked, rather than as a single figure, since the useful statement is where they sit rather than whether they are above or below an average. Attach an explanation to an unfavourable position — this workload family runs at half the utilisation typical for its shape — which is what makes a benchmark actionable rather than merely uncomfortable. Build the governance in from the start: aggregate only, minimum cohort sizes, structural and rate data rather than anything identifying, customer opt-in with reciprocity, and a public statement of exactly what is analysed. And publish the general findings, because in a category this converged, being the vendor that can say what things should cost is a position no competitor can reach by connecting to the same billing export.

## Target Customer
The cost management vendors themselves, primarily; and cloud economics and procurement functions, who would buy the answer directly.

## Impact If Built
The corpus is the only asset in this category that a competitor cannot obtain from the same source, and every participant leaves it idle. Workload normalisation is the enabling work, and reporting positions within a distribution with an explanation attached is what makes the output actionable.
