# Transaction Reconciliation Practice

**Niche:** [[niches/programmatic-ad-platforms/spend-reconciliation-and-fees/profile|Spend Reconciliation & Fees]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Financial markets reconcile every trade to the cent across counterparties daily, and advertising cannot say where a quarter of the money went.
**Tags:** #data-integration #compliance #descriptive-statistics #evaluation-metrics #workflow-orchestration #automation #hypothesis-testing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to account for the gap between what the buyer paid and what the publisher received, impression by impression — and whoever can enumerate it recovers a quarter of the money for whoever hired them.

## The Problem
Trade reconciliation in financial markets is exact, daily and non-negotiable: every transaction carries a unique reference, both sides match on it, breaks are investigated and resolved within a defined window, and the practice is supported by mature infrastructure and regulation. Advertising transacts a comparable volume of small transactions through a comparable chain of intermediaries and reconciles almost none of it, because nothing in the chain was designed to be reconciled and nobody required it to be.

## What Already Exists
Trade matching and affirmation infrastructure; unique transaction identifiers carried through the chain; break investigation and resolution workflow; transaction cost analysis measuring execution quality against benchmarks; and regulatory best execution reporting.

## The Customization Gap
The adaptation is to transactions worth fractions of a cent with no identifier and no mandate. It requires: (1) probabilistic rather than exact matching, since no transaction identifier travels the chain and introducing one requires industry coordination — statistical reconciliation on a sample is the available route and is the central methodological change; (2) reconciliation at aggregate confidence rather than per transaction, because investigating a break on a hundredth of a cent is not economic and financial practice assumes it is; (3) no regulatory compulsion, so participation must be bought with commercial leverage rather than required — which determines the whole product strategy; (4) fee structures that are spreads and undisclosed margins rather than stated commissions, which transaction cost analysis handles only when the benchmark is public and here it is not; and (5) delivery to a marketing organisation rather than a treasury function, which changes what the output must look like to be acted on.

## Target Customer
Advertiser finance and procurement, media auditors, publishers, and financial reconciliation vendors for whom advertising transactions are an unserved market.

## Impact If Solved
Financial reconciliation is exact because a transaction identifier travels the chain and a regulator requires it; advertising has neither. Probabilistic matching on a sample with aggregate confidence is the available route, and commercial leverage replaces the mandate.
