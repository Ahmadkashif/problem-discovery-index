# The Account Margin Explained by the Work

**Niche:** [[niches/facilities-management-firms/corporate-ifm-portfolios/profile|Corporate Occupier IFM Portfolios]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An IFM account's P&L says the margin missed plan; nothing says which sites, services, delivery routes or scope decisions made it miss.
**Tags:** #causal-inference #linear-regression #feature-engineering #descriptive-statistics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to run a corporate portfolio at a margin the contract price can bear. That splits into two contests with different winners: pricing a portfolio whose real maintenance load nobody has measured before the bid closes, and deciding, service by service and region by region, what to self-deliver and what to subcontract once the account is live. Decomposed into contested sub-niches below.

## The Problem
A corporate IFM account spanning a hundred sites reports a monthly margin to the provider's regional leadership. When it misses, the account director explains it from experience: a hot summer, a subcontractor price rise, an unbudgeted project. The explanation is rarely tested, because the P&L is built from general-ledger lines and not from work orders. Labour is booked to the account rather than to the site and task, and subcontract cost arrives as invoices without the asset or the reason attached.

## Why Nobody Has Built This
Finance systems and CMMS instances were never designed to join, and on many accounts the CMMS belongs to the client. Providers treat margin analysis as a finance task done monthly in Excel. Vendors sell either the work-order system or the ERP, not the link between them.

## What to Build
A margin attribution layer that allocates every labour hour, part and subcontract invoice to the site, asset, service line and work-order type that caused it, and decomposes the month's variance against the bid into volume (more work orders than priced), mix (more emergency work), rate (wage or subcontract price changes), delivery route (subcontracted where self-delivery was priced) and scope (work done outside the contract). It ranks the variances by size and shows the tickets behind each.

## Target Customer
Account directors and regional finance leads at the large IFM providers, and the mid-size regional providers whose margins cannot absorb an unexplained miss.

## Impact If Built
Margin conversations move from anecdote to evidence, corrective action targets the actual cause, and the provider walks into renewal knowing which parts of the account make money (estimate: a margin recovery of one to two points on accounts that are currently drifting).
