# Prescription-to-Application Verification Gap

**Niche:** [[niches/crop-farming/variable-rate-prescription-management/profile|Variable-Rate Prescription Management]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Fix (Pain Point)
**One-liner:** After a variable-rate application is completed, no tool automatically compares what was prescribed (the prescription map) against what was actually applied (the as-applied map from the equipment controller) — meaning over- and under-application zones go undetected, and the agronomist cannot verify that their prescription was executed correctly.
**Tags:** #data-integration #automation #revenue-impact

## The Problem
A variable-rate nitrogen prescription specifies 180 lbs/acre in high-yield zones and 120 lbs/acre in low-yield zones. The applicator runs the prescription, and the equipment controller generates an as-applied map showing what was actually applied in each zone. But the agronomist who created the prescription rarely sees the as-applied data — it sits in the equipment controller or the farmer's farm management platform, not in the agronomist's prescription management tool. Without comparing prescribed versus applied, the agronomist does not know: was the prescription loaded correctly? Were application rates accurate? Did equipment malfunctions cause over- or under-application? When end-of-season yield results are disappointing, was it the prescription or the execution that failed? This feedback loop — prescription → application → verification → improvement — is broken at the verification step.

## Why It's Still Broken
Prescription data and as-applied data are in different platforms (the agronomist generates prescriptions in their precision ag tool; the as-applied data lives in the farmer's equipment platform). The spatial alignment between the two maps requires GIS processing that the agronomist does not typically perform. Even when both datasets are accessible, the comparison must account for equipment-specific application patterns (turn-row overlap, headland application, nozzle spacing) that create systematic differences between prescribed and applied rates. No tool automates this comparison.

## What a Fix Looks Like
An automated prescription verification tool that: (1) ingests the prescription map (from the agronomist's platform) and the as-applied map (from the farmer's equipment platform via API), (2) spatially aligns the two maps and computes zone-by-zone variance (prescribed rate - applied rate), (3) flags zones where variance exceeds a configurable threshold (e.g., >10% over-application or >10% under-application), (4) attributes the variance to probable cause (equipment malfunction, calibration drift, prescription loading error, operator bypass), and (5) generates a verification report for the agronomist to review. Over multiple seasons, the tool identifies systematic application errors that can be corrected.

## Who Feels the Pain
Agronomists who invest hours generating optimized prescriptions but cannot verify whether their prescriptions were executed accurately. Farmers who pay for VRT application but do not know if they received the prescribed rates. Equipment operators who may be unknowingly applying incorrect rates due to calibration drift.

## Impact If Fixed
Prescription execution accuracy improves by 10-20% as systematic application errors are identified and corrected. Agronomist prescription improvement accelerates — with verified feedback, prescriptions improve faster over seasons. Input waste from over-application in low-yield zones decreases by 5-10%, saving $3-8/acre. The agronomist-farmer relationship strengthens through demonstrable prescription performance.
