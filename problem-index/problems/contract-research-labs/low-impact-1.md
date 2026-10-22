# Indirect Rates and Incurred-Cost Submissions on a General Ledger

**Industry:** [[contract-research-labs|Contract Research Labs]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A research firm that wins its first cost-type contract has to run government cost accounting — allowable costs, indirect pools, provisional billing rates, an incurred-cost submission six months after year end — on accounting software built for a shop that sells widgets.
**Tags:** #time-series-forecasting #linear-regression #exponential-smoothing #feature-engineering #compliance #data-integration #automation

## The Problem
A small research firm typically starts on firm-fixed-price SBIR Phase I awards, where cost accounting barely matters. The first cost-reimbursement Phase II, DARPA subcontract or agency task order changes that. The firm must segregate unallowable costs under FAR Part 31 (entertainment, some interest, lobbying, certain bid costs), build indirect pools — fringe, overhead, general and administrative — with defensible allocation bases, bill at provisional rates, and reconcile to actual rates at year end. On cost-type contracts the incurred-cost submission is due six months after fiscal year end under FAR 52.216-7, and DCAA may audit both the accounting system and the submission.

In practice a part-time bookkeeper and the founder run it in QuickBooks plus a spreadsheet of rate calculations. Timesheets are corrected after the fact, the overhead pool absorbs a research technician who charged to the wrong line, and the firm discovers in month eleven that its provisional overhead rate was ten points too low and it has under-billed all year (estimate of a common case).

## What Already Exists
General-ledger packages (QuickBooks Online, Xero, Sage Intacct) with add-on timekeeping that advertises DCAA compliance; government-contract ERPs such as Unanet GovCon and Deltek Costpoint, which compute indirect rates, enforce DCAA timesheet rules and support incurred-cost submissions; and outsourced government-contract accountants who build the rate model in Excel each year.

## The Customisation Gap
The general ledgers record cost but do not understand a research firm's cost structure: which accounts are unallowable, which pool a cost belongs to, how a bid-and-proposal hour differs from an internal research hour and from a direct contract hour, and how a rate change ripples into every open contract's billing. The government-contract ERPs understand it, but are priced and configured for mid-size contractors, take months to implement and assume a finance team a ten-person lab does not have. The missing layer is research-firm logic on top of the ledger the firm already uses: an account-to-pool map with allowability flags, a running forecast of year-end indirect rates against provisional billing rates, alerts when a timesheet pattern would fail a floor check, and incurred-cost schedules assembled from the ledger rather than rekeyed.

## Impact If Solved
A small lab sees a rate variance in month three rather than month eleven, avoids the under-billing that otherwise comes back as a year-end cash shortfall, and files a submission DCAA can accept without a consultant rebuilding it — saving tens of thousands of dollars a year in outside accounting and protecting the firm's eligibility for cost-type work (estimate).
