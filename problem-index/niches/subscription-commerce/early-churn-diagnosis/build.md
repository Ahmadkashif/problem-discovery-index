# A Monthly Rate Over a First-Cycle Problem

**Niche:** [[niches/subscription-commerce/early-churn-diagnosis/profile|Early Churn Diagnosis]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Most cancellations happen within the first three deliveries for specific, fixable reasons, and the industry reports a monthly churn rate and buys more acquisition.
**Tags:** #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing #causal-inference #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to know why the first three deliveries fail — and whoever does that takes the economics, because that is where nearly all the churn happens and the reasons are specific and fixable.

## The Problem
A company reports seven percent monthly churn and treats it as a rate to be improved with better emails. Decomposed by cycle, the picture is different: a large share cancel after delivery one, a further group after delivery two, and the customers who reach delivery four stay for a long time. Delivery one's cancellers mostly received something that did not match the impression the sign-up quiz gave them. Delivery two's mostly still had most of delivery one unused. Both are fixable in the product and in the operations. The monthly rate averages them together with the stable base and produces a number that suggests a marketing problem.

## Why Nobody Has Built This
The monthly rate is the convention, is what investors ask for, and is what the platforms report. Decomposing by cycle requires cohort analysis that the tooling offers and nobody sets up as a standing view. The fixes are product and operations changes owned by teams who do not hold the churn metric. And the acquisition response is available immediately while a product fix takes a quarter.

## What to Build
Diagnose the first cycles specifically. Report retention by delivery number rather than by month, which is a reframing available in every platform's data and immediately reveals that this is not a marketing problem — the front-loading is invisible in a monthly figure and obvious in a per-delivery one. Model cancellation probability per subscriber from the signals of the first cycles: what they were shown at sign-up against what they received, delivery condition and timing, whether they opened the account or engaged at all, whether they skipped, and consumption signals where available. Predict the cancellation before the cancel page, so the intervention is a product change or a proactive contact rather than a discount offered to somebody who has decided. Measure the expectation gap directly, comparing what the sign-up flow implied against what the first delivery contained, since that mismatch is the single most cited early reason and nobody quantifies it. Attribute early churn to causes — expectation, cadence, condition, value, friction — and report the mix, which tells the operator which team owns the fix. Instrument the first delivery experience specifically, since it is the moment the subscription is decided and is treated as a fulfilment event. Test fixes against retention with holdouts, which the category has the cohort structure to do easily. And report acquisition cost against retained subscribers rather than against sign-ups, since that is the number the whole model turns on.

## Target Customer
Subscription operators of every size, their investors, and the platform vendors whose cohort analytics are reported rather than acted on.

## Impact If Built
Per-delivery retention is available in every platform's data and shows immediately that this is a product problem rather than a marketing one. Measuring the gap between what sign-up implied and what arrived quantifies the most cited cancellation reason, which nobody currently does.
