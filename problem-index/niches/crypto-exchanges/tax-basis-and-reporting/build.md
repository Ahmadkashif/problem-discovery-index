# Basis From Provenance

**Niche:** [[niches/crypto-exchanges/tax-basis-and-reporting/profile|Tax Basis & Reporting]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The asset's entire history is on a public ledger and the exchange reports its gain as though it appeared from nowhere.
**Tags:** #graph-theory #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #time-series-forecasting #data-integration #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to establish a defensible cost basis for assets that arrived from somewhere else with nothing attached — and whoever reconstructs basis most accurately files the fewest wrong forms under a regime that now makes it a legal obligation.

## The Problem
A deposit arrives. The exchange knows the address it came from, the time it arrived, the amount, and — on a public ledger — the entire history of that address and its predecessors. What it does not know is what the customer paid, and it reports as though the information does not exist. The chain shows when those coins were last acquired, from what kind of counterparty, and at what market price on that date. For a large share of deposits the basis is approximately recoverable and nobody has tried.

## Why Nobody Has Built This
Basis was the customer's problem until the reporting regime changed, so the exchange never built for it and the obligation arrived faster than the capability. Inference produces an estimate, and tax filing culture prefers a documented number to a good one. The chain analysis required overlaps with compliance tooling that sits in a different department. And zero basis is the safe default for the exchange even though it is wrong for the customer.

## What to Build
Infer basis and score the inference. Trace the deposit's on-chain provenance to its last plausible acquisition event, which is the core and is the same graph capability compliance already runs for other reasons. Classify the acquisition type — purchase on another venue, mining or staking reward, airdrop, self-transfer, gift — since the type determines the basis rule and is often inferable from the counterparty's shape. Value at the market price for the identified date and asset, which is straightforward once the date is established. Match self-transfers where both ends are the exchange's own customers, as that case has exact basis available and is currently treated like any other inflow. Score every basis estimate for confidence, because a defensible filing requires knowing which numbers are solid and which are inferences. Structure customer attestation and reconcile it against the inference, so the two sources check each other rather than one being ignored. Flag the cases where inference and attestation disagree materially, since those are the filings most likely to be wrong. Support the transfer statement regime between brokers, which is the intended mechanism and currently works poorly. Retain the reasoning behind each basis figure, as the customer and the authority may both ask. And measure basis coverage and estimated accuracy, which is the number that shows the obligation being met.

## Target Customer
Exchange tax and product leadership, customers facing a gain computed from zero, tax authorities receiving forms of unknown quality, and crypto tax software vendors working from exports rather than from the chain.

## Impact If Built
Basis was the customer's problem until the regime changed, and the obligation arrived faster than the capability. The provenance needed to reconstruct it is public and the graph tooling already exists inside the exchange for compliance.
