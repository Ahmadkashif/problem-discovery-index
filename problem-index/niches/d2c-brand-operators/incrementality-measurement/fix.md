# Attribution Fitted to the Platform's Own Claims

**Niche:** [[niches/d2c-brand-operators/incrementality-measurement/profile|Incrementality Measurement]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Attribution tools reconcile numbers reported by the advertising platforms, which means they are modelling the sellers' claims rather than the brand's outcomes, and the output inherits the bias it was bought to remove.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #revenue-impact #quick-win #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to establish what a marketing dollar actually caused rather than what each channel claims — and whoever does that takes the account, because every budget decision in the category currently rests on numbers the people making them do not believe.

## The Problem
A brand buys an attribution tool to fix the disagreement between channels. The tool ingests platform-reported conversions, applies a model, and produces a tidier allocation. The inputs are still the claims of parties selling the advertising, including modelled conversions the platforms estimate using their own methods and do not fully disclose. The output looks authoritative, is presented in a dashboard, and is a smoothed version of the same bias. The brand now believes a number more than it did before, which is the opposite of the improvement they paid for.

## Why It's Still Broken
Platform-reported data is the easiest input to obtain and the only one available at the granularity dashboards want. Fitting to the brand's own orders requires joining marketing data to order data, which many brands have not done. A tool that produced wide intervals and fewer certainties would be a harder sale than one producing a clean allocation. And the customer cannot evaluate the method, so they evaluate the interface.

## What a Fix Looks Like
Anchor everything to the brand's own outcomes. Fit to the brand's order data as the outcome variable, since that is the ground truth the brand owns and the platforms do not — making this the anchor is the fix, and everything else follows from it. Treat platform-reported conversions as an input feature rather than as a target, so their bias is estimated rather than inherited. Reconcile at the total level first and report the gap between claimed conversions and actual orders as a standing number, which is one arithmetic step and is the most informative single figure a brand can look at. Validate the model against holdout experiments and report the validation, since a model that has never been checked against a causal estimate is a hypothesis. Report uncertainty on every channel's contribution, because the current point estimates imply a precision that the data cannot support. Disclose the method, since a proprietary attribution model is asking the customer to substitute one unverifiable claim for another. Show what changes under different reasonable assumptions, so a brand can see whether their decision is robust to the model choice. And separate the reporting product from the measurement product, because reconciling platform numbers for operational monitoring is legitimate and calling it incrementality is not.

## Who Feels the Pain
Brands paying for a tool that launders the bias it was bought to remove; growth leads defending allocations built on it; and the vendors doing genuine causal work who compete against a cleaner-looking dashboard.

## Impact If Fixed
Fitting to the brand's own orders rather than to platform claims is the anchor, and the gap between total claimed conversions and actual orders is one arithmetic step and the most informative number available. Validating against holdout experiments is what separates a measurement from a hypothesis.
