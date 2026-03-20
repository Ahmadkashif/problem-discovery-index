# EVV-Payroll-Clinical Note Reconciliation

**Industry:** [[home-health-agencies|Home Health Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Electronic Visit Verification, payroll time tracking, and clinical documentation are three separate records of the same visit that never agree — and someone has to reconcile them manually every pay period.
**Tags:** #logistic-regression #decision-trees #feature-engineering #evaluation-metrics #automation #compliance #quick-win

## The Problem
Every home health visit generates three data records: the EVV check-in/check-out (mandated by the 21st Century Cures Act, capturing time and location via GPS), the clinical visit note (documenting care delivered, signed by the clinician), and the payroll time entry (capturing hours worked for compensation). In theory, these should match. In practice, EVV timestamps don't match note completion times (clinicians often finish notes in their car after leaving), GPS locations drift, and payroll entries are rounded to different increments. Someone in the office — usually a billing coordinator — must manually reconcile discrepancies before claims can be submitted and payroll can be processed.

## What Already Exists
EVV vendors (Sandata, HHAeXchange, CellTrak) handle the verification mandate. Payroll systems (ADP, Paychex) handle compensation. EHRs handle clinical documentation. Each does its own job adequately.

## The Customisation Gap
No system natively reconciles all three records against each other with home health-specific tolerance rules (e.g., a 10-minute gap between EVV check-out and note signature is normal because the clinician documented in the driveway; a 4-hour gap suggests a missed EVV check-in). The reconciliation logic needs to understand home health visit patterns, payer-specific EVV requirements, state-level regulations, and the agency's payroll rules.

## Impact If Solved
Eliminates 8-12 hours per week of manual reconciliation work for a mid-size agency. Reduces claim submission delays caused by EVV discrepancies from days to hours.
