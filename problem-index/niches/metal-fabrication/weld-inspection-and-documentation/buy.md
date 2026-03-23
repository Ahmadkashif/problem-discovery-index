# Digital Weld Inspection Log with Code Compliance

**Niche:** [[niches/metal-fabrication/weld-inspection-and-documentation/profile|Weld Inspection & Documentation]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Digital inspection platforms like GoCanvas and iAuditor capture inspection data on mobile forms, but they don't understand welding code acceptance criteria — they can record "undercut: 1/32 inch" but can't determine whether that value is acceptable or rejectable per AWS D1.1 Table 6.1 for a statically loaded structure vs. a cyclically loaded structure.
**Tags:** #automation #compliance #data-integration #worker-facing

## The Problem
CWIs currently record inspection results on paper logs or in generic mobile form apps. Neither approach connects the inspection measurement to the applicable acceptance criteria. The CWI mentally references the code (AWS D1.1, ASME Section IX, customer specification) to determine accept/reject — but this reference is not documented in the inspection record. The log shows "undercut: 1/32 inch — ACCEPT" but doesn't record that the acceptance criterion was "AWS D1.1 Table 6.1 for statically loaded structures permits undercut up to 1/32 inch." When a customer auditor reviews the inspection log, they cannot verify the acceptance basis without re-reading the code themselves.

## What Already Exists
GoCanvas and iAuditor provide configurable mobile inspection forms. Lincoln Electric CheckPoint provides weld parameter logging. These tools capture data but don't encode acceptance criteria logic — they are generic data collection platforms with no welding code intelligence.

## The Customization Gap
A code-aware weld inspection log needs: (1) acceptance criteria database — encoded acceptance limits from AWS D1.1, D1.2, D1.6, ASME Section IX, and common customer specifications; (2) automatic disposition — given the inspection measurement and the applicable code, automatically determine accept/reject and display the specific code clause that governs the decision; (3) code-section configuration per job — configuring which code and which loading condition (static vs. cyclic) applies to a specific project, so all inspections on that project reference the correct criteria; (4) photo attachment per weld — linking the inspection photo to the disposition record for audit traceability.

## Target Customer
CWIs and quality managers at fabrication shops performing code welding, where inspection documentation must reference specific code acceptance criteria for customer audit compliance.

## Impact If Solved
Eliminates the mental code reference step that slows CWI inspections — the acceptance criterion is displayed automatically. Creates audit-ready inspection records that document the acceptance basis, not just the measured value. Reduces inspection documentation time by 30-40% — the CWI enters the measurement, the tool determines the disposition and records the code reference. For a shop with 2 CWIs inspecting 100 welds/day, recovering 30% of documentation time frees 2-3 hours daily for additional inspection capacity.
