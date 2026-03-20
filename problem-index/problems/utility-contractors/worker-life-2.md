# Gas Leak Indicator Pattern Recognition for Field Survey Teams

**Industry:** [[utility-contractors|Utility Contractors]]
**Type:** Worker Life Changing
**One-liner:** Gas distribution survey teams performing leak detection patrols who must identify gas migration indicators from above-grade visual evidence — dead/stressed vegetation patterns, pavement cracking from subsurface gas accumulation, unusual frost patterns — get a photo-assisted field tool that flags potential leak indicators from survey photos for follow-up with combustible gas indicator equipment.
**Tags:** #cnns #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #feature-engineering #tacit-knowledge-ml #worker-facing

## The Problem

Natural gas leak detection patrols on distribution systems use a combination of instruments (combustible gas indicator, flame ionization detector) and visual observation. Experienced gas distribution technicians recognize above-grade visual indicators of subsurface gas migration: dead or dying vegetation in a pattern inconsistent with drought (localized circular die-off over a leak path), unusual surface disturbance, frost melting patterns in winter (methane warms the soil above a leak). These visual indicators guide where to deploy the instrument — narrowing the search from a mile of street to a specific 20-foot zone.

Junior survey technicians who miss these visual indicators rely entirely on instrument scanning, which is slower and less targeted. Missed visual indicators mean walking past a developing leak that could have been caught earlier.

## Why It Matters to the Worker

Gas leak patrol is a safety-critical task where misses have consequences — a gas accumulation under a foundation that wasn't found by patrol can result in an explosion. The visual indicator skill is part of the safety culture around leak detection. Teaching it formally is difficult because the indicators are subtle and context-dependent; senior technicians teach it informally through walkalong training.

## What a Solution Looks Like

A mobile app used during foot patrol: the technician photographs sections of the right-of-way during the patrol. The model flags photos containing potential gas migration visual indicators (dead vegetation patterns, surface anomalies, pavement disturbance patterns). The technician then deploys their combustible gas indicator at the flagged locations. The model doesn't replace instrument testing — it augments the patrol by improving instrument deployment targeting. Training data: photos from gas leak locations with confirmed leaks (positive labels) and patrol photos from clean sections (negative labels), labeled by experienced gas distribution technicians.

## Impact If Solved

Improves gas leak detection rate during distribution patrols. Reduces the miss rate on developing leaks that could reach hazardous accumulation levels. Supports patrol technician training by making the visual pattern criteria explicit and teachable.
