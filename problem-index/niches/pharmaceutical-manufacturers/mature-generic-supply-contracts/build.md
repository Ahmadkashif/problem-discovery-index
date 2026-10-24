# Exit Decisions Priced Before the Shortage

**Niche:** [[niches/pharmaceutical-manufacturers/mature-generic-supply-contracts/profile|Mature Generic Supply & Shortage Exposure]]
**Industry:** [[industries/pharmaceutical-manufacturers|Pharmaceutical Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Generic makers exit low-margin molecules when a quality or sourcing cost lands, not on a plan, and the exit becomes a shortage because nobody saw it coming.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #confidence-intervals #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep shipping a wholesaler's or GPO's awarded generic at an eroded price, and whoever ships the highest share of awarded volume in full takes the account.

## The Problem
A mature molecule earns a few cents a unit. Then a cost arrives: a nitrosamine reformulation, a second API source to qualify, a remediation after a 483, a tariff review. The maker decides whether to absorb it or exit, usually under time pressure and molecule by molecule. When several makers of the same product exit around the same time, a shortage follows.

## Why Nobody Has Built This
Product P&Ls are built for finance, quality costs sit in the QMS, supply risk in procurement, and market structure in commercial databases. No one joins them per molecule, and exit decisions are sensitive enough that they are made in small meetings.

## What to Build
A per-molecule margin-at-risk model: current price and volume, cost to serve, scheduled quality and regulatory costs, API supplier concentration and inspection status, and the number of other active suppliers, with a time-to-event estimate of interruption. It ranks molecules for price renegotiation, second sourcing or planned exit, and drafts the advance notice to FDA that a planned discontinuance requires.

## Target Customer
Supply chain and portfolio heads at generic makers with several hundred marketed molecules.

## Impact If Built
Planning exits and price changes ahead of cost shocks would avoid failure-to-supply penalties and emergency air freight worth several million dollars a year at a large maker (estimate), and would give buyers time to source before a shortage.
