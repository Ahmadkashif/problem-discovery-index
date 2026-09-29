# Pattern Mining Over Schemas and Workloads

**Niche:** [[niches/database-platform-vendors/fleet-corpus-anti-patterns/profile|Fleet Corpus & Anti-Patterns]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Frequent pattern mining, graph matching and failure prediction from structural features are all mature, and the largest corpus of production database structures in existence has none of them applied to it.
**Tags:** #k-means-clustering #graph-theory #gradient-boosting #survival-analysis #dimensionality-reduction #evaluation-metrics #confidence-intervals #hypothesis-testing
**Contested on:** Every serious competitor that gets here is fighting to warn a customer about a failure thousands of other customers have already had — and whoever does that holds a corpus of how databases actually fail that no single organisation can assemble.

## The Problem
Finding recurring substructures in a population of graphs, clustering them, and relating their presence to subsequent outcomes is standard data mining with mature algorithms. A schema is a graph, a query is a graph, and a workload is a distribution over them. The fleet of a large managed vendor is the best corpus of these objects that exists, and the analysis applied to it is aggregation for capacity planning.

## What Already Exists
Frequent subgraph mining algorithms; graph matching and similarity measures; clustering and dimensionality reduction; survival analysis for time-to-failure; supervised failure prediction from structural features; and the software engineering research tradition of mining repositories for defect-predictive patterns, which is the closest methodological analogue.

## The Customization Gap
The adaptation is to schemas and workloads with an outcome to predict. It requires: (1) a structural representation robust to naming, since every customer names things differently and a representation sensitive to identifiers will find no patterns at all — this is the foundational modelling decision; (2) growth and scale as first-class features, because the same structure is benign at one size and pathological at another, and a pattern without a scale condition is not actionable; (3) outcome linkage, joining structure to subsequent incidents, support tickets and performance degradation, which is the labelling constraint and requires the incident record to be structured — the same binding constraint the observability category has; (4) confounding awareness, since customers with certain patterns differ systematically in other ways and a naive association will identify the customer segment rather than the pattern; and (5) content-free operation throughout, using structure and statistics only, which is both sufficient for the analysis and the condition of it being permitted.

## Target Customer
Managed database vendors, database engine vendors with telemetry programmes, and the academic groups who would collaborate given access to a corpus of this kind.

## Impact If Solved
The mining techniques are mature and the corpus is the best of its kind, and the analysis has not been attempted. Scale-conditioned patterns and structured outcome linkage are the two adaptations, and content-free operation is what makes the whole thing defensible.
