# The Skills Ontology as a Measured Model, Not a Maintained List

**Niche:** [[niches/corporate-training/labor-market-skills-data/profile|Labour Market & Skills Taxonomy Data Providers]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every analytic the firm sells rests on a skills ontology maintained by hand against a language that changes faster than the taxonomy does, and nobody measures whether it still describes the labour market.
**Tags:** #bert #transformers #word-embeddings #contrastive-learning #dimensionality-reduction #k-means-clustering #evaluation-metrics #cross-validation #tacit-knowledge-ml #data-integration #revenue-impact

## The Problem
The ontology is the product. Every demand estimate, gap analysis, and talent flow study depends on resolving free text — a posting, a profile, a résumé — into skills and occupations. That resolution is governed by a taxonomy of tens of thousands of nodes with synonyms, hierarchies, and relationships, maintained by a team reading what employers write and deciding what is a new skill, what is a rebranding of an old one, and where an emerging capability belongs. The labour market's vocabulary moves constantly and asymmetrically: new tools acquire names before they acquire categories, and employers use terms inconsistently for years before convention settles. The taxonomy team is always behind, always working from judgment, and there is no measurement of how well the ontology currently covers what employers actually say.

## Why Nobody Has Built This
The taxonomy is the moat, which makes it the last thing anyone hands to an automated process, and its maintenance has always been treated as expert editorial work. As in every classification operation this sweep has examined, the decisions were recorded as outcomes rather than as labelled examples — the database says this phrase maps to that skill, not what the taxonomist was looking at or why they hesitated. And there is no natural ground truth for whether a skills taxonomy is correct, which has been taken to mean it cannot be evaluated at all rather than that evaluation needs designing.

## What to Build
Ontology maintenance as a measured, learning system. Unresolved and low-confidence text is the primary signal: the fraction of posting content that fails to map, clustered semantically, is a direct map of where the taxonomy is behind, and it is computable today from data already held. New term candidates surface from those clusters with evidence — how many employers, in which industries, over what period — so taxonomists work a ranked queue rather than reading. Every taxonomist decision is captured with its full context, building the labelled corpus that has been discarded until now. Coverage becomes a reported metric by occupation family and industry, which is the evaluation that supposedly could not exist: not whether the taxonomy is right in the abstract, but what share of real employer language it currently resolves. And retrospective checking surfaces where historical mappings disagree with current convention, which is how years of accumulated drift become visible.

## Target Customer
Chief economists and heads of taxonomy at labour market data providers running 200-800 staff, and the workforce planning leaders at employers and institutions who build capability strategies on skill definitions they cannot inspect.

## Impact If Built
Removes the constraint on how fast the taxonomy can track a market that reinvents its vocabulary continuously, which is the product's only real quality dimension. Measured coverage is also a claim no competitor makes, and it is exactly what a sophisticated buyer asks when comparing two skills datasets that both assert comprehensiveness.
