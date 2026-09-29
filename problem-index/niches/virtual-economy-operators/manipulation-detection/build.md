# Finding the Manufactured Trade

**Niche:** [[niches/virtual-economy-operators/manipulation-detection/profile|Manipulation Detection]]
**Industry:** [[industries/virtual-economy-operators|Virtual Economy Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every trade is recorded and nothing asks whether any of them were real.
**Tags:** #graph-theory #graph-neural-networks #change-point-detection #k-means-clustering #evaluation-metrics #confidence-intervals #hypothesis-testing #spectral-graph-theory
**Contested on:** Every serious competitor in this niche is fighting to tell a genuine trade from a manufactured one across accounts that are pseudonymous and plentiful — and whoever builds that surveillance takes the account.

## The Problem
Distinguishing a genuine trade from a manufactured one is the core surveillance question and nothing in these platforms attempts it. Accounts are cheap and pseudonymous, so a single actor can operate many; collusion between apparently unrelated accounts is trivial; and the resulting volume and prices then mislead everyone else. The evidence is entirely present in the trade graph — who traded with whom, when, at what price, with what net effect — and nobody constructs the graph.

## Why Nobody Has Built This
Trust and safety teams are organised around account abuse rather than market conduct. Graph analysis at this scale is real engineering with no revenue attached. The manufactured volume inflates the marketplace's reported activity. And nobody has been asked for it.

## What to Build
Build the trade graph and look for the shapes manipulation makes. Construct the account-item trade graph and detect the structural signatures — cycles, tight bipartite clusters, repeated counterparty pairs with no net position change — which is the core and is where manipulation is visible and individual trades are not. Link accounts by device, payment instrument, timing and behavioural signals, since account-level analysis alone is defeated by anyone with two accounts. Detect price ramping as a sequence rather than as a price level, because the pattern is the sequence of trades that built it. Identify cornering of limited supply from concentration statistics at issuance, which is measurable within hours of a release. Score confidence explicitly, as banning someone from goods they paid for demands a high evidentiary bar. Exclude detected manipulation from published price data, which is the most direct way the harm reaches other participants. Backtest detectors against known cases before deploying, since false positives are expensive in both trust and support load. Provide analysts with the graph and the evidence rather than a score alone. Run continuously rather than in periodic sweeps, because the value is in intervening during the pattern. And offer it as a service to third-party marketplaces trading the same items, where much of the activity settles.

## Target Customer
Virtual economy operators, third-party trading marketplaces, market operations teams, and surveillance technology vendors.

## Impact If Built
Manipulation is visible in the trade graph and invisible in individual trades, and nobody constructs the graph. Structural detection plus account linkage is what separates a manufactured market from a real one.
