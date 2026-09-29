# Merchant Lifetime Risk Rather Than Onboarding Risk

**Niche:** [[niches/retail-pos-platforms/pos-payments-merchant-services/profile|POS Payments & Merchant Services]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Platforms assess a merchant once, at signup, from application data, and then observe that merchant's actual behaviour every day for years without ever updating the assessment until something goes wrong.
**Tags:** #survival-analysis #gradient-boosting #change-point-detection #confidence-intervals #evaluation-metrics #bayesian-inference #revenue-impact #compliance
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A merchant is approved on the basis of an application, a credit check and a business category. Eighteen months later they take a surge of unusually large card-not-present transactions, their refund rate triples, their average ticket doubles, and they begin accepting deposits for goods with long lead times. Each of those is a documented precursor to the kind of failure that leaves an acquirer holding chargebacks for goods never delivered. The platform's risk assessment is still the one made at signup. The observation that would have updated it has been flowing through the platform continuously the entire time.

## Why Nobody Has Built This
Underwriting and ongoing monitoring are organisationally separate — underwriting is an onboarding function measured on approval rate and turnaround, and monitoring is a fraud operations function measured on losses detected — and nothing spans them. The behavioural data lives in the processing platform, the application data in an onboarding system, and losses in a chargeback and reserve ledger, and the join is not made. There is also a growth tension: a continuously updated risk view will produce recommendations to reduce exposure on merchants who are currently producing volume, which is a conversation nobody in a growth-oriented payments business wants to have.

## What to Build
A merchant risk state that updates continuously from behaviour. Transaction mix, ticket size distribution, refund and dispute rates, settlement timing, deposit-taking behaviour, seasonality against the merchant's stated category, and changes in any of them form the observation stream; the application data is the prior. The output is a hazard — probability of a loss event in the coming period — with the contributing signals named, and a proportionate response rather than a binary one: adjust reserve, adjust settlement timing, request documentation, or simply watch. The proportionality matters commercially and ethically, since a small merchant abruptly cut off or held in reserve can be destroyed by a false positive, and the platform's incentive to protect itself is stronger than its incentive to be right. Attribution is the other half: every loss should be traceable to the decisions that preceded it, which is what lets the platform learn rather than merely react.

## Target Customer
POS platforms and acquirers carrying merchant credit and fraud losses, ISOs with portfolio exposure, and the underwriting and risk teams inside them.

## Impact If Built
Continuous risk assessment converts a static gate into a managed portfolio, and the loss events this category absorbs are concentrated in merchants whose behaviour changed visibly beforehand. Proportionate intervention also reduces the collateral damage of the current approach, which is to act late and hard on a small merchant who may not deserve it.
