# A Statement Checker That Knows the Contract

**Niche:** [[niches/film-distributors/the-licensor-producer/profile|The Licensor Producer]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A producer receives a quarterly statement and has no practical way to test it against the distribution agreement's fee, expense cap and cross-collateralisation terms short of a five-figure audit.
**Tags:** #large-language-models #transformers #gaussian-mixture-models #feature-engineering #evaluation-metrics #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to give producers a distribution statement they can verify line by line against the receipts behind it, and whoever is most verifiably transparent wins the next film from the filmmakers who were burned last time.

## The Problem
The agreement says the distributor takes, say, a 30% fee on theatrical and 25% on digital, recoups expenses capped at a figure, may not cross-collateralise across territories, and must account quarterly. The statement shows totals by category. The producer can't tell whether the fee was applied to the right base, whether the cap was respected, or whether market costs were charged to their film and four others at once.

## Why Nobody Has Built This
Producers are a fragmented, cash-poor market. Agreements are bespoke and statements vary by distributor. Until language models could read both, every check required an accountant.

## What to Build
A tool that reads the producer's distribution agreement and every statement received, then recomputes what each statement should show given the reported receipts. It flags fee-base errors, cap breaches, prohibited cross-collateralisation, late statements, and expense lines outside the normal range for that distributor and window. It drafts a query letter citing the contract clause, and keeps the statement history so a later audit starts from evidence.

## Target Customer
Independent producers and production companies with titles in distribution; entertainment lawyers and accountants who serve them at volume.

## Impact If Built
Producers get a first-pass check for the cost of software rather than an audit. Distributors that account cleanly can point to it when bidding for the next film.
