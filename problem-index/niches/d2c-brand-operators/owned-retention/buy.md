# Uplift Modelling and Customer Base Management

**Niche:** [[niches/d2c-brand-operators/owned-retention/profile|Owned Retention]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Telecoms and banking built customer base management with uplift models and contact policies decades ago, and direct-to-consumer retention sends to everybody.
**Tags:** #causal-inference #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing #cross-validation
**Contested on:** Every serious competitor in this sub-niche is fighting to get another purchase out of an existing customer without exhausting the audience that took years to build — and whoever does that takes the margin, because messages cost nothing to send and the list is the only asset the platforms cannot take away.

## The Problem
Deciding which existing customers to contact, with what, and how often, is a discipline that telecoms and banks built at scale decades ago. Uplift modelling identifies the customers whose behaviour a contact would actually change, rather than those most likely to buy anyway. Contact policies govern total contact frequency across all campaigns. Next-best-action engines arbitrate between competing messages. Churn prediction drives pre-emptive intervention. All of it exists, is documented, and is not used in this category.

## What Already Exists
Uplift and net lift modelling with established evaluation methods; contact policy management limiting cumulative contact per customer; next-best-action arbitration across campaigns; churn propensity models with intervention design; customer base management practice from telecoms; and the control group discipline those programmes are built on.

## The Customization Gap
The adaptation is to a brand with less data, fewer products and no contract. It requires: (1) uplift modelling on smaller samples, since the telecoms methods assume millions of customers and a direct-to-consumer brand has thousands — which argues for simpler models and pooled priors across comparable brands rather than abandoning the approach; (2) churn defined without a contract, since there is no cancellation event and lapse has to be inferred from a purchase pattern, which is a survival problem rather than a classification one; (3) contact policy across owned and paid, since these brands retarget their own customers on advertising platforms and the contact budget is being spent in two places that do not talk; (4) arbitration across a small product range, where the next-best-action machinery is over-engineered and the useful part is the frequency governance; and (5) a control group discipline the category does not have, which the fix note develops and which everything above depends on.

## Target Customer
Retention teams, messaging platform vendors, and the customer base management practitioners whose discipline transfers to a market that has not adopted it.

## Impact If Solved
Customer base management solved who to contact and how often, decades ago, at scale. Uplift on smaller samples with pooled priors makes it available to these brands, and extending contact policy across owned and paid closes a gap where the same customer is being spent on twice.
