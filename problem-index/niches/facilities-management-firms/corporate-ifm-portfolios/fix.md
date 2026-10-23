# Out-of-Scope Work Done Inside the Fixed Price

**Niche:** [[niches/facilities-management-firms/corporate-ifm-portfolios/profile|Corporate Occupier IFM Portfolios]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A request arrives, a technician does it, and nobody checks whether the contract's scope matrix says the client should have paid extra.
**Tags:** #large-language-models #bert #workflow-orchestration #automation #quick-win #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to run a corporate portfolio at a margin the contract price can bear. That splits into two contests with different winners: pricing a portfolio whose real maintenance load nobody has measured before the bid closes, and deciding, service by service and region by region, what to self-deliver and what to subcontract once the account is live. Decomposed into contested sub-niches below.

## The Problem
Every IFM contract has a responsibility matrix: what is in the fixed price, what is billable above it, and what is the client's own responsibility (tenant fit-out, furniture moves, events, equipment above a cost threshold). Requests arrive at the service desk without that context, and site teams keep the client happy by doing the work. Months later the account is over budget, and the out-of-scope work cannot be billed retrospectively.

## Why It's Still Broken
The matrix lives in a contract appendix written by the bid team and read by nobody at the service desk. Raising a billable quote feels like friction with a client the site team sees every day, and nothing in the work-order flow prompts the question.

## What a Fix Looks Like
Encode each account's responsibility matrix and check every new work order against it at intake: in scope, billable with a quote, or the client's responsibility. Billable items route to a one-click quote for client approval, and the site manager sees the monthly total of out-of-scope work done free, so giving work away becomes a decision rather than a habit.

## Who Feels the Pain
Account directors explaining margin misses, site facility managers caught between the client and their own finance team, and the provider's bid team, whose priced scope was never enforced.

## Impact If Fixed
Recovering even a small share of untracked out-of-scope work restores margin on accounts that look underpriced but are really under-enforced (estimate: a few percent of contract value on loosely governed accounts).
