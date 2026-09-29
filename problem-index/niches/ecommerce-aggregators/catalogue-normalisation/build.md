# Forty Vocabularies for One Portfolio

**Niche:** [[niches/ecommerce-aggregators/catalogue-normalisation/profile|Catalogue Normalisation]]
**Industry:** [[industries/ecommerce-aggregators|Ecommerce Aggregators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Consolidated purchasing is the aggregator model's headline synergy, and it requires knowing that two acquired brands' products are similar enough to buy together — which nobody can determine across forty inconsistent catalogues.
**Tags:** #large-language-models #k-nearest-neighbors #word-embeddings #data-integration #evaluation-metrics #automation #graph-theory #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to describe forty acquired brands' products in one vocabulary — and whoever does that unlocks the synergy, because every portfolio-level decision requires comparability the catalogues do not have.

## The Problem
A sourcing manager wants to know how many products across the portfolio are injection-moulded plastic items under two hundred grams with a printed finish, because that is a consolidation opportunity worth pursuing. The answer is in eleven hundred product records that describe material as plastic, ABS, polymer or nothing, give weight in grams, ounces or not at all, and mention the finish in a free-text description or in a supplier email from four years ago. The question is unanswerable without a person reading every record, which nobody has time for, so the consolidation happens only where somebody happened to notice.

## Why Nobody Has Built This
Normalisation is invisible infrastructure that nobody champions, and the synergy it enables was assumed to follow automatically from ownership. The work looked manual and enormous before extraction from unstructured text became cheap. Each brand's catalogue was inherited as-is during a fast integration. And the absence has no symptom other than synergies that do not materialise, which are attributed to execution.

## What to Build
Extract the portfolio into one schema. Define a common product schema covering the attributes that matter for sourcing, inventory and category decisions — material, process, dimensions, weight, finish, certification, packaging, volume — which is a modest design exercise and is the precondition for everything downstream. Extract those attributes automatically from listing text, images, supplier documents and correspondence, which is now straightforward and is what made this tractable where it previously was not. Reconcile identifiers across brands, since the same component or the same product under different brand names is a consolidation opportunity that is currently invisible. Attach confidence and provenance to every attribute, so a sourcing decision knows whether a value came from a specification or from an inference. Run it over new acquisitions as part of integration, so the portfolio stays comparable as it grows. Produce a portfolio product report — what the portfolio actually contains, by attribute — which most operators cannot produce today and which is useful immediately for category exposure and risk as well as for sourcing. Make it queryable by the sourcing team directly, since the value is in asking questions nobody thought to ask in advance. And feed it into the consolidation analysis, inventory pooling and category concentration work, since one normalisation serves all three.

## Target Customer
Sourcing and category teams, aggregator operating leadership, and the operators who claimed a synergy that requires this to exist.

## Impact If Built
Every portfolio-level question requires a comparability the catalogues do not have, and the synergy that justified the acquisitions depends on it. Automatic extraction made this tractable recently, and one normalisation serves sourcing, inventory pooling and category exposure at once.
