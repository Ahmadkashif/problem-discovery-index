# The Request-to-Part Ledger Captured at the Counter

**Niche:** [[niches/plumbing-and-hvac-distributors/hvac-parts-counter-will-call/profile|HVAC Repair Parts Counter & Will-Call]]
**Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every counter sale answers a question nobody writes down, so the branch can't learn which identifications were right or teach the next hire.
**Tags:** #tacit-knowledge-ml #cnns #contrastive-learning #k-nearest-neighbors #large-language-models #worker-facing #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to hand a service technician the right replacement part — OEM or approved universal — from a model and serial number, a nameplate photo or a description while the homeowner waits, and whoever sends the most technicians back to the job with the right part on the first trip takes the account.

## The Problem
A technician asks for "the blower motor for a 2013 Goodman, the one with the module on it." The veteran knows it's a variable-speed ECM, knows the replacement programming, and sells a universal with the right adapter. The ERP records a motor sold. If it comes back, the return is recorded without the reason.

## Why Nobody Has Built This
Point-of-sale systems record SKUs, not requests; parts databases record catalogues, not what technicians ask for; and returns are coded loosely.

## What to Build
A counter screen and text inbox that store each request as it arrived (words, model and serial, photo), the candidate parts shown, the part sold and any return within thirty days, then use that ledger to rank candidates for the next request with the branch's own history. A two-week demo works on public parts lists and synthetic requests.

## Target Customer
HVAC and refrigeration distributors with high counter volume and retiring counter veterans.

## Impact If Built
If ~5–10% of counter repair-part sales come back as wrong parts (estimate), the ledger cuts that and turns a veteran's identification habits into a training set, so a new hire is useful in months instead of years.
