# Validated Against a Bureau Score Rather Than an Outcome

**Niche:** [[niches/bnpl-providers/repayment-behaviour-intelligence/profile|Repayment Behaviour Intelligence]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The internal model is checked by seeing how well it agrees with a bureau score, on a population the bureau score describes badly, which measures conformity rather than accuracy.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #quick-win #causal-inference #compliance #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to establish what small-instalment repayment behaviour actually predicts about a person's capacity — and whoever answers that owns genuinely new empirical ground about a population the bureaus cannot describe.

## The Problem
A provider builds a model on thin-file consumers and validates it partly by checking how well its rankings agree with a bureau score. That is a reasonable-looking sanity check and it is measuring the wrong thing: the bureau score is a poor description of this population, which is the reason the provider exists, and agreement with it is therefore a measure of conformity to a benchmark known to be bad here. A model that disagrees with the bureau is treated as suspect when disagreement is precisely what a better model on this population would produce.

## Why It's Still Broken
The bureau score is the familiar external reference and validating against a recognised benchmark feels rigorous — the availability of a comparator determined what validation meant, and its unsuitability for this population is the one thing it is never checked against. Outcome-based validation at a six-week horizon requires a discipline the sector has not built. Regulators and partners recognise bureau scores, which gives the comparison institutional weight. And a model that disagrees is harder to defend internally.

## What a Fix Looks Like
Validate against what happened. Measure the model against realised repayment outcomes at the horizons that matter, which is the fix, is entirely feasible at a six-week product cycle, and is the only validation that means anything. Use bureau agreement as a descriptive comparison rather than as a validation criterion, since it is informative about how this population differs and is not a standard to meet. Report where the model disagrees with the bureau and who those people are, because that is the sector's most interesting finding about itself and is currently treated as a defect. Measure across the population including the thin-file segment specifically, since an aggregate figure will be dominated by the consumers the bureau does describe. Calibrate rather than only rank, because the affordability question needs a probability and not an ordering. Track performance over time, since a fast-growing sector's population shifts and a model validated at launch decays. Validate the affordability assessment separately from the credit risk model, as they answer different questions and are frequently conflated. Compare against a simple baseline, because a complex model that does not beat the provider's own repeat-customer flag should be known to. Publish the methodology at least internally, so the validation can be challenged. And report the model's accuracy on thin-file consumers as the headline, since that is the population the business exists to serve and the aggregate hides it.

## Who Feels the Pain
Thin-file consumers scored by a model validated against a benchmark that describes them badly; credit teams defending disagreement with a bureau; and a sector whose central claim is about a population it validates by conformity to the system that excluded them.

## Impact If Fixed
The availability of a bureau comparator determined what validation meant, and its unsuitability for this population is the one thing never checked. Validating against realised repayment at a six-week horizon is entirely feasible and is the only measure that means anything here.
