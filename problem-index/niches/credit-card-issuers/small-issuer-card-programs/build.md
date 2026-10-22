# Peer-Pooled Card Strategy for Small Portfolios

**Niche:** [[niches/credit-card-issuers/small-issuer-card-programs/profile|Community Bank & Credit Union Card Programmes]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A credit union with 20,000 card accounts cannot calibrate a line-increase strategy on its own losses, and nobody pools small issuers' card performance for that purpose.
**Tags:** #gradient-boosting #bayesian-inference #causal-inference #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give an issuer with a few thousand to a hundred thousand card accounts underwriting, line and rewards strategies calibrated on pooled peer-portfolio performance rather than on its own thin history, and whoever's pooled performance data is deepest takes the account — whether the institution keeps the balances or rents its brand to an agent-bank programme.

## The Problem
A small portfolio produces only a few hundred charge-offs a year (estimate), too few to tell whether a cut-off or a line-increase rule works. The institution copies the processor's default or a consultant's template and never tests it.

## Why Nobody Has Built This
Processors hold the data but treat it as client data; consortium benchmarking such as Argus serves large issuers; and small institutions have no analytics staff to use a model if they had one.

## What to Build
A consent-based pool of small issuers' card performance with hierarchical models that borrow strength across institutions, adding each institution's own relationship data (deposit balances, tenure, direct deposit) as features, and delivering ready-to-run strategies with their expected loss and revenue, plus a holdout test design the institution can operate.

## Target Customer
Credit union service organisations, bankers' banks and processors serving hundreds of small issuers.

## Impact If Built
Small issuers lend on strategies tested on comparable portfolios, using the member relationship that is their only advantage over national issuers.
