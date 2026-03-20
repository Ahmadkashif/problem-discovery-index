# AI-Assisted Hail and Wind Damage Assessment from Roof Inspection Photos

**Industry:** [[roofing-contractors|Roofing Contractors]]
**Type:** High Impact
**One-liner:** Experienced roofing inspectors who identify storm damage by reading hail impact patterns, granule loss, and wind lift signatures on shingles — pattern recognition built over thousands of roof inspections — get that visual expertise replicated by a computer vision model that classifies damage from photos, enabling junior inspectors to produce adjuster-quality assessments on the first visit.
**Tags:** #cnns #object-detection #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #matrix-algebra #feature-engineering #tacit-knowledge-ml #revenue-impact

## The Problem

Insurance claim eligibility for roof damage is determined by whether the observed damage is storm-caused (covered) versus normal wear (not covered). Experienced roofing estimators read the roof's visual evidence to make this determination: hail impact craters on asphalt shingles have specific size, shape, and granule displacement patterns that vary by hail diameter and angle of impact; wind damage has characteristic tab-lift signatures and tear patterns distinct from thermal cycling failure; functional damage (damage that shortens shingle life) is distinguished from cosmetic damage (dents without granule loss) by visual cues that insurance adjusters are trained to contest.

A junior estimator who cannot read these visual patterns either undersells the damage (leaving money on the table for the contractor and homeowner) or overclaims (creating liability when the adjuster denies line items). The knowledge gap between a 2-year estimator and a 15-year estimator is primarily visual pattern recognition — a tacit skill that is currently transferred only by walking roofs together over years.

## Why It's High Impact

Insurance claim supplementing generates the highest revenue-per-hour activity in residential roofing. The average insurance roofing claim in a hail market is $12,000–$25,000. A contractor who can consistently identify all legitimately claimable damage earns 15–25% more per job than one who misses line items. At 100 insurance jobs per year, this is $150,000–$500,000 in additional annual revenue for a mid-sized firm.

More broadly, accurate damage assessment enables roofing contractors to expand into new service areas after storm events without requiring their senior estimators to personally inspect every roof. Scalability of the inspection function — currently bottlenecked by senior estimator time — determines how many insurance claims a firm can pursue after a major storm.

## What a Solution Looks Like

A mobile inspection app where the estimator photographs each roof plane, ridge, hip, valley, and flashing zone. The computer vision model:
1. Classifies each photo by damage type: hail impact (size estimate: < 1", 1"–1.5", > 1.5"), granule loss (coverage percentage), wind lift/tab damage, mechanical damage, wear/aging (non-claimable)
2. Identifies the density of hail impacts per square (used to establish functional damage threshold)
3. Flags photos as strong claim evidence vs. weak/contestable
4. Generates a structured damage summary report with photo evidence organized by damage type, suitable for Xactimate line-item entry and adjuster presentation

The model output would not replace the estimator's judgment but would organize and validate their observations, catching damage the estimator photographed but didn't consciously register.

## Competitive Landscape

EagleView and Nearmap provide aerial imagery analysis for roof geometry and basic condition scoring. Their models are not trained for insurance damage assessment at the granular level required for claim supplementing — they produce area measurements and general condition flags, not damage classification suitable for adjuster negotiation. The gap between aerial condition scoring and photo-level damage classification for insurance purposes is the market opportunity.

## Implementation Path

Labeled training data is the primary challenge. Insurance-filed roofing claims with photo documentation and adjuster outcomes provide the supervision signal: photos labeled as covered/denied per damage type with claim outcome. A partnership with a large roofing franchise network (GAF Master Elite, CertainTeed SELECT ShingleMaster) with access to claims history across thousands of inspections would provide the dataset and distribution simultaneously. Fine-tuning YOLOv8 or a vision-language model (GPT-4V, Gemini) on labeled inspection photos: 6-12 months end-to-end with dataset assembly.
