# Field Pest Identification & Threshold Decision Engine

**Niche:** [[niches/pest-control/agricultural-pest/profile|Agricultural Pest Management]]
**Industry:** [[industries/pest-control|Pest Control]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool lets a crop scout photograph an insect or plant damage, identify the pest species, and calculate whether the infestation exceeds economic treatment thresholds for that crop.
**Tags:** #cnn #multiclass-classification #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
Experienced crop pest consultants identify hundreds of insect species by sight — distinguishing beneficial insects (ladybugs, lacewings) from pests (aphids, armyworms), and identifying species-specific damage patterns on leaves, stems, and fruit. They make threshold-based treatment decisions: "this field has 4 corn earworm moths per trap per night — the economic threshold is 5, so hold off on spraying." Junior scouts lack this species identification skill and threshold knowledge, leading to either unnecessary treatments (costly and environmentally harmful) or missed infestations (crop loss).

## Why Nobody Has Built This
Agricultural pest identification is genuinely hard: insects are small, camera angles vary, field conditions (dirt, wind, sunlight) affect image quality, and distinguishing similar species (e.g., fall armyworm vs. true armyworm) requires examining specific anatomical features. Economic thresholds vary by crop, growth stage, pest species, and even market prices (threshold changes when corn is $7/bushel vs. $4/bushel). No single labeled dataset covers the thousands of crop-pest-threshold combinations.

## What to Build
A mobile field scouting app where the scout photographs insects, plant damage, or trap catches. Computer vision identifies pest species with confidence scores. The system pulls the economic threshold for that pest on that crop at the current growth stage, compares observed pest density to the threshold, and recommends treat/hold/monitor. Each identified specimen and treatment outcome feeds back to improve the model.

## Target Customer
Crop pest consultants scouting 5,000+ acres per season who employ junior scouts with less than 3 years of field identification experience.

## Impact If Built
Reduces unnecessary pesticide applications by 15-25% (saving $8-$20/acre in chemical costs), prevents missed infestations that cause 5-15% yield loss, and enables junior scouts to make threshold-quality decisions within their first season.
