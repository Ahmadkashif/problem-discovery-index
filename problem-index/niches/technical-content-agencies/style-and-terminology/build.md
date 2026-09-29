# One Term, One Meaning

**Niche:** [[niches/technical-content-agencies/style-and-terminology/profile|Style & Terminology Consistency]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same concept has three names across the corpus and the reader is expected to know they are the same.
**Tags:** #word-embeddings #automation #evaluation-metrics #data-integration #compliance #large-language-models #descriptive-statistics #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to keep one term meaning one thing across a corpus written by many people over many years, and whoever enforces that mechanically takes the account.

## The Problem
Terminology drifts because writers change, products are renamed, and nobody enforces the vocabulary. The same concept appears as three terms in different sections. One word is used for two different things. A feature renamed two years ago still appears under its old name in half the corpus. Readers searching for one term miss content using another, and a machine synthesising from the corpus produces confident nonsense about the relationship between the three names.

## Why Nobody Has Built This
Style linting handles mechanical rules rather than meaning. Detecting that two terms denote the same concept requires semantic analysis nobody has applied. Terminology changes are announced and not propagated. And the older corpus is exempted from every improvement.

## What to Build
Enforce the vocabulary and detect the drift semantically. Maintain an enforced terminology list with approved terms, deprecated terms and their replacements, which is the core and is what a style guide alone cannot do. Detect the same concept expressed under different names using semantic comparison rather than string matching, since that is the drift a linter cannot see. Detect one term used for two concepts, which is the more damaging direction and is entirely invisible to current tooling. Propagate a terminology change across the whole corpus when a product renames something, rather than fixing new content only. Check the older corpus rather than exempting it, as that is where most of the drift lives. Enforce at authoring in the writer's editor rather than in review. Keep the terminology list synchronised with the product's own naming, which is the source of truth. Handle the legitimate synonyms readers use for search separately from the canonical term, so findability and consistency are both served. Report terminology coverage as a corpus health metric. And make an exception route explicit, since some inconsistencies are deliberate and a rigid rule produces workarounds.

## Target Customer
Documentation teams and technical content agencies, editorial leadership, documentation tooling vendors, and terminology management providers.

## Impact If Built
Three names for one concept breaks search for readers and produces confident nonsense from machines, and no linter can see it. Semantic drift detection with enforced terminology is what a style guide cannot do.
