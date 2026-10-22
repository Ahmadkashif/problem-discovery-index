# Promo Rates That Buy One Transfer

**Niche:** [[niches/money-service-businesses/digital-remittance-apps/profile|Digital-First Remittance Apps]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Fix (Pain Point)
**One-liner:** First-transfer promotional exchange rates attract deal-hunters and duplicate accounts, and the cost shows up only when the second transfer never comes.
**Tags:** #gradient-boosting #k-nearest-neighbors #causal-inference #evaluation-metrics #revenue-impact #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every app is fighting to win a migrant sender's second and tenth transfer, but that is two contests with different winners: a pricing contest over the landed amount shown corridor by corridor, won by FX and pricing discipline, and a risk contest over approving a first-time sender in minutes without paying out stolen or scam-induced funds, won by data and models. Decomposed into contested sub-niches below.

## The Problem
Apps offer a better rate or zero fee on the first transfer. Some new senders become regulars; many send once, and some open repeated accounts with new emails and phone numbers to collect the promotion again, often paying out to the same receiver.

## Why It's Still Broken
Promotions are owned by marketing, duplicate-account detection by risk, and nobody measures the promotion's incremental value by corridor. Duplicate accounts share receivers and devices, but that link is checked only for fraud, not for promotion abuse.

## What a Fix Looks Like
Block repeat promotions using receiver, device and payment-instrument links already computed for fraud; measure each promotion's incremental second-transfer rate against a holdout; and stop promotions in corridors where they buy only one transfer.

## Who Feels the Pain
Growth teams whose acquisition costs look better than they are, and finance teams reconciling promotion spend against retained volume.

## Impact If Fixed
Promotion spend falls where it buys nothing, with no new infrastructure beyond joining data the risk team already holds.
