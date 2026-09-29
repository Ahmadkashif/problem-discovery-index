# Program Analysis Applied to the Query Estate

**Niche:** [[niches/bi-analytics-platforms/metric-definition-drift/profile|Metric Definition Drift]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** SQL parsing, normalisation and equivalence checking are mature compiler-adjacent techniques with excellent open tooling, and the analytics estate is treated as a folder of opaque documents.
**Tags:** #graph-theory #spectral-graph-theory #word-embeddings #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to guarantee that two things called revenue are the same number, and to detect it from the query logic when they are not — and whoever does that takes the account, because the meeting that reconciles instead of deciding is the category's most visible failure.

## The Problem
Determining whether two queries compute the same thing is a program equivalence question, and the database community has been building the tooling for it for decades: parsers, logical plan representations, normalisation rules, containment and equivalence checks. Query optimisers rely on exactly this machinery. The analytics estate — thousands of queries, all stored, all in a handful of dialects — has never had any of it pointed at it.

## What Already Exists
Multi-dialect SQL parsers with good coverage are free and mature. Logical plan representations and normalisation are standard in every query engine. Lineage extraction from SQL is a working commercial and open capability. Column-level lineage tools exist. Embedding models handle the naming side — deciding that "MRR" and "monthly recurring revenue" are the same claim. dbt has made a large share of transformation logic available as version-controlled code, which is the cleanest input this problem has ever had.

## The Customization Gap
The adaptation is from equivalence to explicable difference. It requires: (1) semantic difference rather than a boolean, since knowing two queries are inequivalent is useless and knowing that one excludes test accounts is the whole product, which means diffing normalised plans and rendering the difference in business language; (2) dialect and BI-tool coverage, because the estate spans several warehouses and several tools each generating its own SQL, and partial coverage produces a partial and therefore untrusted report; (3) concept grouping from names and context, which is the soft half of the problem — deciding which queries are claiming to compute the same thing — and is where embeddings do the work that parsing cannot; (4) consequence ranking from usage and audience, since the raw divergence count in any real estate is large enough to be useless without prioritisation; and (5) tolerance for the genuinely legitimate case, because finance revenue and product revenue differing is correct and the product's credibility depends on letting an organisation mark a divergence as intended and never seeing it again.

## Target Customer
BI and semantic layer vendors, data catalogue and observability vendors for whom this is an adjacent capability, and large internal data platform teams.

## Impact If Solved
The parsing and equivalence machinery is decades mature and free, and the analytics estate is the obvious unexploited target for it. Explicable difference and consequence ranking are the two adaptations that turn a technically correct analysis into something a data leader will act on.
