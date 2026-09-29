# Holdout Testing Practice

**Niche:** [[niches/affiliate-networks/channel-incrementality-verification/profile|Channel Incrementality Verification]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Incrementality testing is standard practice in every other performance channel, and affiliate is the one where nobody ever runs it.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #bayesian-inference #descriptive-statistics #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to tell a merchant whether affiliate produced any sales at all — and whoever runs that test credibly decides whether the channel's reported return survives contact with evidence.

## The Problem
Holdout and geo testing are routine in performance marketing. Advertisers test paid search brand terms, suppress display to a region, hold out an email cohort, and measure the difference — because the attributed numbers in those channels are known to overstate. The designs are documented, the analysis is standard, and the tooling is available. Affiliate is the channel with the strongest structural reason to expect overstatement and the one where the test is essentially never run.

## What Already Exists
Geo-based holdout design and analysis; user-level suppression testing; synthetic control methods for regional comparison; power analysis for lift detection; and continuous always-on holdout frameworks.

## The Customization Gap
The adaptation is to a channel whose participants are paid third parties. It requires: (1) suppression implemented at the tracking layer rather than at the media buy, since there is no spend to withhold — the intervention is refusing to credit rather than refusing to show, which is a mechanically different design; (2) partner-type stratification as the primary cut, because the channel is a mixture of roles whose incrementality differs by an order of magnitude and a channel-level average is the least useful possible summary; (3) contractual consequences, since suppressing tracking affects partners' earnings and the design must handle that commercially as well as statistically; (4) network cooperation to implement suppression, which the network has a direct interest in refusing — this is the practical obstacle and it shapes who can build the product; and (5) substitution measurement across channels, since the counterfactual involves shoppers arriving by other paths rather than not arriving.

## Target Customer
Merchant measurement teams, independent measurement vendors, and experimentation vendors for whom affiliate verification is unserved.

## Impact If Solved
Every other performance channel tests for overstatement and the one most structurally prone to it does not. Suppression at the tracking layer rather than the media buy is the design change, and partner-type stratification is what turns a meaningless average into a decision.
