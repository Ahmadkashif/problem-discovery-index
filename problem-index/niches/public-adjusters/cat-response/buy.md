# Aerial Imagery Damage Assessment Integration

**Niche:** [[niches/public-adjusters/cat-response/profile|Catastrophe (CAT) Response]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Satellite and drone aerial imagery platforms exist for roof assessment, but none integrate with PA workflows to prioritize inspections, pre-scope damage, and generate preliminary Xactimate estimates before the adjuster arrives on-site.
**Tags:** #cnn #semantic-segmentation #computer-vision #quick-win

## The Problem
After a CAT event, PAs must inspect hundreds of properties but can only physically visit 5-8 per day per adjuster. Without triage, adjusters waste time on properties with minimal damage while severely damaged properties wait weeks for inspection. Aerial imagery (satellite, drone, fixed-wing) can reveal roof damage, missing shingles, tarp coverage, and structural collapse — but PAs don't have tools to use this imagery systematically for triage and pre-scoping.

## What Already Exists
Aerial imagery providers (EagleView, Nearmap, Cape Analytics) capture post-storm imagery and offer damage detection algorithms used by insurance carriers. Drone survey platforms (DroneDeploy, Skydio) enable on-site aerial capture. These tools are designed for carriers conducting their own inspections — not for PAs who need to triage their client pipeline, identify high-value claims, and pre-scope damage before visiting.

## The Customization Gap
PAs need a triage layer on top of aerial imagery: given a list of client addresses, rank them by estimated damage severity, overlay the damage detection on the property map, generate a preliminary scope (estimated number of roof squares affected, presence of structural damage, evidence of interior water intrusion from missing roofing), and route the highest-severity properties to the most experienced adjusters. The output must feed into the PA's claim management workflow, not exist as a separate map tool.

## Target Customer
PA firms deploying CAT teams that need to triage 200-500 signed clients into inspection priority order within the first week of deployment.

## Impact If Solved
Prioritizes highest-value claims for first inspection, increasing average early settlement value by 20-30%. Reduces unnecessary site visits for low-damage properties by 25%. Enables one adjuster to effectively triage 50 properties per day (aerially) versus 6-8 per day (physically).
