# Carrier Capacity Matching

**Parent Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in load matching is fighting to cover a load on the first carrier contacted, at a rate that carrier will accept — and whoever holds first-tender acceptance rate highest takes the account.

## Profile
**Market Size:** ~$850M US spend across load boards, digital brokerage matching and carrier sales tooling
**Share of Parent Industry:** ~11% of freight technology revenue
**Digital Adoption:** Medium — loads are posted digitally and covered by telephone
**Target Buyer:** Product leads at brokerage platforms and load boards; carrier sales managers who staff the calling
**Automation Potential:** Very High — this is a matching and pricing problem over the richest behavioural dataset in freight

## What Makes This a Distinct Niche
A brokerage covers loads by having people call carriers. A carrier sales rep makes on the order of two hundred calls a day, most of which are declines, to cover a handful of loads. The information that would make most of those calls unnecessary is in the brokerage's own system: which carriers have run this lane, which ones were running toward this origin last week, who accepted at what rate on comparable freight, who has equipment of the right type and a driver with hours, and what rate each one has historically accepted on lanes of this shape. Digital brokerage attempted to automate this and the category retrenched sharply, partly because the matching was built on load attributes rather than on carrier behaviour and partly because the economics were pursued in the wrong order. The contested capability is unchanged and unclaimed: covering the load on the first call.

## Current Tools & Gaps
DAT and Truckstop are the market's price discovery and matching mechanism and are essentially bulletin boards with search. Brokerage platforms provide carrier relationship management with call logging and lane preferences, which are entered by reps inconsistently. Digital brokerages built automated matching with mixed results and the survivors have converged toward the incumbent operating model. The gaps: carrier lane preferences are self-declared rather than learned from behaviour, acceptance probability at a given rate is not modelled despite every tender and response being logged, the carrier's current position and likely next need is not used even where visibility data exists, and nobody measures first-tender acceptance rate — the metric that would tell a brokerage whether any of its matching investment worked.

## Problems
- [[niches/freight-tech-platforms/carrier-capacity-matching/build|🔨 Build: Acceptance Probability Learned From Every Tender Ever Sent]]
- [[niches/freight-tech-platforms/carrier-capacity-matching/buy|🛒 Buy: Recommender Infrastructure Applied to Load Matching]]
- [[niches/freight-tech-platforms/carrier-capacity-matching/fix|🔧 Fix: Two Hundred Calls a Day and No Record of Why They Failed]]
