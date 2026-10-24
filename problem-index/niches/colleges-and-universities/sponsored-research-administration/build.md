# Policy-Change Impact Across the Award Portfolio

**Niche:** [[niches/colleges-and-universities/sponsored-research-administration/profile|Sponsored Research Administration & Cost Recovery]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When an agency changes a cap, a term or a certification, a research university needs to know within a day which of its thousands of awards are affected and what it will cost; today it takes weeks of re-reading.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to recover the full allowable cost of each federal research award as agency rules, caps and terminations change, and whoever leaves the least allowable cost unrecovered takes the account.

## The Problem
A research university holds several thousand active awards, each with its own notice, amendments, agency terms and F&A arrangement. When NIH announced its indirect-cost cap, or when agencies issued termination waves and new certifications, post-award offices had to find affected awards by searching PDFs and spreadsheets, estimate recovery lost, and tell departments what to stop spending. Errors either way cost money: spending after a stop date is disallowed, while stopping allowable work early forfeits recovery.

## Why Nobody Has Built This
Award documents vary by agency and decade, and the suites store them as attachments. Vendors built for steady-state workflow, not for re-reading a portfolio against a new rule, and the volume of policy change before 2025 did not justify it.

## What to Build
A parser that turns each notice of award and amendment into structured terms; a classifier that maps each agency announcement to the clauses it modifies; and a portfolio impact report listing affected awards, cost categories at risk, F&A recovery lost and required actions, with a dated audit trail. Public NIH RePORTER, NSF award search and USAspending data support a prototype before any university data is used.

## Target Customer
Sponsored programs directors at the ~150 research-intensive universities that carry most federal research spending (estimate).

## Impact If Built
Policy events assessed in a day rather than three weeks. Billing allowable closeout costs on terminated awards that would otherwise be missed recovers ~1–3% of their remaining budget (estimate).
