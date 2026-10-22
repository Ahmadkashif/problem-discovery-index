# Credit Line Management

**Parent Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to prove, on randomised holdout cells, that each line increase or decrease earns more incremental revolving balance and interchange than it adds in loss, and whoever measures that counterfactual best takes the account.

## Profile
**Market Size:** ~$3B a year in issuer spend on line-management analytics, bureau refreshes and triggers, decision engines and strategy staff (estimate)
**Share of Parent Industry:** ~5% of issuer spend on data, decisioning and operations (estimate)
**Digital Adoption:** High — line actions are automated batch and real-time decisions
**Target Buyer:** Head of Portfolio Credit Risk / Line Management Strategy Director
**Automation Potential:** Very high

## What Makes This a Distinct Niche
Total credit lines on consumer cards passed $5.7T in 2024 (CFPB) against ~$1.26T of balances, so most of every line is unused, and each line change is a bet: more line means more potential revolving balance and interchange and more exposure at default. Line management is the most mechanical credit decision an issuer makes — millions of proactive increases, requested increases, decreases and over-limit authorisations a month — and the one where the issuer can run clean experiments, because it chooses whom to treat. Its constraints are specific: ability-to-pay for requested increases, Reg B notices for decreases, and loss allowances that move with exposure.

## Current Tools & Gaps
Decision engines (FICO Platform, Experian PowerCurve, Provenir), bureau refreshes and trigger feeds, champion-challenger testing in the engine, in-house uplift models at the largest issuers. Gaps: test-cell history often lost; decisions judged on raw rather than incremental performance; and decreases fired by noisy triggers.

## Problems
- [[niches/credit-card-issuers/credit-line-management/build|🔨 Build: A Counterfactual Ledger for Every Line Action]]
- [[niches/credit-card-issuers/credit-line-management/buy|🛒 Buy: Marketing Uplift Tools Fitted to Credit Lines]]
- [[niches/credit-card-issuers/credit-line-management/fix|🔧 Fix: The Line Decrease Triggered by a Bureau Blip]]
