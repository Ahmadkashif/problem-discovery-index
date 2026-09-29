# Transaction Monitoring for a Public Ledger

**Niche:** [[niches/crypto-exchanges/deposit-screening/profile|Deposit Screening]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bank transaction monitoring assumes a private ledger, a named counterparty and a decision that can wait, and the crypto deposit has none of those.
**Tags:** #compliance #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to decide correctly whether arriving funds are criminal proceeds — and the contest splits cleanly enough that it is not terminal.

## The Problem
Bank transaction monitoring is a mature discipline with scenario libraries, tuning methodologies, model validation standards, alert quality measurement and regulatory expectations for all of it. Exchanges face the same obligation with an inverted information structure: the counterparty is an address rather than a named institution, the ledger is public and complete rather than private and partial, and the relevant history extends backwards through arbitrary hops.

## What Already Exists
Scenario-based monitoring platforms; model risk management and tuning methodologies with documented threshold rationale; alert quality and above-the-line and below-the-line testing; suspicious activity reporting workflow; and the supervisory expectations that shaped all of it.

## The Customization Gap
The adaptation is to complete public history and unnamed counterparties. It requires: (1) transitive risk through the ledger rather than a counterparty risk rating, since the whole question is how far taint propagates and banking has no analogue for it — this is the substantive adaptation; (2) threshold tuning without outcome labels, where banking's below-the-line testing assumes a reviewable sample with knowable answers; (3) attribution purchased from a vendor rather than known from a relationship, which puts the primary input outside model validation; (4) a decision made at deposit time on a customer who is already waiting, rather than in a batch reviewed later; and (5) a public ledger that makes the exchange's own history auditable by anyone, which cuts both ways.

## Target Customer
Exchange compliance leadership, model risk functions applying bank standards to purchased scores, and monitoring vendors whose crypto modules wrap a third-party feed.

## Impact If Solved
Banking's tuning discipline assumes labels its testing can reach. Adapting threshold rationale and validation to a control whose ground truth returns on a fraction of a percent of cases is the real work and would transfer well beyond crypto.
