# Change Detection Adapted to Model-Year Procedure Deltas

**Niche:** [[niches/auto-body-shops/estimating-data-providers/profile|Collision Estimating Data Providers]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Diff tools tell you a document changed; the research question is whether a changed bracket on a 2027 quarter panel invalidates a labor time set for the 2026, and no general-purpose tool has any way to answer that.
**Tags:** #bert #transformers #transfer-learning #object-detection #cnns #graph-neural-networks #evaluation-metrics #automation #workflow-orchestration #data-integration

## The Problem
Every model year, hundreds of vehicles arrive with revised construction, and the research organization must decide which of the existing database entries for the prior year still hold. The input is a large volume of manufacturer documentation — service information, parts catalogues, position statements — issued in inconsistent formats with no change log the publisher can rely on. Researchers work through it looking for the changes that matter: a different substrate, a new fastener strategy, a relocated sensor that adds a calibration requirement, a sectioning restriction. The volume forces triage, so coverage is deepest on high-volume vehicles and thinnest on the long tail, and a missed change means a published time that is quietly wrong for an entire model year.

## What Already Exists
Document comparison and change management are mature and inexpensive. Diffing engines handle structured and semi-structured documents well; enterprise content platforms provide versioning, workflow, and audit trails; commercial document intelligence services extract structure from PDFs at scale, including tables and diagrams. Several vendors sell automotive-specific document ingestion. For detecting that something changed, the market is fully served.

## The Customization Gap
Every one of those tools answers a textual question, and the operative question is a physical one. Most textual changes between model years are immaterial — reformatting, renumbering, editorial rewording — while the changes that matter can be a single specification value or an unremarked difference in an exploded diagram. Worse, the important direction of inference runs from the change to the affected database entries, and no general tool knows that a particular fastener specification underpins a particular labor operation. The adaptation needed is a dependency model connecting database entries to the source documentation elements they were derived from, so that a detected change resolves to the specific entries at risk. Change classification then has to be trained on materiality rather than textual distance — using the publisher's own history of which past changes did and did not require a revision, which is the labelled dataset that already exists in its revision records. And diagram comparison has to be geometric rather than pixel-based, since a redrawn illustration of an unchanged part is the single most common false positive.

## Target Customer
Directors of automotive research and content operations at estimating and procedure publishers, and the researchers who currently triage model-year documentation under a fixed release calendar.

## Impact If Solved
Moves the research organization from documentation triage to materiality review, which is the only part requiring their expertise. Coverage of the long tail improves — the specific place where errors currently concentrate and where competitors are equally weak. And because the dependency model records why every entry exists, the database gains a provenance trail it does not have today, which is directly useful the next time a published number is challenged.
