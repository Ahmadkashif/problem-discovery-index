# Budget Version Control Chaos

**Niche:** [[niches/event-planning/budget-reconciliation/profile|Budget & Invoice Reconciliation]]
**Industry:** [[industries/event-planning|Event Planning]]
**Type:** Fix (Pain Point)
**One-liner:** The event budget changes 15-30 times during planning — and the planner, the client, and the vendors are often working from different versions.
**Tags:** #data-integration #automation #workflow-orchestration

## The Problem
An event budget is a living document. The client approves Version 1 at $40,000. The planner updates it when the AV quote comes in higher ($42,000 — Version 2). The client adds a photo booth ($43,500 — Version 3). The planner negotiates a venue discount ($42,800 — Version 4). Each version exists as a separate spreadsheet file: "Johnson Wedding Budget v4 FINAL.xlsx," "Johnson Wedding Budget v4 FINAL REVISED.xlsx," "Johnson Wedding Budget v4 FINAL REVISED (2).xlsx." The planner sends Version 4 to the client; the client references Version 2. The vendor quotes were based on the scope in Version 3. Nobody is sure which version is current.

## Why It's Still Broken
Event budgets live in spreadsheets because they're flexible and familiar. But spreadsheets have no version control, no change tracking, no approval workflows, and no way to notify stakeholders when numbers change. Cloud spreadsheets (Google Sheets) solve the single-source-of-truth problem but don't track what changed, when, and who approved it. The planner can't show the client "here's what changed since you last approved the budget" — they can only show the current numbers.

## What a Fix Looks Like
A version-controlled event budget with change tracking: every modification is logged (who changed what, when, by how much), client approvals are recorded on specific versions, and stakeholders always see the current version with a change log since their last review. Budget updates trigger notifications to the client showing only what changed: "AV increased $2,000 (new quote), florist decreased $500 (seasonal adjustment), net change +$1,500, new total $43,500." The client approves the changes with one click, creating an auditable approval trail.

## Who Feels the Pain
Event planners who discover during final settlement that the client approved a budget from 3 versions ago and disputes $3,000 in changes they never formally approved, and clients who feel blindsided by final invoices that don't match the budget they remember.

## Impact If Fixed
Eliminates budget disputes at settlement (which occur in 20-30% of events), saves 2-3 hours per event in version management, and builds client trust through transparent, tracked financial communication — reducing client anxiety about runaway costs.
