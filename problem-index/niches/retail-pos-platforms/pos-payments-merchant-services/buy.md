# Credit Risk Practice Applied to Merchant Portfolios

**Niche:** [[niches/retail-pos-platforms/pos-payments-merchant-services/profile|POS Payments & Merchant Services]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consumer and commercial lending have a century of portfolio risk practice — scorecards, vintage analysis, loss forecasting, reserve adequacy — and payments platforms manage merchant portfolios with an approval rule and a monthly loss report.
**Tags:** #logistic-regression #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A payments platform holding merchant credit exposure is running a lending book without the instruments a lender would consider basic. It cannot decompose losses by approval vintage, cannot say whether the cohort approved under last quarter's relaxed criteria is performing worse than the prior one, and sets reserves by a rule rather than by modelled expected loss. When losses rise, the response is to tighten approval criteria globally, which reduces growth uniformly rather than reducing the exposure that produced the loss.

## What Already Exists
Credit risk management is among the most developed quantitative disciplines in existence: scorecard development and validation, vintage and cohort analysis, roll rate and transition modelling, expected loss estimation, reserve adequacy and stress testing are all standard practice with extensive literature, regulatory frameworks and mature tooling. Model governance and validation practice is codified. The methods transfer to merchant portfolios with modest adaptation.

## The Customization Gap
The adaptation is to an exposure that is contingent rather than lent. It requires: (1) modelling the exposure correctly, since a merchant's risk is not a balance but the chargeback and refund liability contingent on transactions already processed, which behaves differently from a loan and peaks with volume; (2) vintage analysis by approval cohort and criteria version, which is what makes an underwriting change evaluable rather than a matter of opinion; (3) reserve and rolling-reserve policy derived from modelled exposure per merchant rather than from a flat percentage, which is where most platforms are simultaneously over-reserving safe merchants and under-reserving risky ones; (4) delivery-lag modelling for merchants selling goods with long fulfilment times, since that lag is the mechanism by which a failing merchant generates losses and is a category-specific feature lending has no analogue for; and (5) model governance appropriate to decisions that terminate small businesses, including an appeal path, which is a fairness requirement that lending has developed under regulation and payments has largely not.

## Target Customer
POS platforms and acquirers carrying merchant exposure, ISOs, and the risk functions inside them staffed by people from payments rather than from credit.

## Impact If Solved
Importing credit portfolio practice gives a payments platform the ability to answer whether an underwriting change worked, which it currently cannot. Exposure-based reserving typically frees capital held against safe merchants while covering the risky ones properly, and the governance and appeal practice is the part that protects merchants from being wrongly destroyed by an automated decision.
