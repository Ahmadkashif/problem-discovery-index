# Condition Adjustment Is the Largest Number and the Least Documented

**Niche:** [[niches/auto-body-shops/total-loss-valuation-providers/profile|Total Loss Valuation Providers]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Fix (Pain Point)
**One-liner:** The condition adjustment routinely moves a settlement by thousands of dollars, rests on an adjuster's judgment recorded as a single category, and has no evidentiary basis anyone can retrieve.
**Tags:** #cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #gradient-boosting #confidence-intervals #compliance #worker-facing #data-integration

## The Problem
Comparable selection and options adjustments are mechanical and defensible. The condition adjustment is neither. Someone assesses the vehicle's pre-loss condition against a scale — a small number of coarse categories — and that single choice can swing the settlement by thousands of dollars. The assessment is made under time pressure, frequently on a damaged vehicle where pre-loss condition must be inferred, sometimes from photographs, and it is recorded as a category with no supporting evidence attached. Two adjusters looking at the same vehicle produce different categories at a rate nobody measures, because measuring it would require a ground truth the process never captures. When the number is challenged, the file contains a word.

## Why It's Still Broken
Pre-loss condition is genuinely hard to establish after a collision, and the coarse scale was a reasonable simplification when assessments were made in person by experienced adjusters. What changed is the volume and the remoteness — assessments are now often made from photographs by staff handling high case loads — while the scale and the documentation practice did not change with it. There is also a structural disincentive: better documentation of condition creates a record that can be contested, and the current practice is contestable only in the abstract because there is nothing to contest. The result is that the least defensible input carries the most weight.

## What a Fix Looks Like
Evidence attached to the judgment. Photographs already collected in the claim are analyzed for the observable condition indicators the scale actually depends on — paint and panel condition, wear on interior surfaces, tyre condition, glass, undamaged-area corrosion — producing a structured assessment of what is visible, with explicit uncertainty where the damage obscures the answer. That assessment is presented to the adjuster as a starting point with the supporting images cited, not as a determination: the adjuster confirms or overrides, and the override is recorded with a reason. Service and title history, where obtainable, joins as corroborating evidence. Over time this produces something the segment has never had — a measurable distribution of condition assessments against observable evidence, which makes inter-assessor variance visible and makes the scale itself testable. Where a vehicle is too damaged to assess, the system says so, which is more defensible than a confident category assigned to an unknowable state.

## Who Feels the Pain
Adjusters making a high-stakes judgment with no support and no feedback; policyholders whose settlement turns on an undocumented category; the compliance function defending an input with no evidentiary basis; and the valuation provider, whose methodology is otherwise rigorous and is judged on its weakest link.

## Impact If Fixed
Addresses the single largest source of unexplained variance in total loss settlements and the most common substantive ground for challenge. Documented condition assessment converts the most disputed input into the best-evidenced one, which reduces revision volume and — more importantly in a segment under regulatory pressure — makes the methodology defensible end to end rather than rigorous everywhere except the number that matters most.
