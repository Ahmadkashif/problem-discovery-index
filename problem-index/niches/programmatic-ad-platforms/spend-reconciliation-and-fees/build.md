# A Quarter of the Money Is Unaccounted For

**Niche:** [[niches/programmatic-ad-platforms/spend-reconciliation-and-fees/profile|Spend Reconciliation & Fees]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The reconciliation between what a buyer paid and what a publisher received routinely loses a quarter of the money to fees nobody can enumerate.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #compliance #revenue-impact #workflow-orchestration #automation #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to account for the gap between what the buyer paid and what the publisher received, impression by impression — and whoever can enumerate it recovers a quarter of the money for whoever hired them.

## The Problem
An advertiser pays a million dollars. Publishers receive something closer to seven hundred and fifty thousand. The difference is fees: demand-side platform, exchange, supply-side platform, data, verification, agency, and several taken at layers that issue no invoice to anyone the buyer can see. When a large industry study attempted this reconciliation across many advertisers, a substantial share of spend could not be traced at all — not shown to be improper, simply untraceable. The money moved through systems that each recorded their own portion and none recorded the chain, and that remains the normal condition of a market transacting hundreds of billions a year.

## Why Nobody Has Built This
Every intermediary earns from the layer the buyer cannot see, so none supplies the data needed to see it — this is a straightforward alignment problem and it is why fifteen years of complaint have changed little. Log-level data is contractually restricted and technically incompatible across platforms. Joining buy-side and sell-side records impression by impression requires an identifier neither side is obliged to carry. And the buyer's own team often earns a percentage of the same spend.

## What to Build
Reconstruct the transaction chain end to end. Join buy-side and sell-side records at the impression level using whatever identifiers exist, accepting statistical matching where exact joins fail, which is the core and is achievable on a sample even where full coverage is refused. Enumerate every fee by layer, with the amount and the party, which is the deliverable and the thing no participant currently produces. Quantify the unaccounted portion explicitly rather than absorbing it, since naming an untraceable share is what creates the commercial pressure — a gap with a number attached is negotiable and a vague sense of leakage is not. Detect fees taken as a spread rather than a disclosed rate, which is where the least visible margin sits and which only a two-sided join reveals. Run continuously rather than as an annual audit, because a retrospective finding changes nothing about the spend already placed. Compare paths to the same inventory on net cost to the publisher, which connects to the supply path work and is the actionable output. Give publishers their side of the reconciliation, since they are equally blind and are a natural ally in obtaining the data. Produce evidence usable in commercial renegotiation, which is what the analysis is actually for. Push conclusions into bidding so expensive paths are avoided automatically. And publish an industry-standard reconciliation method, because a bespoke analysis per advertiser is contestable and a standard one is not.

## Target Customer
Advertiser finance and procurement, agency clients seeking transparency, publishers blind to their own revenue chain, and the auditors currently doing this by hand.

## Impact If Built
A documented share of spend is not improper but simply untraceable, because every system recorded its own portion and none recorded the chain. An impression-level two-sided join with the unaccounted share named as a number turns a vague sense of leakage into a negotiable figure.
