# Corridor Lifetime Value From the First Transfer

**Niche:** [[niches/money-service-businesses/digital-remittance-apps/profile|Digital-First Remittance Apps]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Apps bid for new senders on cost per first transfer, when the value of a sender depends on corridor, funding method and payday rhythm that are visible within a week.
**Tags:** #survival-analysis #gradient-boosting #causal-inference #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every app is fighting to win a migrant sender's second and tenth transfer, but that is two contests with different winners: a pricing contest over the landed amount shown corridor by corridor, won by FX and pricing discipline, and a risk contest over approving a first-time sender in minutes without paying out stolen or scam-induced funds, won by data and models. Decomposed into contested sub-niches below.

## The Problem
A sender to Guatemala who sends every second Friday is worth far more than a one-off sender to the same country, and a sender acquired with a promotional rate behaves differently from one who arrived by referral. Marketing teams set channel bids and promotions on blended corridor averages, so they overpay for one-time senders and underbid for regulars.

## Why Nobody Has Built This
Generic lifetime-value models treat remittance like retail purchases; they miss the payday cycle, the shift from promotional to standard pricing, the effect of risk friction on the second transfer, and the corridor's own seasonality. Remittance teams build crude versions in-house and rarely test them causally.

## What to Build
A model that predicts each new sender's expected transfers and margin over 12–24 months from the first week's behaviour, corridor, funding method, acquisition source and the friction they met, validated by holdout experiments on bids and promotions, and fed back into acquisition bidding and onboarding policy.

## Target Customer
Heads of growth and finance at app-first transmitters spending heavily on paid acquisition.

## Impact If Built
Acquisition spend moves toward senders who stay, promotions stop subsidising one-time senders, and the risk team can see what its friction costs in lifetime value, not just in first-transfer conversion.
