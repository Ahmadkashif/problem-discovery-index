# Migration Progress Tracking Across Thousands of Programs

**Niche:** [[niches/software-dev-agencies/legacy-modernization-shops/profile|Legacy System Modernization Shops]]
**Industry:** [[industries/software-dev-agencies|Software Dev Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Modernization agencies track the migration status of 1,000-10,000 individual COBOL programs in spreadsheets, losing visibility into dependencies, blockers, and true completion percentage.
**Tags:** #workflow-orchestration #data-integration #quick-win

## The Problem
A mainframe modernization project migrates individual programs (or groups of programs) in waves over 12-36 months. Each program moves through states: assessed, business rules extracted, target architecture designed, coded, unit tested, integration tested, equivalence verified, deployed. The project manager tracks 2,000 programs across these states in an Excel spreadsheet with 16,000+ cells. When a dependency is discovered (Program A calls Program B, so B must be migrated first), the spreadsheet cannot model it. When a program is blocked (waiting for a business user to confirm a rule), the PM updates a note field that nobody reviews. Weekly status reports are manually compiled by counting rows in each state column.

## Why It's Still Broken
JIRA and Azure DevOps can track individual tasks but do not model program-to-program dependencies at the scale of legacy modernization (2,000 programs with 5,000+ call-chain dependencies). Creating a JIRA ticket per program is theoretically possible but creates an unmanageable backlog — PMs need a portfolio view, not a ticket queue. Migration-specific tools like CloudEndure and AWS Migration Hub track infrastructure migration, not application-level code migration. No project management tool understands the migration lifecycle stages specific to mainframe modernization.

## What a Fix Looks Like
A migration tracking dashboard built for legacy modernization that: (1) imports the program inventory from the mainframe code repository, (2) auto-discovers program-to-program dependencies through call graph analysis, (3) tracks each program's migration stage with dependency-aware scheduling (cannot start Program A until Program B is complete), (4) surfaces blockers and their downstream impact ("this blocked program is delaying 47 dependent programs"), and (5) generates progress reports with accurate completion percentages weighted by program complexity, not just count.

## Who Feels the Pain
Project managers and engagement leads at legacy modernization agencies who spend 10-15 hours/week maintaining migration tracking spreadsheets and compiling status reports manually.

## Impact If Fixed
Saves 10-15 hours/week of PM time per project. Reduces migration timeline overruns by 20-30% through early blocker identification and dependency-aware scheduling. Improves client confidence through real-time, accurate progress visibility.
