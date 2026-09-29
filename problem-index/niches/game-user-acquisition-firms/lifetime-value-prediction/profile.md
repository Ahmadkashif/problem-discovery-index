# Lifetime Value Prediction

**Parent Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Category:** 🔵 High Market Share
**Contested on:** Every serious competitor in this niche is fighting to predict a cohort's lifetime value from a few days of behaviour when most of that value comes from players who have not spent anything yet — and whoever predicts it better takes the account.

## Profile
**Market Size:** ~$11B US
**Share of Parent Industry:** ~28% of category spend
**Digital Adoption:** High, mis-specified
**Target Buyer:** UA and data leadership
**Automation Potential:** High — modelling and decomposition

## What Makes This a Distinct Niche
Bids are set on predicted lifetime value, most of that value comes from a tiny fraction of players, and at prediction time almost none of them have done anything to identify themselves. Every downstream decision — which sources to buy, at what price, which creatives to scale — is an optimisation against this number. A model with good average error and a poor tail will systematically misprice exactly the cohorts worth buying, and the discipline's enormous sophistication is applied on top of it.

### Contested sub-niches
This niche is not terminal. It names a quantity, and two different problems sit underneath it:
- [[niches/game-user-acquisition-firms/heavy-tail-estimation/profile|🎯 Heavy-Tail Estimation]] — predicting a distribution concentrated in a tail
- [[niches/game-user-acquisition-firms/player-content-decomposition/profile|🎯 Player-Content Decomposition]] — separating the player from the content they will meet

## Current Tools & Gaps
An early-days predicted value model, a payback target and a bidding system consuming both. The gaps: models optimised for average rather than tail accuracy; no uncertainty on cohort predictions; no separation of player quality from content effects; no validation against realised long-horizon value; and no per-source calibration.

## Problems
- [[niches/game-user-acquisition-firms/lifetime-value-prediction/build|🔨 Build: Predicting the Number That Matters]]
- [[niches/game-user-acquisition-firms/lifetime-value-prediction/buy|🛒 Buy: Tail Estimation From Insurance and Finance]]
- [[niches/game-user-acquisition-firms/lifetime-value-prediction/fix|🔧 Fix: The Model Is Accurate on Average and Wrong Where It Counts]]
