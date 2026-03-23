# Plat & Subdivision Review

**Parent Industry:** [[industries/land-surveyors|Land Surveyors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $900M (labor cost)
**Share of Parent Industry:** ~7% of surveyor and municipal reviewer time
**Digital Adoption:** Low-Medium — Subdivision plats are still submitted as paper or PDF to municipal review offices. Review is done by a licensed surveyor or engineer reading the plat against a checklist, redlining deficiencies by hand.
**Target Buyer:** Municipal Reviewer / Development Surveyor / Planning Department
**Automation Potential:** High — Plat review is a compliance-checking process against codified municipal ordinances, subdivision regulations, and survey standards — all rule-based criteria that can be algorithmically verified.

## What Makes This a Distinct Niche
When a developer subdivides a parcel into lots, the surveyor prepares a subdivision plat — a map showing lot boundaries, easements, right-of-way dedications, utilities, setback lines, and detailed lot data. This plat must be reviewed and approved by the municipality before recording. Municipal review checks 50-100 requirements: minimum lot sizes, street frontage, easement widths, setback compliance, flood zone notation, utility access, drainage easements, and geometric accuracy. A single reviewer may handle 5-20 plats per week, spending 2-4 hours on each. Review is almost entirely visual — reading the plat against printed ordinance requirements, measuring dimensions with a scale ruler, and marking deficiencies with red ink. The rejection rate is high (50-70% require at least one revision), creating cycles of submission, review, correction, and resubmission that delay development by weeks.

## Current Tools & Gaps
Municipal reviewers typically use PDF viewers (Bluebeam, Adobe) to annotate submitted plats. Some jurisdictions use electronic plan review systems (ProjectDox, ePlans) for submission workflow but not for substantive review — the reviewer still reads the plat manually. Surveyors prepare plats in CAD (Civil 3D, Carlson) but submit as PDF, losing the structured data. No tool checks a plat against the municipality's subdivision ordinance automatically. The gap is between the structured geometric data in the CAD file and the unstructured manual review process.

## Problems
- [[niches/land-surveyors/plat-subdivision-review/build|🔨 Build: Automated Subdivision Plat Compliance Checker]]
- [[niches/land-surveyors/plat-subdivision-review/buy|🛒 Buy: Electronic Plan Review Adapted for Subdivision Plat Specifics]]
- [[niches/land-surveyors/plat-subdivision-review/fix|🔧 Fix: Submit-Reject-Revise Cycles Delaying Development by Months]]
