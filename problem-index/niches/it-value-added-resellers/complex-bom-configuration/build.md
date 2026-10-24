# A Fit Checker Trained on the Reseller's Own Installs

**Niche:** [[niches/it-value-added-resellers/complex-bom-configuration/profile|Complex BOM Configuration & Site Fit]]
**Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Configurators check vendor rules; nothing checks a BOM against what this reseller has seen go wrong at sites like this customer's.
**Tags:** #tacit-knowledge-ml #gradient-boosting #k-nearest-neighbors #transformers #feature-engineering #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to send solution quotes whose bills of materials install as quoted at the customer's site, and whoever ships the lowest share of quoted lines needing a post-order change order or return takes the account.

## The Problem
A senior engineer reviewing a BOM catches missing power supplies, wrong optics, short licence tiers and support that won't co-term, from memory of past installs. Junior engineers and small resellers don't have that memory, and the senior one is overloaded at quarter-end.

## Why Nobody Has Built This
The training data doesn't exist in one place. Configurator vendors see configurations but not installs; PSA vendors see tickets but not the BOM; resellers never captured the expert's edits as data.

## What to Build
A review surface that diffs configurator exports against the final quote and captures each expert edit with a one-click reason; install tickets, change orders and RMAs joined back to quote lines; then a ranked fit checker that reads each new BOM against vendor rules, the customer's installed base and the reseller's own history, with every flag citing the past case behind it. Start with nearest-neighbour retrieval of similar past deals; add classifiers once enough labels exist.

## Target Customer
Pre-sales leaders at resellers with 10+ solution engineers and a recurring change-order cost they can name.

## Impact If Built
Cutting post-order change orders from ~10% to ~4% of solution deals (estimate) is worth ~$2–4M a year on $200M of solution sales, and lets a junior engineer ship quotes the senior one would sign.
