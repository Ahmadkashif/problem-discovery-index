# Keeping the Number Before It Is Overwritten

**Niche:** [[niches/revops-consultancies/snapshot-retention/profile|Forecast Snapshot Retention]]
**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A week of engineering stands between the discipline and its first measurable claim.
**Tags:** #data-integration #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #compliance #quick-win #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to capture every forecast at every level before it is overwritten, because nothing downstream is possible without that series — and whoever captures it takes the account.

## The Problem
The forecast exists as current state. Fields hold this week's number; next week they hold next week's. The pipeline behaves the same way — stages, amounts and close dates are updated in place, so the history of how a deal moved is unrecoverable. Every question anyone wants to ask about forecasting requires a series that the systems are actively destroying, and nobody is capturing it because it has never been anyone's task.

## Why Nobody Has Built This
CRM platforms record current state and provide history only selectively. Nobody owns the question. Consultancies sell methodology, which is the thing that cannot be evaluated without this. And it is invisible: nothing breaks when history is lost.

## What to Build
Capture everything, on a schedule, immutably. Snapshot forecast and pipeline state on a fixed cadence into an immutable store, which is the core and is the entire product. Capture at every level of the hierarchy rather than the rolled-up number, since bias lives at the representative level. Include the commit, best-case and worst-case positions separately, as the spread is informative. Capture the full opportunity state — stage, amount, close date, owner, age — so deal movement can be reconstructed. Snapshot at the same moment each week relative to the forecast call, which makes comparisons valid. Store outside the operational system so administration changes cannot destroy the history. Recover whatever historical snapshots exist in archived spreadsheets and reports, which typically yields a few quarters and is worth the afternoon. Record the forecast methodology in force at each snapshot, so a later change is evaluable. Keep it indefinitely, since the storage cost is negligible and the analytical value compounds. And make it a standard first deliverable on every engagement, because every subsequent recommendation depends on it.

## Target Customer
Revenue operations teams, RevOps consultancies, CRM and revenue intelligence vendors, and data platform providers.

## Impact If Built
Every question anyone wants to ask about forecasting requires a series the systems are actively destroying. Scheduled immutable snapshots at every level are a week of engineering and the precondition for everything else.
