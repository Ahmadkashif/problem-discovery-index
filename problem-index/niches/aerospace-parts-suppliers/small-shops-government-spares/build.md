# An Eligibility-First Screen for Every Solicitation

**Niche:** [[niches/aerospace-parts-suppliers/small-shops-government-spares/profile|Small Shops Bidding Government Spare Parts]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Bid tools find solicitations; the small shop's real bottleneck is deciding, item by item, whether it is even allowed and able to make the part.
**Tags:** #large-language-models #transformers #logistic-regression #feature-engineering #revenue-impact #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to put a small AS9100 shop's quotes on the government solicitations it can actually win, and whoever lifts the shop's awards per quote submitted takes the account.

## The Problem
An owner scanning DIBBS each morning sees dozens of items in the shop's supply classes. For each, the answer usually turns on things buried in the solicitation and the technical data: is it restricted to approved sources, is the shop one of them, is the drawing package available and readable, does the item need a first article test, does it fall under specialty-metals rules, is the quantity worth the setup. Most items fail one of these, and finding out takes the morning.

## Why Nobody Has Built This
Government contracting software targets large pursuits; DIBBS items are small and many; and the eligibility logic spans solicitation clauses, procurement history and technical data that each tool reads only partly.

## What to Build
A screen that reads every new solicitation in the shop's classes, extracts the restrictions and clauses, checks the shop's approved-source status and data access, reads the technical data package for material, special processes and characteristic count, and returns a short list of items the shop can bid, each with the blocking reasons for the rest and an estimated price band from award history. Items worth a source approval request are flagged with the evidence the request will need.

## Target Customer
Owners and contracts managers at 10-to-100-person AS9100 shops and spares distributors.

## Impact If Built
Turning a morning of triage into a 15-minute review could let a shop quote two to three times more eligible items (estimate) and stop spending estimator time on items it cannot win.
