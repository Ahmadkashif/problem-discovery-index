# Measuring Under Label Scarcity

**Niche:** [[niches/crypto-exchanges/screening-decision-quality/profile|Screening Decision Quality]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The outcome returns on well under one percent of freezes, and the whole evaluation problem is what to do with that.
**Tags:** #confidence-intervals #hypothesis-testing #expectation-maximization #evaluation-metrics #bayesian-inference #cross-validation #compliance #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to measure and defend a freeze decision whose ground truth returns on a fraction of a percent of cases — and whoever can state a precision with a defensible interval sets the threshold everyone else guesses at.

## The Problem
Thousands of freezes a month, and the resolved outcomes number in the tens: a law enforcement confirmation here, a provenance that satisfied an analyst there. Standard evaluation assumes a labelled test set and there is not one. So the question — what fraction of our freezes are correct — is treated as unanswerable, and a threshold that determines whether customers can reach their money is set by feel and adjusted after incidents.

## Why Nobody Has Built This
Label scarcity was accepted as a fact rather than treated as a modelling regime, and the methods that handle it — partial identification, deliberate sampling, proxy outcomes — were never brought to bear because nobody framed the problem as solvable. The institution bears no cost for a false freeze, which removes the demand. The regulator asks about coverage rather than precision. And a measured error rate creates a documented exposure that nobody wants to be first to hold.

## What to Build
Build the measurement regime around the scarcity. Enumerate every source of partial outcome evidence — confirmations, satisfying provenance, post-release account behaviour, complaints, subsequent flags on the same customer, cases closed without action — which is the core and turns tens of labels into hundreds of weak ones. Estimate precision as a bounded interval rather than a point, since honest bounds are decision-useful and the current silence is not. Sample deliberately near the threshold and investigate those cases to conclusion, because a small dedicated labelling budget placed where the decision is uncertain is worth more than a large one placed randomly. Use the released deposits as a natural control and track what happened to them, since the exchange releases most deposits and never looks back. Model the decision's cost on both sides explicitly, as a threshold cannot be chosen without a stated price for each error. Treat the vendor score as a feature to be validated rather than a verdict, which is the model risk requirement nobody applies. Backtest threshold changes against the historical case record, since the counterfactual is computable for anything already scored. Report the estimate with its uncertainty to the board and the examiner, because an institution that states a range is in a far stronger position than one that cannot answer at all. Separate attribution error from decision error, which the decomposition makes possible and which is necessary to fix either. And re-estimate on a schedule, since the adversary and the chains both move.

## Target Customer
Exchange compliance and model risk leadership, examiners assessing a control's effectiveness, and monitoring vendors whose tuning methods assume labels.

## Impact If Built
Label scarcity was accepted as a condition rather than approached as a regime, so the methods that exist for it were never applied. Weak outcome evidence plus deliberate near-threshold sampling converts an unanswerable question into a bounded one.
