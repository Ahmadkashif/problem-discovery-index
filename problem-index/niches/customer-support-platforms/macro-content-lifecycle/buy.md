# Deduplication and Similarity Tooling Off the Shelf

**Niche:** [[niches/customer-support-platforms/macro-content-lifecycle/profile|Macro & Content Lifecycle]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Detecting near-duplicate text is a solved problem available in every embedding library, and support libraries contain nine variants of the same answer that agents choose between arbitrarily.
**Tags:** #bert #word-embeddings #contrastive-learning #k-means-clustering #evaluation-metrics #confidence-intervals #automation #quick-win
**Contested on:** Every serious competitor in support content is fighting to keep a library alive rather than merely large — and whoever can retire dead content with evidence takes the knowledge function.

## The Problem
Nine macros address password resets. Three are for a product version that no longer exists, two differ only in tone, one includes a step that was removed, one is a shortened version of another, and two are genuinely distinct because they cover different account types. An agent searching sees nine results and picks one, effectively at random. A generative answering layer retrieves from all nine and may synthesise across contradictory versions, which is worse. Detecting that these are variants of one thing is an embedding comparison that takes seconds.

## What Already Exists
Semantic similarity and near-duplicate detection are elementary with any modern embedding model. Clustering, canonical selection and content consolidation tooling exists in content management and in data deduplication generally. Contradiction detection between texts is a developed natural language inference task with usable models. Everything required is free or nearly so.

## The Customization Gap
The adaptation is to a library whose variants are sometimes meaningful. It requires: (1) distinguishing a true duplicate from a legitimate variant, since the account-type distinction in the example above matters and a naive merge would break it — which means clustering must surface the differences rather than only the similarity; (2) contradiction detection within clusters, because two articles that say different things about the same thing is the most dangerous state a library can be in and is currently invisible; (3) usage and outcome data attached to each variant, so consolidation keeps the one that works rather than the one that was written first; (4) version and product scoping, since much apparent duplication is legitimate versioning that was never marked as such and the fix is metadata rather than deletion; and (5) a review flow that presents a cluster with a recommended canonical version and the differences highlighted, since a knowledge manager can adjudicate that in a minute and cannot adjudicate a list of nine documents.

## Target Customer
Support platform vendors, knowledge managers facing libraries they did not create, and the organisations whose generative retrieval is now drawing from all of it.

## Impact If Solved
Duplicate clustering is close to free and typically reduces a library substantially in a single pass, with the outcome data determining which variant survives. Contradiction detection within clusters is the highest-stakes output, because contradictory content is the specific condition that makes a generative answering layer unreliable in ways that are hard to diagnose afterwards.
