# Post-Cancellation Demand From Libraries That Already Cancelled

**Niche:** [[niches/libraries-and-archives/e-resource-renewal-analytics/profile|E-Resource Renewal & Usage Analytics]]
**Industry:** [[industries/libraries-and-archives|Libraries & Archives]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A library deciding whether to cancel a package guesses its cost from downloads, while dozens of peers have already cancelled and observed what readers actually requested afterwards.
**Tags:** #causal-inference #linear-regression #time-series-forecasting #confidence-intervals #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to hand an academic library a renew, cancel or renegotiate number for each package — usage, open-access substitution and post-cancellation demand joined — before the publisher's renewal deadline, and whoever's number the provost and the consortium both accept takes the analytics budget.

## The Problem
Downloads overstate need: many are casual, some are robots, and many articles are freely available elsewhere. The true cost of cancellation is the interlibrary loan, document delivery and lost reading that follow, which a library sees only after it cancels.

## Why Nobody Has Built This
Each library's cancellation history is small and private, publishers discourage sharing, and price data is often under confidentiality clauses. Single-library tools model scenarios from that library's own downloads.

## What to Build
A pooled, consortium-hosted model trained on member libraries that cancelled packages or titles: their pre-cancellation COUNTER usage, open-access availability and faculty profile, and their post-cancellation request and delivery data. For any library's renewal it estimates post-cancellation requests and cost per title, with a confidence range, and shows the analogous cancellations it rests on. Prices stay local; only usage and outcomes are pooled.

## Target Customer
Consortium licensing directors and collections heads at research and mid-size universities.

## Impact If Built
Renewal decisions made on observed consequences rather than download counts, and a stronger negotiating position for the consortium.
