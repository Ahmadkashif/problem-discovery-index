# A Ticket Audit Model Before the Invoice

**Niche:** [[niches/landfill-operators/scale-house-ticketing-fees/profile|Scale-House Ticketing, Tonnage & Fee Reporting]]
**Industry:** [[industries/landfill-operators|Landfill Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Wrong material codes, rates and fees are found weeks later in a customer dispute or a host-community audit; a model reading every ticket before invoicing would catch most of them the same day.
**Tags:** #gradient-boosting #k-nearest-neighbors #feature-engineering #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every load across the scale into a ticket that bills, reports and pays fees correctly the first time, and whoever has the smallest share of tickets corrected after invoicing takes the account.

## The Problem
Attendants choose material codes and rates under pressure, and rules change: new contracts, new surcharges, expired special-waste approvals. Finance finds errors through complaints and audits.

## Why Nobody Has Built This
Scale software validates fields, not plausibility; each site's rate and fee rules are idiosyncratic; and nobody has labelled historical corrections.

## What to Build
A model trained on each site's tickets and past credit memos that scores every new ticket for likely error — material code unusual for the customer or vehicle, net weight implausible for the vehicle, rate not matching the contract, missing or expired approval, host fee or surcharge not applied — and routes the riskiest to a supervisor before the invoice run.

## Target Customer
Controllers and business managers at landfills and multi-site disposal networks.

## Impact If Built
If ~2% of tickets are corrected after invoicing (estimate) and the model catches three-quarters of them first, a site issuing 150,000 tickets a year avoids ~2,250 credit memos and the disputes behind them.
