# A Measurement Business That Does Not Measure Itself

**Niche:** [[niches/marketing-attribution-vendors/validation-and-ground-truth/profile|Validation & Experimental Ground Truth]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The product is a number that reallocates a marketing budget, derived from observational data, and essentially nobody in the category backtests it against an experiment that could show it was wrong.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #bayesian-inference #monte-carlo-methods #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to make experiments the ground truth and every model an interpolator between them — and whoever does that credibly makes their own error rate visible and resets the terms the whole category competes on.

## The Problem
A vendor tells a client that a channel contributed a given amount. The client moves budget on it. Whether the number was right is never established. The vendor's model fits its training data well, which is reported as accuracy and is not evidence of anything causal. When a client does run an experiment, the result is frequently far from the model's estimate, and that discrepancy is discussed once and not recorded. Across the category this has happened thousands of times and no vendor can state how often their estimates are within a useful distance of an experimental result, because none of them has collected the comparison.

## Why Nobody Has Built This
Publishing an error rate makes a vendor's failures visible while competitors publish none, which is a straightforward first-mover disadvantage and is the entire reason the category has no validation norm. Experiments are expensive and sparse, so the validation set is small. Clients have accepted models without validation for two decades. And a vendor whose numbers turned out to be frequently wrong would have to explain that to existing customers.

## What to Build
Invert the relationship between models and experiments. Treat every experiment as ground truth and every model as an interpolator between them, which is the conceptual change and reframes the product from an answer to a continuously validated estimate. Record every model prediction before the outcome is known, since retrospective claims of accuracy are worthless and prospective records are the only credible basis. Backtest systematically against every experiment run, including the ones the model got wrong, and keep the record. Report the error distribution rather than a fit statistic, so a client knows how much to trust the number for a decision of a given size. Recalibrate continuously from each new experiment, which is what makes the model improve rather than merely persist. Estimate where the model is reliable and where it is not, since accuracy varies by channel, spend level and business type and an average error rate conceals that. Design experiments specifically to test the model where it is least certain, which is the efficient use of a scarce validation budget. Pool validation across clients, connecting to the priors work, since experiments are rare per client and abundant across a portfolio. Publish the methodology and the error rates, because that is the move that resets the category and it only works if it is verifiable. And support client-side audit, since a validated number that cannot be checked is still an assertion.

## Target Customer
Measurement vendors willing to compete on correctness, client measurement and finance functions, and the advertisers reallocating budgets on unvalidated numbers.

## Impact If Built
A business whose product is measurement has no measurement of itself, because publishing an error rate is a first-mover disadvantage. Recording predictions prospectively and backtesting against every experiment converts an assertion into a continuously validated estimate.
