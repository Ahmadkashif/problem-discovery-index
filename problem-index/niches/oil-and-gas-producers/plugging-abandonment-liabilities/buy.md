# Asset Retirement Obligation Software Adapted to Well Inventories

**Niche:** [[niches/oil-and-gas-producers/plugging-abandonment-liabilities/profile|Plugging & Abandonment Liabilities]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lease and asset-retirement accounting software already discounts and accretes future obligations; it does not know a well's depth, state rules or idle status.
**Tags:** #linear-regression #feature-engineering #data-integration #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to estimate what each idle well will cost to plug and when the regulator will force it, and whoever's plugging estimates land closest to the final plugging invoices takes the account.

## The Problem
Accountants compute ARO from a cost estimate and a timing assumption per well, discount it and accrete it each quarter. The cost and timing inputs are guesses, maintained in spreadsheets, and the auditor asks for support.

## What Already Exists
Lease accounting and ARO modules in ERPs and specialist tools (Visual Lease, LeaseQuery and similar) handle discounting, accretion and disclosure schedules.

## The Customization Gap
Well-level inputs: cost estimates from depth, casing and state; timing from production decline, economic limit and state inactive-well rules; bonding and financial assurance by state and federal lease; and updates when wells are sold, plugged or reactivated. Links to commission well records keep the inventory current.

## Target Customer
Controllers at mid-size operators with thousands of wells and audit scrutiny on ARO.

## Impact If Solved
For an operator with ~3,000 wells (estimate), replacing a spreadsheet ARO with a well-level, auditable schedule cuts quarter-end ARO preparation from ~3 days to a few hours (estimate) and gives auditors support for every input.
