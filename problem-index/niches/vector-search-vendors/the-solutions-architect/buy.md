# Query Explanation From Search and Databases

**Niche:** [[niches/vector-search-vendors/the-solutions-architect/profile|The Solutions Architect]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Relational databases explain query plans and search engines explain relevance scores term by term, and vector search returns a list with no account of itself.
**Tags:** #evaluation-metrics #norms-and-inner-products #data-integration #automation #worker-facing #descriptive-statistics #graph-theory #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make the platform explain why a document was not returned — and whoever does that takes the support load, because that one question is most of the category's solutions engineering.

## The Problem
Every relational database has a command that shows how a query was executed, what it cost and why the planner chose that path — it is the single most-used debugging tool in the field. Full-text search engines go further and decompose a relevance score into its contributing terms and factors, which is how search relevance engineers work. Vector search returns identifiers and distances. Neither the plan nor the scoring is inspectable, and the debugging practice that both traditions built is unavailable.

## What Already Exists
Query plan explanation with cost breakdown and actual-versus-estimated rows; relevance score explanation decomposing a score into its components; search debugging tooling that compares two configurations on the same query; profiling output showing time spent per stage; and index usage and statistics reporting.

## The Customization Gap
The adaptation is to a score that is a distance in a learned space rather than a sum of interpretable term contributions. It requires: (1) explanation at the level the user can act on — chunk, field, and the comparison against exact search — since a distance cannot be decomposed into terms the way a lexical score can, and finding the actionable decomposition is the design problem; (2) traversal explanation for the graph, showing where the search entered, how far it explored and where the target sat relative to that path, which is the direct analogue of a query plan and does not exist anywhere; (3) counterfactual explanation as a first-class query — why was this not returned — which the database tradition does not offer and which is the actual question here; (4) hybrid explanation covering both modes and their fusion, since the score the user sees is a combination and no part of it is currently visible; and (5) configuration comparison on a fixed query set, which is how search relevance work is actually done and has no equivalent in this category.

## Target Customer
Vector search vendors, solutions and support organisations, application teams, and the search relevance engineering community.

## Impact If Solved
Both the database and search traditions built their debugging practice on explanation, and this category ships none. Counterfactual explanation — why was this not returned — is the question that drives the support load and neither tradition offers it directly.
