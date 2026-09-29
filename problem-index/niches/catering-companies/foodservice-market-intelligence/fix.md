# Custom Studies Leave No Trace in the Firm

**Niche:** [[niches/catering-companies/foodservice-market-intelligence/profile|Foodservice Market Intelligence Firms]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Fix (Pain Point)
**One-liner:** The firm has answered the same category question for nine manufacturers over four years and cannot retrieve one of those answers, so the tenth analyst starts from the raw menu database like the first one did.
**Tags:** #word-embeddings #bert #transformers #k-means-clustering #dimensionality-reduction #descriptive-statistics #evaluation-metrics #tacit-knowledge-ml #data-integration #workflow-orchestration

## The Problem
Custom studies are a large share of revenue and leave nothing behind. An analyst defines the category boundary, decides how to treat borderline preparations, picks the operator segments and geographies, builds the cuts, sanity-checks against known benchmarks, and ships a deck. Every one of those definitional choices is consequential and none is recorded outside the notebook that produced it. The next study on the same category re-derives them differently, so two clients competing in one category receive totals that do not reconcile, and the firm cannot explain the gap because neither derivation was written down. The accumulated analytical judgment of the custom practice — which is the firm's most valuable asset after the database itself — is functionally write-only.

## Why It's Still Broken
Delivery is organized around the engagement and ends when the deck ships. The archive exists for contractual reasons, indexed by client and date, which is precisely the wrong index for the question an analyst actually has. The analysis lives as code and spreadsheet formulas, so even finding a prior study does not recover its reasoning. And because each client sees only their own work, cross-book inconsistency stays invisible until two clients compare figures — rare enough never to have forced a fix, damaging enough when it happens to be the thing that should have.

## What a Fix Looks Like
A study record capturing analytical substance rather than the output artifact: category and segment definitions, database vintage, inclusion and exclusion rules with stated reasons, derived measures, and headline findings — recorded as structured fields during the work rather than as documentation afterward. Indexed by subject, so an analyst starting an engagement immediately sees prior coverage of the category and the definitions each study used. A consistency layer compares definitional choices across overlapping studies and flags divergence, distinguishing a deliberate client-specific cut, which should be recorded as such, from an accidental inconsistency, which should be resolved. Definitions that recur promote into a shared library, so the house position on a contested category boundary becomes executable rather than dependent on who was assigned.

## Who Feels the Pain
Analysts rebuilding derivations that exist; the insights director accountable for consistency with no instrument to check it; account teams caught out when clients compare numbers; and the firm's credibility, which rests on figures being reproducible.

## Impact If Fixed
Turns years of custom delivery into a compounding asset — marginal study cost falls in well-covered categories while quality rises, because the analyst starts from accumulated decisions rather than reinventing them. Consistency becomes assertable. And the record of what clients have asked about over time is the earliest available signal of where category interest is moving, which the firm currently discards with every deck it ships.
