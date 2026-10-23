# Notice Clocks Read From the Field Record

**Niche:** [[niches/heavy-civil-contractors/change-delay-site-condition-records/profile|Change, Delay & Differing-Site-Condition Records]]
**Industry:** [[industries/heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The events that start notice clocks are already written in foremen's diaries and RFIs; a reader that catches them the night they're written saves entitlement that late notice forfeits.
**Tags:** #large-language-models #bert #transformers #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn each field event into a notice inside the contract's clock and a time impact analysis the owner accepts, and whoever gets the most time and money granted at the change-order stage, before it becomes a claim, takes the account.

## The Problem
"Inspector stopped pile driving pending design answer", "hit rock at elevation -32, borings showed sand", "high water, crew sent home". Each is a potential notice, and each sits in a diary nobody reads until the claim.

## Why Nobody Has Built This
Field apps store diaries; nobody classifies them against the contract. Contract clauses vary by owner, and the users are project managers who already have too many tools.

## What to Build
A nightly classifier over diaries, RFIs and correspondence that tags candidate events, retrieves the governing clause and deadline, and drafts the notice for the project manager's approval. Unanswered clocks escalate. A demo can run on public contract specs and synthetic diaries.

## Target Customer
Project managers and operations VPs at heavy civil and marine contractors with ~$50M+ revenue (estimate).

## Impact If Built
If late or missing notices fall by ~80% (estimate), entitlement survives on changes that are often worth several percent of contract value (estimate).
