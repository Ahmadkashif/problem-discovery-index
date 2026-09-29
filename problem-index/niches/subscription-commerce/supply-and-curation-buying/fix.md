# The Substitution Nobody Wanted

**Niche:** [[niches/subscription-commerce/supply-and-curation-buying/profile|Supply & Curation Buying]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Fix (Pain Point)
**One-liner:** When the buy falls short, subscribers receive a substitute chosen by whoever is packing, and the substitution is recorded as a fulfilled order rather than as the retention event it is.
**Tags:** #evaluation-metrics #descriptive-statistics #revenue-impact #confidence-intervals #automation #causal-inference #quick-win #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to buy the right quantity of the right things for a subscriber base whose size and composition at delivery is unknown — and whoever does that protects the margin, because the buy is committed months before the base that receives it is known.

## The Problem
The buy falls two thousand units short. Operations substitutes from whatever is in the warehouse, spread across whichever subscribers happen to be picked last, with the choice made by a packer working to a deadline. Some substitutions are fine and some go to subscribers who explicitly excluded that category at sign-up. The system records two thousand fulfilled orders. Several weeks later a group of cancellations appears, is attributed to general dissatisfaction, and nobody connects it to a stock shortfall three months earlier that was resolved operationally.

## Why It's Still Broken
Substitution is a fulfilment decision made under time pressure and is designed to get boxes out of the door, which it does. The subscriber-level consequence is invisible to the person substituting and the churn arrives weeks later in a different report. Nothing records what was substituted for whom, so the analysis is impossible even retrospectively. And the shortfall is treated as resolved once the boxes ship.

## What a Fix Looks Like
Make substitution a decision rather than an accident. Record every substitution against the subscriber and the reason, which costs a field and makes the entire retention consequence analysable for the first time — this is the fix's precondition and takes an afternoon. Allocate the shortfall deliberately, sending substitutions to the subscribers least likely to mind, which the preference model can identify and which turns a random harm into a managed one. Never substitute against a stated exclusion, which requires the exclusion to be checked at pack time and is the single most damaging failure available. Tell the subscriber before the box arrives and offer a choice or a credit, since a substitution explained in advance is a service moment and one discovered on opening is a betrayal. Measure the retention effect of substitution per type, so the true cost of a shortfall is known and can be weighed against buying deeper. Feed that cost back into the buy decision, which is where the shortfall originated and where the cost belongs. Prefer shipping short with a credit over substituting badly, which is sometimes the better outcome and is never considered. And report substitution rate as a standing operating metric, since it is a leading indicator of the churn that follows.

## Who Feels the Pain
Subscribers receiving something they excluded; packers making retention decisions under a deadline; and operators whose churn has a cause three months upstream that nobody has connected.

## Impact If Fixed
Recording the substitution against the subscriber costs a field and makes the retention consequence analysable at all. Allocating the shortfall to the subscribers least likely to mind converts a random harm into a managed one, and the measured cost belongs in the buy decision that caused it.
