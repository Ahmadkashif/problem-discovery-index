# A Discrepancy Origin Model Across Every Handoff

**Niche:** [[niches/armored-car-services/shortage-discrepancy-claims/profile|Shortage, Discrepancy & Loss Claims]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every discrepancy is investigated as if it were the first, though the carrier holds years of evidence on which customers, devices and counting stations produce them.
**Tags:** #bayesian-inference #hypothesis-testing #gradient-boosting #feature-engineering #data-integration #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to establish where a shortage arose — the customer's count, the truck or the counting room — with evidence before the customer's claim window closes, and whoever settles the most discrepancies without a write-off or an insurance claim takes the account.

## The Problem
A carrier's vault records thousands of small differences a month between declared and counted amounts (estimate). Each is handled on its merits: an analyst checks the seal, maybe pulls a clip, emails the customer. A supermarket whose clerks miscount every week and a counting station whose operator is drifting look, case by case, the same as a bag opened in transit.

## Why Nobody Has Built This
The evidence sits in separate systems owned by different departments — route scans with operations, vault counts with processing, video with security, claims with customer service. Discrepancies are treated as a cost of doing business, and the investigations team is small and works the large cases.

## What to Build
A hierarchical model of discrepancy rates by customer, location, drop type, device, counting station, operator and route, updated with every resolved case, which gives each new discrepancy a probability of origin at each handoff and flags those that do not fit any baseline. Each case opens with its evidence attached: seal photos, scan trail, count-station clip, safe or ATM logs. Investigators work the cases the model cannot explain; customers get a reasoned response within days.

## Target Customer
Vault operations and security directors at the national carriers and the larger regional independents.

## Impact If Built
Faster, evidenced resolution of the routine majority cuts write-offs and claim handling, protects innocent crews, and points investigators at the few patterns — one station, one route, one store — that are real losses.
