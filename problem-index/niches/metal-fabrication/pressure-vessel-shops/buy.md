# Weld Map Management Linked to ASME Code Requirements

**Niche:** [[niches/metal-fabrication/pressure-vessel-shops/profile|Pressure Vessel & Tank Shops]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Weld tracking platforms like Lincoln Electric WeldCloud log welding parameters and wire consumption, but they don't understand ASME code requirements — which welds are code-required seams that need NDE, which WPS applies to each joint based on material and thickness, and whether the assigned welder is qualified for that specific WPS.
**Tags:** #data-integration #compliance #automation #worker-facing

## The Problem
A pressure vessel weld map identifies every weld seam on the vessel, assigns a WPS to each seam based on material combination and thickness, specifies the NDE requirement (radiography, ultrasonic, MT, PT) based on the joint category per ASME code, and assigns a qualified welder. Managing this map manually — updating it as welders change, tracking which seams are complete, ensuring the assigned welder's qualification covers the assigned WPS — is a daily coordination task for the quality supervisor. When a welder's qualification expires mid-project, the quality supervisor must catch this before the welder performs code work with an expired qualification — a compliance violation that can invalidate completed welds.

## What Already Exists
Lincoln Electric WeldCloud and Miller WeldSmart track welding parameters, wire consumption, and arc-on time per welder. These platforms provide productivity analytics but not code compliance management. They know that Welder #7 welded for 4.2 hours today — but not that Welder #7's qualification for WPS-003 expired last week, making the welds performed under that WPS potentially non-compliant.

## The Customization Gap
An ASME-aware weld management system needs: (1) weld map creation linked to vessel design — auto-generating the weld seam list from the vessel drawing with material, thickness, and joint category per ASME code; (2) WPS assignment rules — matching each weld seam to the appropriate WPS based on material combination, thickness range, and welding process; (3) welder qualification tracking — validating that the assigned welder holds current qualification for the assigned WPS before authorizing the weld; (4) NDE scheduling — automatically flagging code-required NDE based on joint category and generating the NDE request for the NDE contractor.

## Target Customer
Quality supervisors and ASME code administrators at pressure vessel shops with 10+ active welders and 5+ vessels in fabrication simultaneously.

## Impact If Solved
Prevents welder qualification compliance violations that invalidate completed welds — each incident requires rewelding at $500-$5,000 per weld seam plus project schedule impact. Automates NDE scheduling that is currently tracked on spreadsheets, ensuring 100% of code-required NDE is performed before the AI review. Reduces weld map management labor by 50-60% — from 2-3 hours daily to 1 hour of exception handling.
