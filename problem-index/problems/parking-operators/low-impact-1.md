# The Owner's Monthly Statement Built From Six Systems

**Industry:** [[parking-operators|Parking Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every managed facility needs a monthly owner statement that reconciles PARCS sessions, app and marketplace payouts, monthly billing, validations, card settlements and reimbursable payroll, and generic accounting and reconciliation tools know none of those parking objects.
**Tags:** #large-language-models #gaussian-mixture-models #change-point-detection #feature-engineering #data-integration #automation #compliance

## The Problem
Under a management contract the operator collects the owner's revenue, pays approved expenses out of it, takes a fee and remits the rest. About 88% of SP+'s commercial locations ran this way in 2023, and Mobile Infrastructure Corporation moved its own garages from leases to management contracts in 2024. Every month a revenue-control analyst at the operator builds one statement per facility. Transient revenue comes from the PARCS: tickets issued, tickets closed, lost-ticket fees, voids and gate overrides. Monthly revenue comes from a billing system or a spreadsheet of tenant accounts. Reservations come from SpotHero, ParkWhiz and the operator's own app, each paid out net of its own commission on its own schedule. Validations come from retailers and hotels, and card settlements from the processor. Payroll charged back to the owner has to follow the contract's rules for union rates, overtime and supervisors shared between sites. An analyst covering ~30–60 facilities spends the first ~10 days of each month (estimate) stitching these together in Excel. The owner's asset manager then reads the statement, asks why transient revenue fell 8% while entries rose 2%, and waits a week for the answer.

## What Already Exists
General ledgers (NetSuite, Sage Intacct, Yardi for real-estate owners), account-reconciliation and close tools (BlackLine, FloQast), BI dashboards in Power BI or Tableau, and each PARCS vendor's own revenue reports (FLASH, Amano McGann, SKIDATA). Marketplaces send payout files and operator portals. Owners hire outside auditors such as RSM, which audited Arlington County's SP+ garage contract in 2026, to check compliance after the fact.

## The Customisation Gap
The generic tools reconcile bank balances and journal entries, not parking sessions. The parking-specific logic is matching sessions to money: entries against exits against paid tickets, with voids, lost tickets and gate-arm overrides flagged per cashier and per shift. Monthly cards issued have to match those billed, and validations redeemed have to match those invoiced to the validating tenant. Each marketplace booking needs its gross price, commission and payout date, and the analyst has to separate a cardholder who never came from a booking that never paid. On top of that sit the contract rules: which expenses are reimbursable, the incentive fee formula, rate-change approvals and the owner's reporting template. Each management contract is different, and those rules live in the analyst's head and a PDF.

## Impact If Solved
A parking-specific close that drafts each owner statement and explains the top variances in plain language would cut the analyst's monthly close from ~10 days to ~3 for 30–60 facilities (estimate). It would also catch the 1–3% of gross revenue that typically leaks at cash-handling facilities (estimate) before the owner's auditor finds it.
