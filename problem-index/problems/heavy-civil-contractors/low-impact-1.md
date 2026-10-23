# Time Impact Analyses Rebuilt for Every Owner's Schedule Spec

**Industry:** [[heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Primavera P6 can model any delay, but each owner's schedule specification sets its own notice clock, analysis method and file format, so every time impact analysis on a Corps, transit or port job is built by hand against a different rulebook.
**Tags:** #large-language-models #transformers #graph-theory #feature-engineering #compliance #workflow-orchestration #automation

## The Problem
On a Corps of Engineers contract, the schedule specification (UFGS-01 32 01.00 10, revised August 2026) requires a justification of delay "within 10 days of a delay occuring". It wants a prospective time impact analysis built to AACE 52R-06 on a copy of the last approved schedule before the impact, a fragnet showing every predecessor and successor, and proof that the delay consumed all project float before a day is granted. The schedule must be updated monthly, activities may not exceed 20 workdays, and the file goes in as a P6 .xer or the Corps' Standard Data Exchange Format. A transit agency's spec uses a different update cycle and delay method, a port authority's another, and a railroad's design-build contract another again.

The project scheduler, often one person covering several jobs, does this by hand. They pull the daily reports and RFIs that show when the impact began, build the fragnet, insert it into the right baseline, run the schedule, and write the narrative. A high-water event, a late permit, a differing site condition and a design change can stack in the same month. Each needs its own analysis, in order, with concurrency considered.

## What Already Exists
Oracle Primavera P6 and its peers schedule anything. Schedule-quality checkers (Acumen Fuse-type tools, DCMA 14-point checks) test logic. Forensic schedule analysts sell retrospective delay analysis once a claim is likely, the work mapped at [[niches/general-contractors/construction-claims-forensics/profile|Construction Claims & Schedule Forensics]]. Project management platforms log RFIs and daily reports, and the scheduling function is mapped for general contractors at [[niches/general-contractors/project-scheduling-management/profile|Project Scheduling & Management]].

## The Customisation Gap
The generic tools don't know the owner's rulebook. What a heavy civil scheduler needs layered on is the spec itself, parsed into rules: the notice clock and who it runs to, the required method (AACE 52R-06 prospective, 29R-03 retrospective, ASCE 67-17 principles), float ownership, duration limits, activity coding, cost-loading, and the required file format. It also needs the contract's own event types: high water and river stages for marine and lock work, track-outage windows for rail, environmental windows such as dredging bans for turtle or fish seasons, and owner-furnished items. It then needs the link from the field record (daily report, RFI, survey) to the schedule activity, so the fragnet is drafted from evidence rather than reconstructed from memory. None of that is in P6.

## Impact If Solved
If a scheduler can produce a compliant draft TIA in hours rather than ~3–5 days (estimate), notices go in inside the 10-day window instead of being late or skipped. Time extensions then get granted on the merits, and fewer delays turn into the claims that consume a contractor's margin and a forensic firm's fees years later.
