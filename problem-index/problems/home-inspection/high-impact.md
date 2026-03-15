# Defect Detection and Severity Classification from Inspection Photos

**Industry:** [[home-inspection|Home Inspection]]
**Type:** High Impact
**One-liner:** Experienced home inspectors who identify defects across 12+ home systems by reading subtle visual evidence — hairline cracks in foundation walls, double-tapped breakers in panels, improper flashing patterns on roofs — get that multi-system visual expertise augmented by a computer vision model that flags potential defects in their inspection photos, reducing the miss rate for non-obvious defects.
**Tags:** #cnn #object-detection #multiclass-classification #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem

A home inspection covers 12-15 building systems — structure, roofing, exterior, electrical, plumbing, HVAC, insulation, windows, doors, and more — in 2.5-4 hours. An experienced inspector has internalized hundreds of defect patterns across all these systems through years of inspections. A newer inspector has more gaps in their visual library — systems they've inspected less frequently (older knob-and-wire electrical, slate roofing, steam heat systems) present defects they haven't developed recognition for.

The miss-rate problem has direct business consequences: a significant defect missed during inspection and discovered by the buyer after closing leads to E&O claims. Even experienced inspectors miss defects — not from lack of care but from the cognitive load of inspecting 15 systems in rapid succession. The photographic record of the inspection captures what the camera saw; the question is whether the inspector consciously registered all the evidence in the photo.

## Why It's High Impact

A computer vision model that reviews inspection photos for known defect patterns would provide a "second pass" review that catches defects the inspector photographed but didn't register — reducing the E&O miss rate that is the primary liability and business risk for home inspectors.

The business model opportunity is significant: offering "AI-reviewed" inspections as a premium service tier justifies higher pricing ($50-$100 premium) while reducing liability. For a firm doing 400 inspections per year, an AI-reviewed tier at a $75 premium with 50% adoption adds $15,000 in annual revenue while reducing E&O exposure.

## What a Solution Looks Like

Integration with Spectora or similar report writing software: after the inspector adds photos to each report section, the model reviews each photo for defect indicators in the relevant system. Flagged observations are presented to the inspector: "Possible double-tap at breaker 14 — review the electrical panel photo." The inspector confirms or dismisses each flag, adds to the report if confirmed. The model doesn't write the report — it reviews the photographic evidence for the inspector's consideration.

**Defect categories with strong vision signal:**
- Electrical: double-tapped breakers, wire gauge mismatch, missing knockouts, scorching/burning evidence, AFCI/GFCI installation
- Roofing: shingle condition (granule loss, curling, cracking), flashing sealing, ridge cap integrity, penetration sealing
- Structural: foundation crack type and pattern (horizontal, stair-step, vertical, offset), wall bow, beam/post condition
- Plumbing: active leak evidence (staining, efflorescence, mineral deposit), improper CPVC/PEX connections, missing pipe support
- Exterior: paint failure, wood rot, caulk failure at penetrations, grading issues (soil contact with siding)

## Implementation Path

Spectora has the photo library from thousands of inspectors. A data partnership with Spectora provides access to photos with inspector-written defect descriptions in the corresponding report section — the report narrative is the natural language supervision signal for training. Fine-tuning a detection model (YOLOv8 or DETR) on labeled inspection photos: 12-18 months end-to-end with dataset assembly across multiple defect categories and building systems. Starting with 3-4 high-volume, well-understood defect categories (electrical panel, roofing, foundation cracks) as an initial product scope.
