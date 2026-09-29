# Contribution That Transfers

**Niche:** [[niches/esports-organizations/roster-valuation/profile|Roster Valuation]]
**Industry:** [[industries/esports-organizations|Esports Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A player's statistics describe a situation, not a player, and the contract is signed as though they describe the player.
**Tags:** #causal-inference #bayesian-linear-regression #confidence-intervals #gradient-boosting #evaluation-metrics #hypothesis-testing #revenue-impact #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to establish what a player will contribute to a different team, when every statistic available depends on the patch, the meta, the role and the teammates they had — and whoever solves the transfer takes the account.

## The Problem
Esports statistics are situational to an unusual degree. The game itself changes every few weeks with patches. The prevailing strategy shifts. A player's role determines which numbers they can accumulate. Teammates create or absorb the opportunities that generate those numbers. League strength varies enormously. So the figures that look like an individual's performance are largely a description of the circumstances they played in, and the signing decision treats them otherwise.

## Why Nobody Has Built This
The analytical staff are employed to win the next match, not to value transfers. Sample sizes per player per patch are small. Cross-league comparison requires data organisations do not share. And the scouting culture regards this as a judgement question rather than a measurement one.

## What to Build
Adjust for the situation before comparing anyone to anyone. Estimate individual contribution net of teammate, role and patch effects, which is the core — the raw statistic describes a situation and the decision needs a property of the person. Normalise across leagues using the matches where they meet, since cross-league comparison is the commonest and most expensive error. Model patch and meta as explicit covariates rather than pooling across them, as pooling is what makes the numbers untransferable. Report contribution with an interval, because small samples per context mean the uncertainty frequently exceeds the difference between candidates. Project performance onto the signing team's specific composition and style, which is the actual question and is never asked in that form. Value consistency and adaptability across metas separately from peak performance, as the former predicts transfer success and the latter sells highlight reels. Track past signings against realised outcomes to calibrate, which no organisation does. Include age and career stage, given how short these careers are. Combine the model with scouting judgement rather than replacing it, which is what gets it used. And price the contract against contribution and its uncertainty rather than against reputation.

## Target Customer
Esports organisations and general managers, leagues, player agencies, and sports analytics vendors.

## Impact If Built
The raw statistic describes a situation and the decision needs a property of the person. Contribution estimated net of teammate, role and patch effects, projected onto the signing team, is the question nobody currently asks.
