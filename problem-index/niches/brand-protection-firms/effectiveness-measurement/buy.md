# Buy: Incrementality Measurement From Marketing

**Niche:** Enforcement Effectiveness Measurement
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Marketing learned to separate activity from effect with holdouts and geographic tests, and brand protection reports activity and calls it effect.
**Tags:** #causal-inference #bayesian-inference #evaluation-metrics #confidence-intervals #hypothesis-testing #gradient-boosting #revenue-impact
**Contested on:** Whether anyone can show that enforcement reduced counterfeit sales, or only that it produced takedowns.

## The Problem

Separating what a spend caused from what would have happened anyway is a problem marketing spent two decades on, and its answers are well developed.

Incrementality testing withholds a channel from part of a market and compares. Geographic holdouts use matched markets to establish a counterfactual. Media mix modelling estimates the contribution of each channel with saturation curves. And the discipline is now thoroughly sceptical of attributed results, having learned that reported conversions overstate incremental effect substantially.

Brand protection is in the position marketing was in before that reckoning. It reports attributed activity — listings removed, attributed to the enforcement programme — with no counterfactual, no holdout and no saturation estimate. Whether the next unit of spend removes more infringement or the same infringement more often is unknown.

The methods transfer with unusual directness, because enforcement intensity already varies across a brand's categories, platforms and markets, which supplies the natural experiment without anyone having to design one.

## What Already Exists

Incrementality testing: holdout design, matched-market testing and the platforms that run them.

Media mix modelling: channel contribution estimation with saturation and carryover, with commercial and open-source implementations.

Causal inference: synthetic control, difference-in-differences and matched comparison, developed for exactly the question of what a policy or spend caused.

Prevalence measurement: survey methodology for estimating a population proportion, entirely standard.

Brand protection: takedown reporting, with some prevalence sampling by a minority of firms.

## The Customization Gap

**Holdouts are ethically awkward and already exist naturally.** Deliberately not enforcing in a category to measure the effect is uncomfortable. Enforcement intensity already varies enormously across categories, markets and platforms for budget reasons, which supplies the comparison without anyone withholding anything.

**The outcome is not directly observable.** Marketing measures sales. Counterfeit sales are unobservable, so the analysis must work with proxies — prevalence, exposure, warranty claims, seizures — each biased differently and best used together.

**Saturation is the unasked question.** Marketing estimates where returns diminish. Nobody has asked whether the next thousand takedowns buy anything, and the answer is likely to be uncomfortable given the re-emergence pattern.

**Attribution scepticism has to be imported wholesale.** The most valuable lesson marketing learned is that attributed results overstate effect. Brand protection reporting is attributed activity with no counterfactual, which is precisely the pattern that reckoning addressed.

**Cross-channel allocation has an analogue.** Enforcement levers — listing notices, payment reports, infrastructure action, legal — are channels competing for a fixed budget, and the allocation is currently made by convenience rather than by measured return.

**The measurement would be done by the party being measured.** A firm modelling its own incremental effect has an obvious interest, which argues for the brand or an independent party doing it.

## Target Customer

Brand leadership and finance, who already understand incrementality from their marketing spend and would recognise the framing immediately — this is the argument that lands fastest with them.

Brands with enough category and market variation to support a natural-experiment analysis, which is most large brands.

Measurement specialists as the provider, since a firm measuring its own effect is not a credible arrangement and the analysis is well within a marketing analytics team's capability.

## Impact If Solved

Two decades of hard-won scepticism about attributed activity applies to an industry reporting attributed activity in almost exactly the form marketing used to.

The natural experiment already exists in the variation of enforcement intensity across a brand's own categories and markets, which means no holdout needs to be designed and the analysis can be run on historical data.

And a saturation estimate would answer the question nobody has asked: whether the next increment of enforcement spend buys a reduction in infringement or the same operators removed more frequently.
