# Training and Calibration Records Kept Apart From the Work

**Niche:** [[niches/aircraft-mro-shops/small-part-145-repair-stations/profile|Small Part 145 Repair Stations]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Fix (Pain Point)
**One-liner:** A technician signs a release while their recurrent training has lapsed, using a gauge two weeks past calibration, and nobody knows until an auditor samples the job.
**Tags:** #compliance #workflow-orchestration #automation #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep a small repair station's certificate and its customers' approvals with a one-person quality department, and whoever leaves the fewest findings per FAA and customer audit takes the account.

## The Problem
Training records (145.163) and tool calibration records (145.109) live in spreadsheets maintained by the quality manager. Work orders record who did the job and, at best, which tools. Nothing checks at sign-off that the person was current for the task and the tools were in calibration, so lapses surface at audit, and every job touched by a lapsed tool may need review.

## Why It's Still Broken
The records are kept for the auditor, not for the work. Linking them requires tool IDs on work orders and task-level training qualifications, which small shops have never had a system to hold.

## What a Fix Looks Like
Tool and technician checks at the moment of sign-off: scan or select the tools used, and the work order confirms calibration status and the technician's authorisation for that task and article. Expiring items show a week ahead. If a tool is found out of tolerance, the system lists every job it touched since its last good calibration.

## Who Feels the Pain
Quality managers facing findings; technicians whose signatures are questioned; customers asked to accept re-inspection of released parts.

## Impact If Fixed
Preventing even one out-of-calibration recall a year, which can mean re-inspecting ~20–100 released articles (estimate), saves weeks of work and protects a customer approval worth far more than the system.
