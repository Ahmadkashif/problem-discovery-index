# Replacement Value Comparison Read From Any Carrier's Statement

**Niche:** [[niches/life-insurance-carriers/annuity-suitability-review/profile|Annuity Suitability & Best-Interest Review]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The riskiest annuity sales are replacements, and judging one requires reading the old contract's statement, which comes in a different format from every carrier.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to clear each annuity sale's best-interest review before issue with a record a market conduct examiner accepts, and whoever auto-clears the most files without missing an escalation a senior reviewer would have caught takes the account.

## The Problem
When a client surrenders one annuity to buy another, the reviewer must judge what is given up: surrender charges, a living-benefit rider's accumulated value, death benefit step-ups, guaranteed minimum rates. The producer's comparison form summarises this, sometimes wrongly. The truth is in the old contract's statement and rider terms.

## Why Nobody Has Built This
Statement formats vary by carrier, product and year, and rider mechanics are complex. Rules engines can only check what the producer typed.

## What to Build
A reader that extracts account value, surrender charge schedule, rider bases and guarantees from any carrier's statement. It computes the value surrendered and the break-even of the new contract under stated assumptions, compares that with the producer's comparison form, and flags discrepancies for the reviewer with the source page highlighted.

## Target Customer
Annuity new-business and suitability leaders at FIA, RILA and fixed annuity writers with high replacement volume.

## Impact If Built
Replacement reviews in minutes with an evidenced comparison, and the most harmful replacements caught before issue.
