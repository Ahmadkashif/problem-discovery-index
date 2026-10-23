# An Increase-to-Move-Out Response Model

**Niche:** [[niches/assisted-living-communities/street-rate-renewal-pricing/profile|Street-Rate & Renewal Pricing]]
**Industry:** [[industries/assisted-living-communities|Assisted Living Communities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators choose annual increases without knowing how many residents each extra point drives out.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set each vacant unit's street rate and each resident's annual increase from live demand, and whoever raises revenue per occupied unit without a rise in move-outs in the 90 days after the increase takes the account.

## The Problem
Owners push for larger increases as occupancy recovers. Executive directors warn that families will leave. Neither side has evidence, because move-outs mostly come from health events and the price effect is buried among them.

## Why Nobody Has Built This
Separating price-driven from health-driven move-outs needs resident-level acuity, increase size and move-out reason in one dataset, with variation across buildings. Operators rarely join them, and multifamily tools do not model health at all.

## What to Build
A causal model across an operator's communities that uses differences in increase size and timing to estimate the effect of each extra point of increase on 90-day move-out probability, controlling for acuity, length of stay, payer and local alternatives. It produces resident-level increase recommendations and a community-level revenue-versus-retention curve for the owner.

## Target Customer
Revenue management leads at chains and REIT asset managers overseeing operators under RIDEA management agreements.

## Impact If Built
On an 80-unit community billing ~$5.3M, each point of increase is ~$53,000 a year (estimate). Knowing the move-out cost of the last point lets operators take ~1 more point where demand allows and avoid it where it would cost two or three move-outs.
