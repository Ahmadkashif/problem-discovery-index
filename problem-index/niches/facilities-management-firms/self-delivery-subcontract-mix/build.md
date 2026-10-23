# A Make-or-Buy Model per Service Line and Metro

**Niche:** [[niches/facilities-management-firms/self-delivery-subcontract-mix/profile|Self-Delivery vs Subcontract Delivery Mix]]
**Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Providers decide what to self-deliver by habit and account boundaries when the economics depend on density across every account in a metro.
**Tags:** #optimization-fundamentals #linear-regression #monte-carlo-methods #feature-engineering #graph-theory #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide, service by service and region by region, whether its own technicians or a subcontractor will do the work more cheaply at the contracted SLA, and whoever builds enough self-delivery density to keep margin off the pass-through line takes the account.

## The Problem
An account team subcontracts HVAC repairs in a region because it has no HVAC technician there, while another account team at the same provider employs three HVAC technicians twenty miles away who are half-utilised. Neither team sees the other's demand. Decisions to hire, to subcontract or to move a technician are made per account at contract start and rarely revisited.

## Why Nobody Has Built This
The data needed (work orders, technician time, travel, subcontract invoices) sits across separate systems and separate account P&Ls, and the organisation is built around accounts, not metros. Field-service optimisation vendors schedule the technicians a firm already has; they do not answer whether it should have them.

## What to Build
A cost-to-serve model for self-delivered work by trade and metro (labour, travel, utilisation, overtime) and a matching model of subcontract cost from invoice history, feeding an optimisation that recommends the delivery mix across all accounts in a metro under SLA constraints, together with the volume at which hiring one more technician pays. It runs as a quarterly review and as a check whenever a new account is won in the metro.

## Target Customer
Heads of technical services and regional operations at IFM providers with overlapping account footprints.

## Impact If Built
Margin moves from subcontractor markup to the provider's own labour where density supports it, and new bids in a metro can be priced on the density the provider already has (estimate: one to three margin points on affected service lines).
