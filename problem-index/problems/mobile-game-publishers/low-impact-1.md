# Soft Launch Geography and Readout

**Industry:** [[mobile-game-publishers|Mobile Game Publishers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Games are validated in a handful of conventional test markets and scaled globally on the assumption that the numbers transfer, which they do inconsistently and in ways nobody models.
**Tags:** #causal-inference #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #transfer-learning #evaluation-metrics #probability-distributions

## The Problem
Before a global launch a game is soft launched in selected markets to validate retention, monetisation and the live operations cadence. The market choice is conventional — a small set of English-speaking and Northern European countries, chosen historically for cheap installs and similarity to the target market.

The assumption is transferability, and it holds unevenly. Monetisation rates differ substantially by market for reasons that include income, payment friction, store behaviour and genre familiarity; retention differs by competitive landscape and device mix; acquisition cost differs by a large factor. A game validated at a given ARPDAU in a small market may perform quite differently at scale in the United States, and the direction is not always the intuitive one.

Readout is the second weakness. Soft launch data is compared against benchmark ranges from previous titles, adjusted by judgement. The comparison rarely accounts for the market difference formally, for the acquisition sources used, or for the fact that a soft launch cohort is acquired differently from a scaled one. Decisions worth tens of millions rest on that comparison.

## What Already Exists
Soft launching is universal practice and the conventional market set is well established. Analytics platforms report cohort metrics by geography. Publishers maintain internal benchmark ranges from their own portfolios. Remote configuration and experimentation platforms allow live tuning during soft launch. Market-level data on install costs and monetisation rates is available from Sensor Tower, data.ai and the ad networks.

## The Customisation Gap
The transfer question is never modelled. What exists is a set of informal adjustment heuristics — multiply monetisation by a factor for this market, expect retention to hold — applied by experienced people. A publisher with a portfolio of titles that have been through both soft launch and global scale has the data to estimate the transfer relationship properly, per genre and per market pair, with uncertainty. That estimate is the single thing that would make a soft launch readout defensible, and essentially nobody has built it.

Market selection is the second gap. The conventional set was chosen for reasons that have shifted, and the right test markets depend on which questions need answering: monetisation depth, retention, live operations tolerance and localisation each favour different markets. Choosing markets to maximise information about the specific uncertainty in this title — rather than by convention — is an experimental design question nobody poses.

Cohort comparability is the third. Soft launch installs come from small campaigns at low volume, which means a different acquisition mix and a different player population from what a scaled launch will bring. Adjusting for that composition difference is straightforward and is not done, which is why soft launch numbers routinely fail to hold at scale in a direction everybody blames on the market.

## Impact If Solved
Soft launch is the last checkpoint before a publisher commits its largest acquisition budgets, and it is read against informal heuristics that nobody has validated. A transfer model estimated from the publisher's own portfolio, information-maximising market selection and cohort composition adjustment would make that checkpoint mean what everyone currently assumes it means — and would stop the recurring pattern of a game that validated in soft launch failing to scale for reasons that were knowable.
