# The Gap Report Between the Drawings and the Contractor's List

**Niche:** [[niches/electrical-distributors/bid-day-project-quoting/profile|Bid-Day Project Quoting & Takeoff]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The contractor's list is the starting point of every project quote, and the veteran's value is knowing what it left out.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #object-detection #gradient-boosting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put a complete, spec-compliant, SPA-priced quote in the bidding contractor's hands before the bid closes, and whoever posts the highest hit rate on plan-and-spec quotes takes the account.

## The Problem
A contractor's estimator builds a material list for its own bid and sends it to distributors to price. The list is often short: fittings, supports, lugs, spare breakers, a transfer switch on another sheet, the fixture type changed in addendum 2. Veteran quoters catch these by reading the drawings; newer ones price the list as sent, and the omissions return as change orders or lost margin after award.

## Why Nobody Has Built This
Takeoff software was built for contractors counting devices from scratch, not for distributors checking someone else's list. The labelled data — the quoter's edits with reasons — has never been captured, because quoting happens in spreadsheets.

## What to Build
A gap engine that extracts panel schedules, one-line diagrams, fixture schedules and spec requirements from the bid package, reconciles them against the contractor's list, and flags missing, inconsistent or non-compliant lines with the sheet or paragraph as evidence. The quoter accepts or rejects each flag with a reason, and those decisions train a model of the desk's own completeness judgement. For an engineer, a two-week demo works on public bid sets from municipal plan rooms and a synthetic contractor list.

## Target Customer
Quotation managers at distributors with plan-and-spec project business.

## Impact If Built
Omissions are caught before the bid rather than after award. If missed items run ~2–5% of package value on plan-and-spec jobs (estimate), catching most of them protects that margin on every won job, and newer quoters reach veteran completeness in months rather than years.
