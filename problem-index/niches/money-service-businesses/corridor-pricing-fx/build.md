# Corridor-Day Elasticity From Your Own Transfers

**Niche:** [[niches/money-service-businesses/corridor-pricing-fx/profile|Corridor Pricing & FX Margin]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pricing teams move FX spreads daily without knowing how much volume each basis point buys in each corridor.
**Tags:** #bayesian-inference #causal-inference #hypothesis-testing #gradient-boosting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each corridor's fee and FX spread so the landed amount wins the sender's comparison while still paying back acquisition cost, and whoever prices each corridor-day most precisely takes the account.

## The Problem
In a corridor such as US–Mexico or US–Pakistan, senders compare landed amounts and switch for small differences around paydays, while loyal senders barely react. Pricing teams set spreads by matching a few competitors and watching volume the next week, unable to separate their own price effect from competitor moves, FX swings and seasonality.

## Why Nobody Has Built This
Prices respond to competitors and competitors to them, so naive regressions mislead. Pricing teams are small and treasury-led, and transmitters have been reluctant to run randomised price tests on live customers.

## What to Build
A hierarchical demand model per corridor, channel and amount band, estimating volume and new-sender response to own and competitor landed amounts, identified from small randomised price tests and exogenous FX moves, with uncertainty that tells the team where to test next. It outputs a recommended spread per corridor-day with expected volume and margin.

## Target Customer
Heads of pricing at transmitters pricing more than a few dozen US-outbound corridors.

## Impact If Built
Margin is kept where senders are insensitive and given up only where it buys volume — a few basis points across billions of dollars of send volume is material to profit.
