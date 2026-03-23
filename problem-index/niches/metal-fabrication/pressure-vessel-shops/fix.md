# Manual NDE Record Assembly and Inspector Coordination

**Niche:** [[niches/metal-fabrication/pressure-vessel-shops/profile|Pressure Vessel & Tank Shops]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Fix (Pain Point)
**One-liner:** NDE records — radiographic film interpretations, ultrasonic test results, and surface examination reports — arrive from the NDE contractor as separate documents that must be manually matched to specific weld seams on the weld map and assembled into the vessel's documentation package.
**Tags:** #automation #compliance #data-integration #worker-facing

## The Problem
ASME code vessels require NDE (radiography, ultrasonic, magnetic particle, or liquid penetrant testing) on code-required weld seams. NDE is typically performed by a third-party NDE contractor who visits the shop, examines the specified welds, and issues individual examination reports. The quality coordinator receives these reports — sometimes paper, sometimes PDF — and must match each report to the corresponding weld seam on the vessel's weld map, verify that the NDE method matches the code requirement for that joint category, confirm the NDE technician's certification level is adequate for the examination type, and file the report in the vessel's documentation package. For a vessel with 50 code-required NDE examinations, this matching and filing process takes 4-8 hours.

## Why It's Still Broken
NDE contractors use their own report formats and identification systems. They label welds by their own numbering convention, which may not match the fabricator's weld map numbering. Reconciling "NDE Report #2847, Weld W-15 per sketch attached" with "Weld Seam 22 on Vessel V-2024-037 Weld Map Rev. C" requires manual cross-referencing. Digital NDE reporting standards exist (DICONDE for radiography) but are not universally adopted. The NDE contractor's incentive is to perform and report the examination — not to integrate their reporting with the fabricator's documentation system.

## What a Fix Looks Like
A shared weld examination portal where the fabricator creates an NDE request linked to specific weld seams on the vessel's weld map. The NDE contractor receives the request with unambiguous weld identification (vessel number, weld seam number, location sketch), performs the examination, and uploads the report directly to the weld seam record. The quality coordinator sees a dashboard showing NDE completion status per vessel — which welds are examined, which are pending, which have unacceptable results requiring repair and re-examination. No manual report-to-weld-map matching required.

## Who Feels the Pain
Quality coordinators who spend hours matching NDE reports to weld maps, and NDE contractors who are called back to the shop when their reports don't clearly identify which weld was examined — a coordination failure that delays both parties.

## Impact If Fixed
Eliminates NDE report matching labor — 4-8 hours per vessel. Prevents missing NDE records that delay ASME AI review. Reduces NDE contractor revisits caused by unclear weld identification. For a shop fabricating 30 vessels/year with average 50 NDE examinations each, saves 120-240 quality hours annually and prevents 2-3 weeks of cumulative AI review delays.
