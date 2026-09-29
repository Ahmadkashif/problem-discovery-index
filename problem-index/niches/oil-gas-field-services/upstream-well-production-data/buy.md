# Entity Resolution Across Fifty Regulators Who Never Agreed on Anything

**Niche:** [[niches/oil-gas-field-services/upstream-well-production-data/profile|Upstream Well & Production Data Providers]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The product is one national database assembled from state filings that use different identifiers, different units, different reporting periods, and different definitions of a well.
**Tags:** #named-entity-recognition #graph-ml #ocr #data-integration #anomaly-detection

## The Problem
Every state regulates oil and gas separately and has done so for a century. Permits, completions, production, and ownership are filed to different agencies in different formats on different schedules, with different well identifiers, different allocation conventions for commingled production, and different rules about what is confidential and for how long.

The product is a single normalized national view. Producing it means resolving wells across filings, tracking operator name changes and corporate transactions, allocating production reported at lease level down to wells, reconciling units, and backfilling records released years after the fact when a confidentiality period ends.

That reconciliation is the company. It is also mostly hand-tuned rules and analyst intervention accumulated over decades.

## What Already Exists
Entity resolution and master data management platforms are mature. Document extraction handles scanned filings competently. Data pipeline and quality tooling is commodity.

## The Customization Gap
Generic resolution assumes records describing a stable entity. Here the entity is redefined by every jurisdiction it touches.

**A "well" is not one thing.** Wellbores, completions, laterals, and producing entities are different objects, and states report at different levels — so a national well count depends on definitional choices, and production must be allocated across them under rules that vary by state and by operator practice.

**Operator identity is a moving corporate graph.** Companies merge, rename, and transfer assets constantly, and a production history is only continuous if the operator chain resolves. That is entity resolution over a corporate network with legal events attached, and it determines whether a decade of history belongs to one curve or three.

**Retroactive and confidential data.** Records arrive late, are amended, and are released when confidentiality lapses — so the database must be temporally versioned, and any analysis has to know what was knowable when. Almost no generic pipeline treats as-of reconstruction as a first-class requirement.

**Extraction from scanned filings.** Completion reports, well logs, and older records are documents, and the completion detail that drives every forecast is often only in them.

**Anomaly detection against the state's own behaviour.** A state changing its reporting format or backfilling a period looks like a production event. Distinguishing a data artefact from a real change requires monitoring each source's behaviour, not the aggregate series.

## Target Customer
Chief Data Officer or VP of Data Engineering at an upstream data provider, where reconciliation quality is the product and reconciliation labour is the cost.

## Impact If Solved
Every number the industry plans against descends from this reconciliation, and errors in it propagate silently into type curves, reserve estimates, and acquisition prices. Making the resolution model-driven and temporally reconstructable improves the base data and — through as-of reconstruction — makes any backtest of a forecast honest rather than contaminated by hindsight.
