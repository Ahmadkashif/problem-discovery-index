# Every Custom Study Is Rebuilt From the Raw Feed

**Niche:** [[niches/acupuncture-practices/natural-products-market-data/profile|Natural Products Channel Data Vendors]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Fix (Pain Point)
**One-liner:** The vendor has answered the same category question for eleven different clients over three years and cannot retrieve any of those answers, so the twelfth analyst starts at the raw panel like the first one did.
**Tags:** #word-embeddings #bert #transformers #k-means-clustering #dimensionality-reduction #descriptive-statistics #evaluation-metrics #tacit-knowledge-ml #data-integration #workflow-orchestration

## The Problem
Delivered studies leave the building as decks and spreadsheets and are archived by client and date. That is the only index. An analyst starting work on a botanical category has no practical way to find out that the firm has covered it eleven times before, or which definitional choices those studies made — whether a given product form was counted in the category, how a private label line was treated, which projection vintage was used. So each study re-derives the definitions, and the re-derivations do not agree. Two clients competing in the same category receive category totals that differ, and the vendor cannot explain why because neither derivation was recorded. The accumulated analytical work of the firm, which is its most valuable asset after the panel itself, is functionally write-only.

## Why It's Still Broken
Custom study delivery is organized around the engagement, and the engagement ends when the deck ships. Nothing in the process has an interest in the study's afterlife: the analyst is on to the next one, the archive is a compliance artifact, and there is no role that owns cross-study consistency. The technical position makes it worse — the analysis exists as a notebook or a spreadsheet formula, so even when someone finds a prior study, the reasoning is embedded in code and cell references rather than stated anywhere retrievable. And because clients see only their own studies, inconsistency across the book is invisible until two of them compare notes, which happens rarely enough to never force a fix.

## What a Fix Looks Like
A study record that captures the analytical substance rather than the output artifact: the category and attribute definitions used, the panel vintage and projection method, the inclusion and exclusion decisions with their stated reasons, the derived measures, and the headline findings — recorded as structured fields as the work is done, not as documentation afterward. Made searchable by subject rather than by client, so an analyst opening a new engagement immediately sees prior coverage of the same category with the definitions each one used. A consistency layer then compares definitional choices across studies touching the same categories and flags divergence, which turns an invisible liability into a managed one. Where a divergence was deliberate — the client asked for a non-standard cut — the record says so, which is the difference between an inconsistency and a documented choice.

## Who Feels the Pain
Analysts rebuilding derivations that already exist; the insights director accountable for methodological consistency across a book of work with no instrument to check it; account teams caught out when two clients compare category totals; and the vendor's credibility, which rests entirely on numbers being reproducible.

## Impact If Fixed
Turns three years of delivered studies into a reusable asset, which compounds — the marginal cost of a study in a well-covered category falls sharply while the analytical quality rises, because the analyst starts from the firm's accumulated definitional decisions rather than reinventing them. Cross-client consistency becomes something the vendor can assert and demonstrate rather than hope for. And the record of what clients have asked about, over time, is itself a commercial signal the vendor currently discards: it is the earliest available indicator of where category interest is moving.
