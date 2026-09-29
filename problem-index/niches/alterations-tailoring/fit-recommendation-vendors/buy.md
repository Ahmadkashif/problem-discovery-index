# Entity Resolution Adapted to Garment Specification Drift

**Niche:** [[niches/alterations-tailoring/fit-recommendation-vendors/profile|Apparel Fit & Returns Analytics Vendors]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Master data management products match records that refer to the same thing; the hard problem here is deciding whether two garments with the same style number and different factories are the same thing at all.
**Tags:** #contrastive-learning #bert #transformers #word-embeddings #k-means-clustering #random-forests #evaluation-metrics #data-integration #automation #workflow-orchestration

## The Problem
A fit model is only as good as its belief about what a given garment physically is, and that belief is built from specification data arriving from hundreds of brands in hundreds of formats. The same style is carried by multiple retailers under different SKUs, gets re-cut mid-season when production moves factories, appears with measurements in inches at one source and centimetres at another, and is described by a colourway name that changes by market. Analysts spend a large share of their time deciding whether two records describe one garment, two garments, or one garment in two states — and getting it wrong pollutes the model in the way hardest to detect, because a merged pair of genuinely different cuts produces a fit signal that is confidently wrong rather than obviously missing.

## What Already Exists
Entity resolution is a mature, well-served category. Informatica and Reltio provide enterprise master data management with survivorship rules and stewardship workflow; Senzing and Zingg offer machine-learning matching that handles noisy identifiers well; Snowflake and Databricks both ship reasonable native matching. All of them handle fuzzy names, transliteration, missing fields, and human review queues competently.

## The Customization Gap
Every one of these assumes the entity is stable and the records are noisy observations of it. Garment identity is the opposite: the record can be perfectly clean and the underlying object genuinely changed, because a factory move or a mid-season cost engineering pass alters the physical garment while the style number stays fixed. No general-purpose tool has a concept of an entity that legitimately drifts, so it either merges across a real change or splits on a naming variation, and there is no correct configuration. The adaptation needed is a garment identity model with a temporal dimension — a style is a sequence of physical states, each with its own measurement set and production window, and matching decides both which style a record belongs to and which state. Measurement comparison has to be geometry-aware rather than string-aware, so that a difference of a quarter inch at the chest is treated differently from the same difference at the neck, and unit and point-of-measure conventions are normalized before comparison rather than after. Detected drift then becomes an output in its own right: a brand that silently re-cut a style mid-season is information the brand itself frequently does not have.

## Target Customer
Heads of data engineering and fit ontology leads at fit intelligence vendors, and the analysts who currently arbitrate merge decisions by hand under volume pressure.

## Impact If Solved
Removes the largest silent error source in the model and the largest manual time sink in the operation at the same time. Treating drift as signal rather than noise also produces a saleable finding the vendor cannot currently offer — mid-season specification change detection, which sits directly on the brand's own quality problem and comes free once identity is modelled temporally.
