# The First Two Weeks Nobody Feeds Back

**Niche:** [[niches/retail-pos-platforms/merchant-underwriting-risk/profile|Merchant Underwriting & Risk]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A new merchant's first fortnight of transactions is the single most informative thing anyone will ever learn about them, and it is used for fraud alerting and never fed back into the model that approved them.
**Tags:** #change-point-detection #logistic-regression #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #quick-win
**Contested on:** Every serious competitor in merchant onboarding is fighting to approve a merchant in minutes at the same loss rate a week of manual review would produce — and whoever holds that trade-off best takes the volume.

## The Problem
A merchant approved as a boutique retailer processes, in its first two weeks, transactions with an average ticket four times its stated expectation, a card-not-present share far above the norm for its category, and a cluster of test transactions from a single card. Fraud monitoring generates alerts on some of this. None of it is connected back to the underwriting decision, so the underwriting model never learns that applications with this application profile produce this early behaviour — which is the fastest-arriving, highest-signal outcome data the platform has, available fourteen days after approval rather than after a loss event months later.

## Why It's Still Broken
Underwriting and fraud monitoring are different teams with different systems and different metrics, and nobody owns the loop between them. Model retraining in underwriting typically uses realised losses as the label, which arrive slowly and sparsely, and early behavioural divergence has not been adopted as an intermediate outcome even though it is a strong leading indicator. And the platform's growth incentives mean that scrutinising recently approved merchants is organisationally unwelcome.

## What a Fix Looks Like
Define an early-behaviour outcome and close the loop. Fourteen and thirty days after approval, compute a divergence measure between the merchant's stated business and its actual transaction profile — ticket distribution, channel mix, refund rate, velocity, card testing patterns, geographic dispersion. Use it as an intermediate label for underwriting model training, which means the model gets feedback in weeks rather than in quarters and can adapt to adversarial shifts at something like their own pace. Use it operationally too: a merchant diverging sharply in week one is the right moment for a proportionate intervention, when the exposure is still small. And report approval-cohort divergence rates back to underwriting as a standing metric, which is how a policy change becomes evaluable before its losses arrive.

## Who Feels the Pain
Risk teams reacting to losses months after the decisions that caused them; underwriting teams whose policy changes cannot be evaluated for two quarters; and legitimate merchants caught in the blunt tightening that follows a bad loss month.

## Impact If Fixed
Early divergence is the fastest outcome signal available in merchant risk and is currently discarded. Feeding it back shortens the underwriting feedback loop from quarters to weeks, which in an adversarial domain is the difference between adapting and being outrun. The operational use — intervening early while exposure is small — also reduces the severity of the interventions this business has to make.
