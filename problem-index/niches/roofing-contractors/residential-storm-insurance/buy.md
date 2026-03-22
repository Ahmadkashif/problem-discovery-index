# EagleView Damage Classification Layer

**Niche:** [[niches/roofing-contractors/residential-storm-insurance/profile|Residential Storm & Insurance]]
**Industry:** [[industries/roofing-contractors|Roofing Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** EagleView already captures high-resolution aerial imagery and delivers precise roof measurements — but it stops at geometry and never tells you what's wrong with the roof, leaving the highest-value step (damage assessment) entirely to human judgment.
**Tags:** #cnns #semantic-segmentation #transfer-learning #data-integration #automation #revenue-impact

## The Problem
Every insurance-restoration roofing company orders EagleView reports for roof measurements — square footage, pitch, facet layout, ridge/hip/valley lengths. These reports are accurate to within 2% and have eliminated manual measurement as a bottleneck. But the EagleView report tells you the roof is 32 squares with a 6/12 pitch across 8 facets — it does not tell you that facets 2, 3, and 5 have hail damage affecting 60% of the surface area, that the ridge cap on the north-south ridge is cracked, or that the pipe boot on facet 4 has failed. Contractors pay $30-50 per EagleView report for geometry and then send an inspector to the roof for 30-45 minutes to assess condition. The measurement data and the condition data never connect automatically.

## What Already Exists
EagleView provides aerial measurement reports used by 95%+ of insurance-restoration roofers. Their imagery captures roofs at resolutions sufficient for measurement but the analysis pipeline only extracts geometric features. HOVER, another measurement platform, focuses on siding and exterior measurements. Nearmap provides high-frequency aerial imagery but no condition analysis. Several startups (Betterview, Cape Analytics) serve insurance carriers with property condition assessment from aerial imagery, but they serve the carrier side — not the contractor side — and their models are trained to minimize claims, not maximize legitimate damage documentation.

## The Customization Gap
Three layers need to be built on top of EagleView's existing imagery pipeline. First, a condition assessment model that classifies roof surface condition (good/fair/poor/damaged) per facet from the same imagery used for measurement — this requires training on contractor-annotated imagery rather than carrier-annotated imagery, since the two sides have systematically different damage thresholds. Second, a damage-type classifier that distinguishes hail, wind, aging, and mechanical damage from aerial perspective — a harder problem than ground-level classification because the viewing angle is different from how inspectors are trained. Third, a change-detection layer that compares pre-storm and post-storm imagery of the same property (EagleView already has historical imagery) to isolate storm-caused damage from pre-existing conditions, which is the single most contested point in insurance claims.

## Target Customer
Insurance-restoration roofing companies already purchasing EagleView reports at $30-50 per property, spending $15K-75K annually on aerial measurement. These companies would pay an additional $20-40 per report for condition assessment that reduces the need for physical roof inspections on 60-70% of properties — the ones where aerial imagery can definitively identify or rule out storm damage.

## Impact If Solved
Eliminates physical roof inspections on 60-70% of initial assessments, saving 30-45 minutes per property and enabling inspectors to pre-qualify leads before committing to a site visit. For a company inspecting 500 roofs per storm season, this recovers 250-350 inspection hours and eliminates wasted trips to undamaged properties that currently consume 30-40% of inspector time.
