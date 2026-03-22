# Panel Inspection & Diagnostics

**Parent Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $3-5B (embedded across all electrical contracting segments)
**Share of Parent Industry:** Touches all segments — every service call, home inspection, and maintenance visit involves panel assessment
**Digital Adoption:** Low-Medium — thermal imaging cameras are common but image interpretation is entirely manual. No digital tools exist for visual panel defect identification.
**Target Buyer:** Master electrician, home inspector, residential service company owner
**Automation Potential:** Very High — panel inspection is the #1 tacit knowledge task in electrical contracting, where experienced electricians identify defects in seconds that juniors miss entirely. The visual patterns (double-tapped breakers, heat damage, manufacturer identification) are well-suited to CNN-based object detection.

## What Makes This a Distinct Niche
Panel inspection is the single most experience-dependent task in electrical contracting. When a master electrician opens a residential panel cover, they process dozens of visual signals simultaneously in 10-15 seconds: they identify the panel manufacturer (Federal Pacific Stab-Lok and Zinsco panels are fire risks requiring replacement), spot double-tapped breakers (two wires on a single-pole breaker rated for one), notice heat discoloration on wires or bus bars indicating overloaded circuits, identify wire gauge mismatches (14-gauge wire on a 20A breaker), see corrosion from water intrusion, and assess overall workmanship quality. This gestalt assessment takes 5-10 years of daily panel exposure to develop. A junior electrician or home inspector looking at the same panel might catch 1-2 of 5-6 issues, or might miss a Federal Pacific panel entirely if the label is worn. The consequence of missed defects ranges from code violations to house fires — Federal Pacific panels alone are estimated to cause 2,800 fires per year in the US.

## Current Tools & Gaps
Thermal imaging cameras (FLIR, Fluke) identify hot spots indicating overloaded connections but require training to interpret (not every hot spot is a problem; temperature differentials relative to ambient and load conditions matter). No tool assists with visual panel defect identification. Home inspection software (Spectora, HomeGauge) provides report templates with electrical checkboxes but no diagnostic assistance. The entire panel assessment process is human judgment with no digital augmentation.

## Problems
- [[niches/electrical-contractors/panel-inspection-diagnostics/build|🔨 Build: AI Panel Inspection from Photos]]
- [[niches/electrical-contractors/panel-inspection-diagnostics/buy|🛒 Buy: Thermal Image Interpretation for Electrical Panels]]
- [[niches/electrical-contractors/panel-inspection-diagnostics/fix|🔧 Fix: Panel Inspection Quality Calibration]]
