# Specialty Crop Pest & Disease Identification from Field Photos

**Niche:** [[niches/crop-farming/specialty-crop-growers/profile|Specialty Crop Growers]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Plant disease identification apps (Plantix, PlantNet) provide general identification for common diseases, but specialty crop growers need identification specific to their crop and region — distinguishing between 15-20 diseases and 10-15 pests on a single crop (e.g., apple) with specific treatment recommendations per pest/disease/growth-stage combination.
**Tags:** #cnns #multiclass-classification #tacit-knowledge-ml #quick-win

## The Problem
A specialty crop scout or grower photographs a symptomatic leaf, fruit, or branch in the field and needs to know: what is it (specific pathogen or pest), how severe is it (threshold requiring treatment or below economic threshold), and what to do about it (specific product, rate, timing, and re-entry interval). Generic plant ID apps provide genus-level identification ("fungal disease") but not the species-level diagnosis ("this is fire blight, not bacterial canker") that determines the treatment response. An experienced crop scout identifies 30+ pest/disease complexes by visual cues — lesion shape, color, location on the plant, growth stage, weather history — but experienced scouts are scarce and expensive ($40-60/hour).

## What Already Exists
Plantix (PEAT GmbH) and PlantNet provide AI-powered plant disease identification from smartphone photos. These apps cover broad crop ranges with limited depth per crop. University extension services publish diagnostic guides with photos. Neither provides the depth of identification (species-level on a single crop) or the treatment recommendation specificity that a commercial grower needs.

## The Customization Gap
The system must provide crop-specific, region-specific identification: for Washington State apple growers, it must distinguish fire blight from Erwinia amylovora versus bacterial canker, apple scab from Venturia inaequalis versus sooty blotch, and codling moth damage versus Oriental fruit moth. Each identification must include: severity assessment (is this beyond the economic threshold for treatment?), treatment recommendation per growth stage (what products are effective, what is the pre-harvest interval?), and resistance management guidance (rotate chemical classes to prevent resistance development). This depth of crop-specific knowledge does not exist in generic plant ID apps.

## Target Customer
Specialty crop growers and crop scouts managing 50+ acres of a single crop. Approximately 20,000-30,000 US specialty crop operations.

## Impact If Solved
Scout productivity doubles — the scout uses the app to confirm identification rather than bringing samples to the university extension lab (3-5 day turnaround). Misidentification-driven incorrect treatments decrease by 50-70%. Beginning scouts reach effective diagnostic performance in 1-2 seasons instead of 5-10 years.
