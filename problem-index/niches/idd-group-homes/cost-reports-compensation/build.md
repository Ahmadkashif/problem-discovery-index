# One Allocation Model Behind Every State Cost Template

**Niche:** [[niches/idd-group-homes/cost-reports-compensation/profile|Cost Reports & Direct Care Compensation Reporting]]
**Industry:** [[industries/idd-group-homes|IDD Group Homes]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every state filing asks how each service dollar was spent, and the agency rebuilds the answer from raw payroll for each one.
**Tags:** #linear-regression #feature-engineering #data-integration #compliance #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to produce the agency's cost reports and direct care compensation figures straight from payroll, ledger and claims data, and whoever files with the fewest state audit adjustments takes the account.

## The Problem
The controller spends weeks each year allocating payroll, benefits, mileage and overhead to ICF/IID cost centres, waiver services and homes for the cost report. She does it again for a rate-study survey, and from 2028 will do it again for the state's compensation-share collection. Each allocation is a spreadsheet with its own assumptions, and auditors adjust what they cannot trace.

## Why Nobody Has Built This
Payroll and ERP vendors do not know Medicaid service categories; cost-report specialists are services firms that rebuild the model per client per year.

## What to Build
A persistent allocation model connected to payroll, timeclock, ledger and claims. It maps every hour and cost to service, home, funding source and the Access Rule's worker and excluded-cost categories, with documented rules. From that one model it generates each state's cost-report template, rate-study survey responses and compensation-share figures, with an audit trail from each reported number back to source records. It flags allocations that changed from last year.

## Target Customer
CFOs and controllers at agencies with ICF/IID cost reporting or large waiver programmes; accounting firms serving several providers.

## Impact If Built
~3–6 weeks of a controller's annual allocation work shrink to ~1 week of review (estimate). Audit adjustments fall because every figure traces to source; on a cost-based ICF/IID rate, one avoided disallowance can be worth ~$20,000–100,000 a year (estimate). The agency also enters rate negotiations with defensible cost data.
