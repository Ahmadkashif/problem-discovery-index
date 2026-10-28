# One Record From the Shop's Request to the Part at the Bay

**Niche:** [[niches/auto-parts-distributors/shop-order-intake-fulfilment/profile|Shop Order Intake & Hot-Shot Fulfilment]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A shop order touches the phone, the catalog, the stock system, the driver and the returns desk, and no record joins them, so nobody knows whether a miss was the match or the run.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #workflow-orchestration #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn a shop's call, text or e-catalog order into the right part at the shop's bay, but that hides two contests with different winners: matching the request to the one part that fits that VIN, won by catalog depth and matching models and measured by fitment returns, and running the delivery, won by route density and dispatch and measured by shop orders cancelled because the part arrived after the shop's window. Decomposed into contested sub-niches below.

## The Problem
When a shop complains, the store cannot say whether the part was wrong (a matching failure), late (a delivery failure) or right but returned for another reason. Each system holds its slice: the call isn't recorded, the catalog shows the sale, the driver's run sits in a paper log, and the return carries a vague code.

## Why Nobody Has Built This
Order capture, catalog, stock, dispatch and returns are sold by different vendors, and no business system creates an identifier for the shop's original request.

## What to Build
A request identifier created at intake (call, text, e-catalog) and carried through match, pick, run and return, with timestamps and outcomes at each step. It reports, per shop and per store, fitment-return rate and orders cancelled for late arrival separately, which is what the two sub-niches compete on, and it gives the matching model and the dispatcher their labels.

## Target Customer
Commercial operations leaders at chains and warehouse distributors; business-system vendors that could carry the identifier.

## Impact If Built
If a store could attribute each of its ~5–10 daily shop complaints (estimate) to match or run, it could fix the larger cause first; a 25% cut in repeat complaints on a $3M commercial book protects shops worth ~$100K+ a year (estimate).
