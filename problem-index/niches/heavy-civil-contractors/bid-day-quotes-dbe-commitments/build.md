# Quote Levelling in the Last Two Hours

**Niche:** [[niches/heavy-civil-contractors/bid-day-quotes-dbe-commitments/profile|Bid-Day Subcontractor Quotes & DBE Commitments]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Dozens of sub and supplier quotes land in the final hours as PDFs and emails with exclusions buried in them; reading, levelling and plugging them is the most error-prone hour of the bid.
**Tags:** #large-language-models #transformers #feature-engineering #workflow-orchestration #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to close a complete set of conforming subcontractor and supplier quotes, with the owner's DBE or small-business participation documented, before the bid deadline, and whoever has the lowest conforming quote plugged on every scope when the deadline hits takes the account.

## The Problem
A quote says "excludes dewatering, bonds, testing" in small print, or covers only some of the bid items. The estimator plugs it as the low number and the job carries the gap.

## Why Nobody Has Built This
Quote formats vary by trade and region, and the window is two hours. Estimating vendors built quote grids for manual entry, and commercial-building levelling tools target GCs' trade packages, not pay-item bid schedules.

## What to Build
An inbox agent that reads each quote, maps its prices to the bid items, extracts exclusions and conditions, levels quotes per scope with the gaps priced from the estimate, checks DBE or small-business status, and fills the estimating system's quote grid for the estimator to confirm. A demo can run on public bid schedules and synthetic quotes.

## Target Customer
Chief estimators at contractors submitting ~50+ public bids a year (estimate).

## Impact If Built
If one exclusion miss a year is avoided (estimate: ~$100K–$500K each), and estimators gain an hour of review on bid day, the tool pays back on the first catch.
