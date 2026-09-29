# Credited With Sales That Would Have Happened Anyway

**Niche:** [[niches/programmatic-ad-platforms/incrementality-and-budget-allocation/profile|Incrementality & Budget Allocation]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The channel credited with the most sales is frequently the one best positioned to observe sales that were going to happen, and the budget follows the credit.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #bayesian-inference #evaluation-metrics #revenue-impact #time-series-forecasting #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to tell an advertiser what their spend actually caused rather than what it was credited with — and whoever does that decides where the category's budget goes.

## The Problem
A retargeting campaign shows advertisements to people who have already visited the site and are already likely to buy. It is credited with an enormous share of conversions, so it receives more budget, so it shows more advertisements to people already intending to purchase, so it is credited with more. Every attribution model in common use rewards proximity to the purchase rather than causation of it. When advertisers run a proper holdout, the incremental contribution is frequently a fraction of the attributed one — and yet the next quarter's budget is set from the attribution report, because that is what arrives monthly and the experiment does not arrive at all.

## Why Nobody Has Built This
Measuring incrementality reduces the measured value of the channels doing the measuring, which is an alignment problem so direct it explains almost everything about this niche's state. Experiments cost reach and are treated as spend forgone rather than as information bought. Geo and holdout designs require coordination across teams that nobody owns. And attribution reports arrive automatically while experiments must be commissioned.

## What to Build
Make causal measurement continuous rather than occasional. Build always-on experimentation into the buying itself — holdouts, geo splits and staggered rollouts running permanently as a small share of spend — which is the core and converts incrementality from a project into a stream; the cost is small and known while the current cost of misallocation is large and unknown. Design the experiments properly with power analysis up front, since most industry lift studies are underpowered and produce a number that is indistinguishable from noise and is then acted on. Combine experiments with observational modelling, using the experiments to calibrate the model so allocation can be updated between experiments rather than only during them. Run mix modelling at a cadence that can inform decisions, since an annual model describes a year that has already been allocated. Reconcile the three views — attribution, experiment and mix model — explicitly, because they will disagree and an unreconciled disagreement means the advertiser simply picks the flattering one. Allocate budget from the causal estimates with uncertainty carried through, which is the deliverable and is what the whole apparatus is for. Measure saturation and diminishing returns per channel, since the marginal dollar's return is the actual allocation question and average return cannot answer it. Keep the measurement independent of the parties being measured, which is the fix note's subject. Handle cross-channel interference, as a holdout in one channel is contaminated by another and naive designs produce biased answers. And report the cost of the experimentation programme against the reallocation it produced, because that ratio is what sustains it.

## Target Customer
Advertiser measurement and finance functions, independent measurement vendors, and the agencies whose recommendations currently rest on attribution reports.

## Impact If Built
Attribution rewards proximity to the purchase rather than causation of it, and the budget follows the credit. Always-on experimentation at a small known cost replaces an unknown large cost of misallocation, with observational models calibrated against the experiments between runs.
