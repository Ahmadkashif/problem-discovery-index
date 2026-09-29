# Merchant Onboarding and Cold Start

**Industry:** [[payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every new merchant is a new definition of normal, and the model spends its first months learning it while the merchant judges the product on exactly those months.
**Tags:** #transfer-learning #gradient-boosting #k-means-clustering #bayesian-inference #confidence-intervals #evaluation-metrics #feature-engineering #data-integration

## The Problem
A luxury watch retailer's normal is a single five-thousand-dollar order from a new customer with express shipping to a different address. A meal delivery service's normal is forty orders a week from the same device. A digital goods seller has no shipping address at all. A ticketing platform has enormous velocity around on-sale moments that would look like an attack anywhere else.

A general model applied to a new merchant produces the predictable failure: high false positives in the first weeks, because the merchant's legitimate patterns resemble fraud somewhere else in the training distribution.

Onboarding therefore means tuning. Historical order data is imported where the merchant has it in usable form, rules are written to encode known-good patterns, thresholds are set conservatively and relaxed as evidence accumulates. It takes weeks to months and is performed by an implementation team.

Seasonality extends the problem well beyond onboarding. A merchant's first Black Friday on a new platform is a distribution the model has never seen from that merchant, and the historical window that would have covered it does not exist yet.

Merchants also change. A new product line, a new geography, a new marketing channel bringing a different customer profile — each shifts the distribution, and the model attributes the change to risk because that is the only thing it can attribute it to.

## What Already Exists
Vendors offer historical data import, configurable rules, merchant category baselines and staged rollout. Consortium data provides cross-merchant identity signal that partially substitutes for merchant-specific history. Some platforms support shadow mode so a merchant can compare before switching.

## The Customisation Gap
Transfer is coarse. Merchant category is a weak descriptor of risk profile; two apparel retailers with different price points, geographies and acquisition channels behave very differently. Learning a merchant embedding from early behaviour and borrowing strength from genuinely similar merchants rather than from a category label is a well-posed and largely unattempted improvement.

Uncertainty is not expressed. A new merchant's model should be explicit about what it does not know, and thresholds should be set from posterior uncertainty rather than by a consultant's caution. Bayesian treatment of the cold start is natural here and rare.

Distribution shift is not separated from risk. When a merchant launches a campaign that brings a new customer profile, the correct response is to recognise a shift and adapt, not to decline the new customers. Distinguishing benign shift from an actual attack is the core unsolved problem of onboarding and of merchant change alike.

And nothing tells the merchant what to expect. A new merchant could be shown, from comparable merchants, the approval and review rates likely in each of the first twelve weeks, which would prevent most of the early-relationship friction that causes churn during onboarding.

## Impact If Solved
The onboarding period determines whether a merchant relationship survives, and it is exactly when the model is weakest and the merchant is most attentive. Merchant embeddings for principled transfer, explicit uncertainty in threshold setting and separating benign distribution shift from attack shorten the cold start and remove the failure mode that loses accounts before the product has had a chance to work.
