# Timesheet-to-Budget Real-Time Reconciliation

**Niche:** [[niches/engineering-consultants/project-budget-forecasting/profile|Project Budget Forecasting & Change Orders]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Timesheets and project budgets live in separate systems — hours are entered days or weeks late, coded to wrong phases, and never reconciled against the proposal fee schedule until the project is over.
**Tags:** #data-integration #automation #anomaly-detection #worker-facing #revenue-impact

## The Problem
The proposal says Phase 1 (Schematic Design) is budgeted at 120 hours across 3 staff. Timesheets are entered weekly (or bi-weekly at many firms) by each engineer, who selects a project number and phase code from a dropdown. Reconciling actual hours against the phase budget requires the PM to export timesheet data, manually map it to the proposal fee schedule, and calculate remaining budget per phase. This export-and-calculate process takes 30-60 minutes per project per month, so PMs do it monthly at best — or never. When a junior engineer miscodes 20 hours to the wrong phase (or the wrong project entirely), the error is invisible until the reconciliation. By then, the PM has been making staffing decisions based on inaccurate budget data for weeks.

## Why It's Still Broken
Timesheet systems (Deltek, Harvest, Toggl) and proposal/contract management live in separate databases with different data models. The proposal defines scope in narrative phases ("Schematic Design," "Design Development"); the timesheet uses numeric phase codes ("Phase 1.0," "Phase 1.1") that may or may not map cleanly. Nobody maintains the mapping table between proposal phases and timesheet codes because it requires setup at project initiation — a step that is skipped in the rush to start work. The cultural problem compounds the technical one: engineers view timesheet entry as administrative overhead and resist detailed phase coding.

## What a Fix Looks Like
An automatic sync layer between the firm's timesheet system and its proposal/contract database. At project setup, the system creates timesheet codes that mirror the proposal phases and pre-populates the budget for each. Every time a timesheet entry is submitted, the system updates the budget-vs-actual dashboard and flags anomalies: "Junior Engineer X logged 15 hours to Phase 3 (Construction Administration), but Phase 3 hasn't started yet — possible miscoding." The PM sees a real-time budget status without running any manual exports, and coding errors are caught within 24 hours instead of months later.

## Who Feels the Pain
Project managers who fly blind on budget status between monthly reconciliations, and firm principals who discover fee erosion only at project closeout.

## Impact If Fixed
Eliminates 30-60 minutes per project per month of manual reconciliation (for a firm with 30 active projects, that's 15-30 hours/month). Catches timesheet coding errors within 24 hours, preventing the cascading budget distortions that lead to uninformed staffing decisions. Firms that implement real-time budget tracking report 5-8% improvement in project margins.
