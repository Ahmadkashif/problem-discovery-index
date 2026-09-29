# Filtered Search That Falls Off a Cliff

**Niche:** [[niches/vector-search-vendors/dedicated-retrieval-infrastructure/profile|Dedicated Retrieval Infrastructure]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Nearly every production query filters by tenant, date or permission, and approximate indexes handle selective filters badly in ways that are undocumented and discovered in production.
**Tags:** #k-nearest-neighbors #graph-theory #evaluation-metrics #descriptive-statistics #hypothesis-testing #confidence-intervals #quick-win #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to hold a required recall and tail latency at the lowest cost per vector at billion scale — and whoever does that takes the account, because the buyer is running the arithmetic against self-hosting and will act on it.

## The Problem
A multi-tenant application filters every query to one customer's documents. For a large tenant this is fine. For a tenant holding a thousandth of the corpus, the graph traversal spends its whole budget on vectors that are filtered out and returns three results where ten were requested, or falls back to a scan and takes two hundred times longer. Both failure modes appear only for selective filters, which means they appear for small tenants, which means the customers most likely to churn get the worst experience. Nothing in the documentation describes the behaviour and nothing in the metrics distinguishes it.

## Why It's Still Broken
The interaction between filtering and graph-based approximate search is genuinely hard — the index was built over the whole corpus and the filter defines a subgraph that may be poorly connected. Vendors implement one strategy, usually pre-filtering or post-filtering, and its failure regime is a known limitation rather than a documented one. Benchmarks do not include filters. And the symptom is per-tenant, which makes it invisible in aggregate metrics and hard for the affected customer to articulate.

## What a Fix Looks Like
Make the behaviour visible and then choose the strategy per query. Report effective recall under the filter rather than global recall, which is the number that describes what the user experienced and is currently not computed — this alone surfaces a problem most operators do not know they have. Detect the selectivity of each query's filter and choose between pre-filtering, post-filtering with expansion, and an exact scan on the filtered subset, since each is correct in a different regime and picking one globally guarantees a bad regime. Maintain per-partition indexes for high-cardinality filter fields like tenant, which turns the hard case into an easy one and is the standard answer nobody offers by default. Report when a query returned fewer results than requested, because silently returning three of ten is the most damaging behaviour here and the signal already exists. Document the failure regimes explicitly, including the selectivity ranges where each strategy degrades, since a known limitation that is written down is a design constraint and one that is not is a support incident. Include filtered queries in published benchmarks. And alert on per-tenant recall degradation, so the small tenant's bad experience reaches the operator before it reaches a renewal conversation.

## Who Feels the Pain
Small tenants receiving incomplete results from a system reporting excellent recall; operators debugging a latency spike that only occurs for particular filters; and vendors losing accounts to a documented-as-nothing limitation.

## Impact If Fixed
Effective recall under the filter is the number that describes the user's actual experience and nobody computes it. Choosing the filter strategy per query by selectivity is what removes the cliff, and reporting short result sets surfaces the most damaging silent failure.
