# Claims Filed From the Agreement, Not the Spreadsheet

**Niche:** [[niches/industrial-distributors/rebates-and-spa-claims/profile|Supplier Rebates & SPA Claims]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every SPA arrives as a document with its own part list, dates and rules, and the claim is only as good as the person who keyed it.
**Tags:** #large-language-models #transformers #gradient-boosting #feature-engineering #compliance #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to file every claim the distributor has earned under each manufacturer's agreement terms before the claim window closes, and whoever recovers the most claim dollars at the lowest denial rate takes the account.

## The Problem
A mid-size distributor may hold hundreds of active SPAs across bearing, power transmission and fluid power manufacturers (estimate), each with part lists in the manufacturer's numbering, end-customer conditions, quantity caps and expiry dates. Terms are keyed into the ERP by hand; claims are built monthly from sales exports. Errors at keying become denials at claiming.

## Why Nobody Has Built This
Rebate software grew up on the manufacturer side, where programme design and accrual are the problem. Distributor claim desks are small, and each manufacturer's format is different, so no vendor saw enough volume to automate extraction until document AI became cheap.

## What to Build
A claim engine that reads each agreement as it arrives, extracts terms into a structured record, resolves part numbers to the distributor's SKUs and approved equivalents, and keeps the ERP contract table in sync. Monthly, it matches invoice lines to agreements, runs each manufacturer's denial rules, scores denial risk from past responses, and prepares claim files in each manufacturer's format, ready for submission or filed by an agent through the portal.

## Target Customer
CFOs and controllers at industrial distributors with roughly $50M–$2B in sales (estimate) and dozens of manufacturer agreements.

## Impact If Built
Recovering an extra ~5–10% of earned claim dollars (estimate) drops straight to net profit, and denials fall because claims are checked before they're filed.
