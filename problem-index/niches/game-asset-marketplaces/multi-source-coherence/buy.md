# Data Normalisation From Integration Platforms

**Niche:** [[niches/game-asset-marketplaces/multi-source-coherence/profile|Multi-Source Asset Coherence]]
**Industry:** [[industries/game-asset-marketplaces|Game Asset Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data integration platforms solved reconciling many sources into one schema, and asset pipelines do it by hand per file.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #feature-engineering #compliance #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to make assets from fifteen creators with fifteen conventions look like one game, and whoever automates that work takes the account.

## The Problem
Reconciling many sources with different conventions into one consistent internal representation is exactly what data integration platforms do. Schema mapping, unit and format normalisation, validation rules, transformation pipelines and quality reporting are all mature, commoditised capabilities. Every business with more than a few data sources uses them. Asset pipelines have the same structure — many sources, incompatible conventions, one target — and reconcile by hand.

## What Already Exists
Source-to-target schema mapping; unit and format normalisation; declarative transformation pipelines; validation and quality rules; and source quality reporting.

## The Customization Gap
The adaptation is to artefacts whose correctness is partly aesthetic. It requires: (1) a target convention that includes visual and stylistic consistency, which no validation rule can express and which is the substantive difference — the mechanical half normalises like data and the aesthetic half does not; (2) transformations over geometry, materials and textures rather than over records; (3) correctness judged by how it looks in a scene rather than by a schema check; (4) an artist rather than a data engineer as the operator, requiring a visual interface; and (5) a target that evolves as the game's art direction develops, so the normalisation must be re-runnable.

## Target Customer
Game studios, technical artists, asset marketplaces, and pipeline and integration tooling vendors.

## Impact If Solved
Data integration commoditised reconciling many sources into one schema. A target convention that includes visual consistency is the half no validation rule expresses, which is where the artist stays in the loop.
