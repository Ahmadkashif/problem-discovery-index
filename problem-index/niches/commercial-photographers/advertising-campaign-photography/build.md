# Usage Pricing From Won and Lost Bids

**Niche:** [[niches/commercial-photographers/advertising-campaign-photography/profile|Advertising & Campaign Photography]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every production company keeps years of estimates and award decisions, and none of them can say what national out-of-home for two years actually closes at in their own book.
**Tags:** #gradient-boosting #confidence-intervals #feature-engineering #large-language-models #evaluation-metrics #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to win the agency's bid with a treatment and an estimate whose usage terms the art buyer can defend to the client's procurement team and cost consultant, and whoever prices usage most defensibly takes the account.

## The Problem
A producer pricing usage on a triple bid works from memory, a published calculator and the last similar job. They do not know their own win rate at a given usage fee, how often the cost consultant cut usage and by how much, or which categories (beverage, automotive, pharma) carry an exclusivity premium that clients actually accept. Lost bids are rarely recorded with the reason, so the history that would answer these questions disappears.

## Why Nobody Has Built This
Each production company or rep agency handles a few hundred bids a year, too few to model alone, and none will share raw estimates with a competitor. Estimates are PDFs and spreadsheets with free-text usage lines, so pooling them first needs a common structure for licence terms. Estimating tool vendors sell desktop software, not data.

## What to Build
A service that parses estimates into structured usage terms (media, placements, territory, duration, exclusivity, image count, options) and joins them to outcomes: won, lost on price, lost on creative, cancelled, and the final negotiated fee. Each participating firm gets quantile ranges and win probabilities for a new brief from its own history. Firms that contribute get pooled, anonymised category benchmarks on top. The output is a range and a rationale the producer can put in front of an art buyer.

## Target Customer
Executive producers at photo production companies, photographers' reps and agencies representing rosters, and advertising photographers billing several hundred thousand dollars a year.

## Impact If Built
Producers price usage from evidence rather than instinct, stop discounting usage by reflex in triple bids, and recover an estimated several points of fee on every awarded job.
