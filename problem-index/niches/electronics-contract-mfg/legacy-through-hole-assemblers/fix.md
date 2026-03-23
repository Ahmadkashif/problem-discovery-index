# IPC-A-610 Inspection Bottleneck on Through-Hole Joints

**Niche:** [[niches/electronics-contract-mfg/legacy-through-hole-assemblers/profile|Legacy Through-Hole Assembly Houses]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** 100% visual inspection of through-hole solder joints against IPC-A-610 workmanship standards — checking fill, wetting, bridging, and cold joint indicators on every pin of every component — takes 5-15 minutes per board and is the production bottleneck at most THT shops.
**Tags:** #cnns #object-detection #tacit-knowledge-ml #worker-facing

## The Problem
Through-hole solder joints are inspected visually under magnification against IPC-A-610 acceptance criteria. An inspector checks solder fill (visible through the barrel from the solder side), wetting angle, fillet formation, bridging between adjacent pins, cold joint indicators (grainy/dull surface), and flux residue. A typical board has 100-500 through-hole joints, each requiring individual assessment. Experienced inspectors develop pattern recognition — they scan a board and their eye is drawn to suspect joints without consciously evaluating each one — while new inspectors must check each joint sequentially, taking 2-3x longer. At THT shops where every board requires 100% visual inspection (no AOI system exists for through-hole), inspection is the throughput bottleneck.

## Why It's Still Broken
AOI systems are designed for SMT — they inspect surface-mount solder joints from above. Through-hole joints must be inspected from the solder side (bottom of the board) and ideally from the component side (top) to verify fill through the barrel. No commercial AOI system is designed for through-hole joint inspection. The through-hole market is too small and declining for major AOI vendors (Koh Young, Mirtec) to develop a dedicated product. Manual visual inspection remains the only option, and inspector hiring is increasingly difficult as the role requires IPC-A-610 certification and the pay ($15-20/hour) is not competitive with less demanding manufacturing jobs.

## What a Fix Looks Like
A camera-based inspection aid that captures an image of the solder side of each board after wave solder, uses a CNN model trained on IPC-A-610 acceptance criteria for through-hole joints to identify suspect joints, and presents only the suspect joints to the inspector for final disposition. The inspector reviews 10-30 flagged joints instead of visually scanning 100-500 joints — a 70-80% reduction in inspection time. The model is not the final inspector (the human makes the accept/reject decision), so IPC-A-610 certification requirements are met while throughput increases dramatically.

## Who Feels the Pain
Inspectors who spend 6-8 hours per day under magnification, developing eye strain, neck pain, and fatigue-related accuracy degradation. Shop owners who cannot hire enough qualified inspectors to meet demand. Customers whose orders are delayed because inspection is the bottleneck.

## Impact If Fixed
Inspection throughput increases 3-5x per inspector. Inspector fatigue-related accuracy degradation is eliminated because the inspector focuses only on flagged joints. Inspector hiring pressure decreases — existing inspectors can handle 3-5x the volume with camera-assisted screening.
