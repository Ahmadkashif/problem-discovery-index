# Custom Studies Are Delivered and Then Lost

**Niche:** [[niches/auto-dealers-independent/registration-market-intelligence/profile|Vehicle Registration & Market Intelligence Data]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** The consulting side answers the same segment question for six manufacturers over four years, each time from the raw registration feed, and cannot retrieve a single one of the previous answers.
**Tags:** #word-embeddings #bert #transformers #k-means-clustering #dimensionality-reduction #descriptive-statistics #evaluation-metrics #tacit-knowledge-ml #data-integration #workflow-orchestration

## The Problem
Alongside syndicated products, these firms run substantial custom research: a manufacturer wants loyalty analysis for a segment in specific markets, a lender wants collateral concentration by configuration, a supplier wants vehicle-in-operation projections for a component. Analysts build each from the underlying data, making dozens of definitional choices along the way — how the segment is bounded, which body styles are in, how fleet registrations are treated, which geography definition applies. The deliverable ships as a deck and is archived by client. The definitions are not archived at all. So the next study on the same segment re-derives them, differently, and two clients competing in one market receive segment totals that do not reconcile. The firm cannot explain the discrepancy because neither derivation was written down.

## Why It's Still Broken
Custom work is organized around the engagement and ends when it ships. Nobody owns cross-study consistency, and the archive exists for contractual rather than analytical reasons. The analysis lives in notebooks and query files where the reasoning is embedded in code, so even locating a prior study does not recover the choices it made. And because each client sees only their own work, inconsistency across the book stays invisible until two clients compare figures — rare enough that it has never forced the fix, and damaging enough when it happens that it should have.

## What a Fix Looks Like
A study record capturing analytical substance rather than the output artifact: segment and geography definitions, the data vintage used, inclusion and exclusion rules with stated reasons, derived measures, and headline findings — recorded as structured fields during the work rather than as documentation afterward. Indexed by subject rather than by client, so an analyst starting an engagement sees every prior study touching the same segment with the definitions each used. A consistency layer compares definitional choices across studies on overlapping subjects and flags divergence, distinguishing a deliberate client-specific cut, which is fine and should be recorded as such, from an accidental inconsistency, which is not. Common definitions promote into a shared library so the house position on a contested boundary is executable rather than a matter of who did the work.

## Who Feels the Pain
Analysts rebuilding derivations that exist; the research director accountable for consistency across a book of work with no instrument to check it; account teams exposed when clients compare numbers; and the firm's credibility, which rests entirely on figures being reproducible.

## Impact If Fixed
Turns years of delivered custom work into a compounding asset — marginal study cost falls in well-covered segments while quality rises, because the analyst starts from accumulated definitional decisions instead of reinventing them. Consistency becomes assertable rather than hoped for. And the record of what clients have asked about over time is itself an early signal of where the industry's attention is moving, which the firm currently throws away every time a study ships.
