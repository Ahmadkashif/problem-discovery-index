# The Line Redrawn Every Two Years by Argument

**Niche:** [[niches/open-source-commercial-vendors/open-core-and-licensing/profile|Open Core & Licensing]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Feature flagging and licence enforcement are entirely solved, and where the line between free and paid should sit is redrawn every year or two by argument, because nobody can measure which features actually drive purchase.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #causal-inference #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor here is fighting to draw a line between free and paid that customers accept and the community tolerates — and whoever can locate that line from evidence takes the model, because it is currently redrawn every two years by argument.

## The Problem
A vendor has fourteen commercial features. Three are the reason most customers bought. Four are used by almost nobody and are held commercial because they were commercial when they shipped. Two are used constantly by the community's most sophisticated operators, who have built their own equivalents rather than paying, and are therefore generating community effort against the vendor rather than revenue. Nobody knows which is which. The next boundary decision will be made by a leadership team reasoning about what feels enterprise, and the evidence — usage among paying customers, purchase attribution, and what community users built instead — is obtainable and uncollected.

## Why Nobody Has Built This
Feature-level usage among paying customers is straightforward to collect and is frequently not, because the product analytics discipline arrived late to infrastructure software. Purchase attribution requires asking at the moment of conversion, which is a sales process change nobody has made. What community users built instead is visible in public repositories and issue discussions and has never been assembled. And the boundary is treated as a strategic judgement where evidence is one input among several, which has become a reason to have no evidence at all.

## What to Build
Locate the boundary from evidence rather than from argument. Measure feature usage among paying customers, which immediately separates the features that justify the subscription from those that occupy space in a comparison table. Attribute purchase to features by asking at conversion and by observing what changed in the customer's usage after it, which are both obtainable and neither is collected. Assess the customer's alternative for each commercial feature — what they would do without it, how hard that is, whether an open equivalent exists — since willingness to pay is determined by the alternative and not by the feature's merit, and this is the variable the current reasoning omits. Watch for community reimplementation continuously, since a paid feature being rebuilt in the open is the model's characteristic failure and is visible in public repositories long before it matters. Estimate unlicensed commercial use, which in an open codebase is soft-enforced and is a real number nobody has. Model the boundary move before making it: which customers would be affected, what the community reaction has been to comparable moves, what the revenue effect would be. And evaluate afterwards, since every previous move was an experiment that was never read.

## Target Customer
Open-source company leadership and product management, and the entitlement and licensing vendors serving them.

## Impact If Built
The boundary is the product in this model and is placed by intuition, while the determining variable — how hard the customer's alternative is — is never assessed. Watching for community reimplementation is the early warning for the model's characteristic failure and is entirely public.
