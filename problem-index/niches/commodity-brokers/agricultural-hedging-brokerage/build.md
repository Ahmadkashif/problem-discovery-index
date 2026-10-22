# One Position per Hedger Across Futures, Cash and Insurance

**Niche:** [[niches/commodity-brokers/agricultural-hedging-brokerage/profile|Agricultural Hedging Brokerage]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No one in agricultural hedging, whether broker, FCM, elevator or lender, can see a hedger's whole position, so hedges are sized and margin is financed on partial information.
**Tags:** #large-language-models #feature-engineering #monte-carlo-methods #data-integration #worker-facing #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every competitor is fighting to keep an agricultural hedger hedged through a price spike". But for a farmer the contest is advice and a margin plan that the farmer and the farmer's lender trust, won by brokers with farm relationships. For elevators, feed mills and processors it is clearing a large hedge book against cash-contract positions and financing its margin calls at scale, won by FCMs with balance sheets and grain-system integration. Decomposed into contested sub-niches below.

## The Problem
A farmer's price risk is spread across a futures account at one FCM, cash contracts at two elevators (forward, basis, hedge-to-arrive, minimum price), a crop insurance revenue policy, and sometimes LRP endorsements on cattle. An elevator's risk is its cash-contract book against its own futures. Each party sees its own slice. The broker advising a hedge and the FCM financing its margin calls work from what the client remembers to mention.

## Why Nobody Has Built This
Each slice lives in a different system owned by a different business, under different confidentiality expectations, and the farmer is the only party entitled to all of it but has no software. FCMs build for clearing and elevators build for grain accounting.

## What to Build
A client-permissioned position service that pulls futures and options from the clearing FCM, reads elevator contract confirmations and insurance summaries the client forwards (photos, PDFs, portal exports), and presents one position in bushels and head. It shows hedge ratio against expected production, margin-call exposure under price scenarios, and contract deadlines. Brokers use it to advise, and FCMs use the hedge evidence when deciding whether to extend a margin call.

## Target Customer
Heads of agricultural brokerage at FCMs and principals of ag introducing brokers, with farmers and elevator managers as the permissioning users.

## Impact If Built
Hedges sized to real exposure and margin credit extended on evidence. In a rally like spring 2022, fewer hedgers get forced out of positions that their crops were already covering.
