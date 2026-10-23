# A Recirculation Planner Across Every Bank in the Vault

**Niche:** [[niches/armored-car-services/vault-processing-recirculation/profile|Vault Counting, Fitness Sorting & Local Recirculation]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A carrier's vault holds many banks' cash and sorts every note it receives, but plans each bank's Fed deposits and orders separately, shipping fit notes to the Fed on Monday that another order needs on Wednesday.
**Tags:** #optimization-fundamentals #time-series-forecasting #gradient-boosting #data-integration #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to sort deposited notes to Federal Reserve fitness standards and send them back out to the bank's own branches and ATMs instead of round-tripping them through the Fed, and whoever recirculates the most fit notes locally takes the account.

## The Problem
Every Fed round-trip costs transport, processing and, above a de minimis amount, a recirculation fee; every fit note held too long costs the owning bank funding. The vault's planners decide what to ship and what to keep with limited foresight of the coming week's orders.

## Why Nobody Has Built This
Each bank owns its own inventory in the carrier's vault, so cross-bank planning raises ownership and accounting questions. Order forecasting is done by banks or their vendors, not by the vault. Sorters produce fitness data that rarely leaves the counting room.

## What to Build
A planner that forecasts each bank's branch and ATM orders by denomination for the coming week, combines them with the fit inventory sorted from deposits, and recommends what each bank should hold, issue and ship to the Fed to minimise fees and funding cost while keeping orders filled. Ownership stays per bank; the planner simply sees all of them at once and nets within each owner's rules.

## Target Customer
Vault operations and cash management product leaders at national and large regional carriers; banks outsourcing vault services.

## Impact If Built
More notes reused locally cuts Fed fees and transport for banks and gives the carrier a measurable reason to be chosen as vault provider.
