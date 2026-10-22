# Holdout-Calibrated Matchback

**Niche:** [[niches/direct-mail-agencies/response-matchback-reporting/profile|Response Matchback & Campaign Reporting]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Matchback credits mail with every mailed buyer, including those who would have bought anyway, and nobody corrects the credit by the amount holdouts show it overstates.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #bayesian-inference #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to credit each response to the right list, segment and version within the client's planning cycle, in numbers the client's finance team and the list owners both accept — and whoever delivers a reproducible matchback before the next circulation plan takes the account.

## The Problem
For house-file segments of active customers, most matched buyers would have purchased without the mailing; for cold prospects, few would. Matchback treats both the same, so house-file mail looks more profitable than it is and prospecting looks less. Clients that have run holdouts know the gap is large and varies by segment; most have never run one.

## Why Nobody Has Built This
Holdouts are sporadic and owned by individual clients, so no agency has assembled enough of them to estimate correction factors by segment type. Reporting matchback-only credit is also commercially comfortable.

## What to Build
A reporting engine that runs standard matchback and, alongside it, an incrementality estimate for each cell: measured directly where the cell has a holdout, and otherwise inferred from a hierarchical model of matchback-to-incrementality ratios fitted across all holdouts the agency's clients have allowed, by segment type (active, lapsed, prospect), offer and season. Each report shows both numbers and the uncertainty.

## Target Customer
Agency analytics directors and mailer circulation directors with enough campaigns to run a few holdouts a year.

## Impact If Built
Circulation decisions move from credited response to caused response, which typically cuts house-file over-mailing and protects prospecting budgets that matchback undervalues.
