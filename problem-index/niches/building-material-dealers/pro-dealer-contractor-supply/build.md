# The Job Ledger That Grades Every Package

**Niche:** [[niches/building-material-dealers/pro-dealer-contractor-supply/profile|Pro Dealer Supply to Builders & Remodelers]]
**Industry:** [[industries/building-material-dealers|Building Material Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every job's original package, add-ons, returns and back-charges already sit in the dealer's ERP; nobody has joined them into a per-job, per-builder, per-estimator record of what was quoted versus what was consumed.
**Tags:** #tacit-knowledge-ml #gradient-boosting #causal-inference #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to be the builder's and remodeler's lumber and components supplier," but before award that fight is the fastest complete priced package from a plan set, won by estimating desks and takeoff tools, and after award it is every start delivered complete on the builder's schedule at the agreed price, won by scale, component capacity and logistics. Decomposed into contested sub-niches below.

## The Problem
A pro dealer knows its sales by builder and its margin by branch. It does not know how far each job's consumption drifted from its quote, why, or whose takeoff drifted most. Add-on orders and returns are booked as separate tickets; back-charges are negotiated by the outside salesperson and credited without a cause code.

## Why Nobody Has Built This
ERPs are built around tickets, not jobs, and job names are typed inconsistently across orders. Takeoff tools stop at the quote. The value only appears when the two are joined, and neither vendor owns both.

## What to Build
A job ledger that reconstructs each job from ERP tickets (fuzzy matching on job names, addresses and builder accounts), attaches the takeoff and any plan revisions, and computes per category: quoted, delivered, returned, added and back-charged. On top, a simple attribution — takeoff gap, plan change, site waste — confirmed by the estimator in a weekly review. For an engineer, a two-week demo works on a synthetic ERP export with deliberately messy job names.

## Target Customer
Operations and estimating managers at pro dealers with ~$50M+ of builder sales; rollup integration teams comparing acquired yards.

## Impact If Built
If add-ons and returns run ~5–15% of package value (estimate), a ledger that shows which part was avoidable is worth ~1–2 margin points on builder sales at a dealer that acts on it (estimate), and it produces the labels every takeoff model needs.
