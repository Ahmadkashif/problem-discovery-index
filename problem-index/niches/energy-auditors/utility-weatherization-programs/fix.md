# Multi-Program Data Re-Entry

**Niche:** [[niches/energy-auditors/utility-weatherization-programs/profile|Utility Weatherization Programs]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Fix (Pain Point)
**One-liner:** Auditors enrolled in multiple utility programs re-enter the same audit data into different portal formats for each program, multiplying administrative time by the number of programs served.
**Tags:** #automation #data-integration #worker-facing #quick-win

## The Problem
A home performance contractor enrolled in 3 utility programs (electric utility rebate program, gas utility weatherization, and state energy office low-income program) completes an audit that qualifies for measures under all three programs. The auditor must submit the same project data — blower door results, insulation specs, HVAC efficiency ratings — into 3 different portals, each with different field names, required documentation, and submission workflows. What could be a single submission becomes 3 separate data entry sessions totaling 4-6 hours. The same data is entered slightly differently each time (one portal wants R-value, another wants insulation depth in inches, a third wants both), creating inconsistencies that trigger QA flags.

## Why It's Still Broken
Utility programs are administered by different entities (investor-owned utilities, municipal utilities, state agencies) using different technology platforms chosen independently. There is no industry standard for audit data exchange format — HPXML (Home Performance XML) exists as a specification but adoption by program portals is sporadic. Each program views its portal as the authoritative data source and has no incentive to accept data from a competing program's system. The result is a Balkanized data landscape where the auditor is the manual integration layer.

## What a Fix Looks Like
A canonical audit data repository where the auditor enters project data once and the system translates it into each program's submission format — mapping fields, converting units, attaching the correct photo set, and generating program-compliant outputs. When the auditor adds insulation depth (6 inches of cellulose), the system calculates R-value (R-21), maps it to each program's field name (Program A: "attic_r_value," Program B: "insulation_R," Program C: dropdown selection "R-19 to R-30"), and pre-fills each submission. Changes in one program's submission auto-cascade to others where applicable.

## Who Feels the Pain
Home performance contractors enrolled in 2-4 programs who spend 50-60% of their office time on data entry rather than field work, and small audit companies where the owner is both the auditor and the administrator.

## Impact If Fixed
Cuts multi-program submission time by 60-70% (saving 2-4 hours per project for multi-program auditors), eliminates cross-program data inconsistencies, and enables auditors to enroll in more programs without proportional administrative burden — directly increasing revenue per audit.
