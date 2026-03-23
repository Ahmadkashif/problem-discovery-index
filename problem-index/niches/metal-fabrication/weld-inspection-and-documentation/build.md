# AI-Assisted Weld Visual Inspection System

**Niche:** [[niches/metal-fabrication/weld-inspection-and-documentation/profile|Weld Inspection & Documentation]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No production-deployable system captures weld images under controlled illumination, detects defect indications (porosity, undercut, overlap, cracks), classifies severity relative to the applicable code acceptance criteria, and generates inspection documentation automatically — the full inspection workflow from image capture to quality record.
**Tags:** #cnns #transfer-learning #evaluation-metrics #tacit-knowledge-ml #compliance #revenue-impact

## The Problem
Weld visual inspection is the most skill-dependent quality step in fabrication. A CWI examines each weld for surface indications — porosity (spherical interruptions), undercut (groove at weld toe), overlap (rolled weld metal), cracking (linear indications), and inadequate size — and determines whether each indication is within the acceptance criteria of the applicable welding code. This assessment takes years to calibrate: the CWI must distinguish acceptable weld surface appearance from rejectable conditions at the boundary where codes are ambiguous ("porosity shall not exceed 3/32 inch in any linear inch" — but is that indication porosity or surface contamination, and does it actually measure 3/32?). With 40,000 CWIs in the US and growing demand from infrastructure projects, the inspection workforce cannot scale with production demand.

## Why Nobody Has Built This
Weld defect detection via computer vision is technically demonstrated in academic research, but production deployment requires: (1) controlled illumination at the inspection point (ambient shop lighting is inconsistent), (2) training data labeled by experienced CWIs (expensive annotation, with 5-10% inter-annotator disagreement on borderline cases), (3) defect size measurement from images (not just detection but dimensional assessment against code thresholds), and (4) code-configurable acceptance criteria (different codes have different thresholds for the same defect type). Each of these requirements adds deployment complexity beyond basic object detection.

## What to Build
An integrated inspection station: LED light array with consistent illumination, high-resolution camera, and inference computer. The CWI positions the weld under the camera, captures an image, and the system displays: detected indications with bounding boxes, defect type classification, estimated dimensional measurements, and accept/reject recommendation per the configured code. Borderline cases (confidence below threshold) are flagged for CWI judgment. Every inspection decision is logged with the supporting image, creating an automatic quality record. The CWI's role shifts from routine accept/clear decisions to boundary-case judgment and model oversight.

## Target Customer
Quality managers at fabrication shops with 2+ CWIs and 50+ inspected welds per day, where inspection throughput is a production bottleneck. Approximately 3,000-5,000 shops in the US.

## Impact If Built
Multiplies CWI capacity by 3-4x — the CWI reviews AI-flagged borderline cases rather than inspecting every weld visually. Enables 100% inspection coverage (eliminating sampling inspection) without additional CWI headcount. For a structural fabricator with 3 CWIs inspecting 200 welds/day at 50% capacity utilization, AI-assisted inspection enables the same 3 CWIs to cover 600-800 welds/day — eliminating the inspection bottleneck and the quality escape risk of uninspected welds.
