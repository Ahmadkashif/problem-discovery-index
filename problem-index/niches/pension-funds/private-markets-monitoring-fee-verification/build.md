# Fee and Carry Recomputed From the LPA Every Quarter

**Niche:** [[niches/pension-funds/private-markets-monitoring-fee-verification/profile|Private Markets Monitoring & Fee Verification]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every plan receives fee and carry figures from its GPs and almost none recompute them from the partnership agreement that governs them.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #compliance #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to turn every GP statement, notice and partnership agreement into a record of NAV, cash flows, fees and carry that reconciles to the custodian and to the LPA's own terms, and whoever closes each quarter with the fewest unexplained differences before the board's review takes the account.

## The Problem
Management fee step-downs after the investment period, offsets of transaction and monitoring fees, caps on organisational expenses, hurdles, catch-ups, clawbacks and most-favoured-nation elections all live in the LPA and side letters. Each quarter's capital account statement applies them, and the plan has no independent number to compare against. An overcharge is found, if at all, when an analyst happens to check a fund by hand.

## Why Nobody Has Built This
Monitoring platforms are built to aggregate many LPs' documents and report performance; recomputation per fund requires executing each fund's bespoke terms. LP operations teams are small, and the legal language is long and varied. Until language models could draft term schemas, the setup cost per fund was prohibitive.

## What to Build
A term engine that reads each LPA, amendment and side letter once and drafts an executable fee-and-waterfall schema for a specialist to approve. It then recomputes every quarter's fees, offsets, expenses and carry from the statement and classifies each difference (timing, basis, offset, expense category, carry) with a citation to the clause. Output feeds the 7514.7 report and ILPA template comparisons directly.

## Target Customer
Investment operations heads at public plans with 100+ fund interests; consultants preparing fee reports for smaller plans.

## Impact If Built
Overcharges are raised within a quarter while the GP relationship is active, and the plan publishes recomputed numbers rather than reported ones. One analyst covers a programme that today needs a team.
