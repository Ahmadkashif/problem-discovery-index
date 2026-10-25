# Account-Level Price Response for the Annual Increase

**Niche:** [[niches/waste-haulers/commercial-price-retention/profile|Commercial Price Increases & Account Retention]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Haulers raise thousands of commercial accounts every year by cohort percentages and learn which ones would have stayed at a higher price only from who cancels.
**Tags:** #survival-analysis #causal-inference #gradient-boosting #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to push the annual commercial price increase through without the customer leaving for a rival hauler or a broker, and whoever loses the fewest accounts per point of increase takes the account.

## The Problem
A regional hauler sends the annual increase in a batch: perhaps 6% on most accounts (illustrative), more on accounts priced below a floor, less on large or contested ones. Cancellations follow over the next months, some to competitors, some to brokers, some to closures. The hauler never learns which accounts would have taken 8% and which left because of 6%, because the increase was not varied in a way that can be measured.

## Why Nobody Has Built This
Pricing decisions are made by managers who trust their read of local competition, increases are not randomised, and the outcome (cancellation) arrives months later mixed with business closures. Billing systems store rate history but not the decision behind it.

## What to Build
A survival model of time-to-cancellation with price-change, fee, service-quality and competitor-presence covariates, and a deliberate experiment design that varies increases within safe bands so response can be measured. Outputs: recommended increase per account, expected loss per point, and the retention offer most likely to work when the customer calls.

## Target Customer
Pricing and revenue managers at haulers with 5,000+ commercial accounts.

## Impact If Built
Reaching the same average yield with ~10–20% fewer cancellations (estimate) is worth ~$0.5–1M a year to a hauler with a $50M commercial book.
