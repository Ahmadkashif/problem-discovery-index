# Air Ambulance Offer Model Trained on IDR Determinations

**Niche:** [[niches/ambulance-services/air-medical-out-of-network-payment/profile|Air Medical Transport & Out-of-Network Payment]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Air operators pick their IDR offers from habit and a spreadsheet when CMS publishes every determination's offers, QPA and winner, and their own files hold the payer's past behaviour.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get paid for flights flown to patients whose health plans do not contract with the operator, and whoever collects the most per out-of-network transport after independent dispute resolution takes the account.

## The Problem
In baseball-style IDR the certified entity must pick one of the two final offers. An operator that offers too high risks losing the whole dispute to the plan's offer, near the QPA. An operator that offers too low leaves money behind on every win. Air operators won 89% of determinations in Q2 2025, which suggests many offers sit below what would still win (CMS). Each dispute also costs an administrative fee and entity fees, so a poorly chosen dispute costs money even when it wins.

## Why Nobody Has Built This
The public IDR files are large (one 2025 quarterly file exceeds a gigabyte) and CMS has published them quarterly only since early 2024, starting with 2023 data. Air ambulance is a small share of disputes. Operators' revenue teams are built to file, not to model, and IDR representation firms are paid per dispute, so they gain from volume rather than offer precision.

## What to Build
A model that, for each out-of-network flight, predicts the probability that a given offer wins against this plan, in this state, at this QPA and mileage. It is trained on the CMS public IDR files (air ambulance determinations, offers as dollars and percentage of QPA, prevailing party, entity) and on the operator's own determinations and open-negotiation outcomes. It recommends the offer that maximises expected collection net of fees, and flags flights where accepting the open-negotiation counteroffer beats disputing.

## Target Customer
Revenue-cycle leaders at the three air operators that bring 82% of air disputes, and at the hospital-based and regional programmes behind them, plus the IDR representation firms that serve them.

## Impact If Built
If better-placed offers raised collected revenue per disputed flight by 5% (an estimate) on 10,000 disputes a quarter at a $20,000 average award (an estimate), that is ~$10M a quarter across the field.
