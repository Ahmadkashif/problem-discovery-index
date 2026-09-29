# The Lift Study Run by the Seller

**Niche:** [[niches/programmatic-ad-platforms/incrementality-and-budget-allocation/profile|Incrementality & Budget Allocation]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The platform selling the media designs the experiment, selects the holdout, analyses the result and reports the lift, and the advertiser is asked to plan against it.
**Tags:** #hypothesis-testing #causal-inference #confidence-intervals #evaluation-metrics #compliance #quick-win #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell an advertiser what their spend actually caused rather than what it was credited with — and whoever does that decides where the category's budget goes.

## The Problem
The platform offers a conversion lift study at no charge. The platform decides who is in the holdout, how long it runs, which conversions count, when to stop, and how to analyse it. It reports a strong positive lift. The advertiser has no access to the assignment, no ability to check the analysis, no view of whether other studies were run and discarded, and no way to reproduce the number. They plan a year's budget on it. This arrangement would be unacceptable in any other context where a measurement determines a purchase, and in advertising it is the normal way the central question is answered.

## Why It's Still Broken
Free studies from the seller are convenient and independent measurement is not, so the convenient one became standard practice. Advertisers mostly lack the statistical capacity to evaluate a design even when given one. The methodology is usually described as proprietary, which forecloses inspection. And a study showing no lift is simply not published, so the visible record is selected.

## What a Fix Looks Like
Separate the measurer from the seller. Hold the randomisation independently — by the advertiser or a third party — which is the fix and is the single structural change that makes every subsequent number credible; everything else is a partial remedy. Pre-register the design, the metric, the duration and the stopping rule before the study runs, since post hoc flexibility is how an honest procedure produces a flattering answer without anyone lying. Require raw assignment and outcome data so the analysis can be reproduced, which is the minimum the advertiser should demand and almost never does. Count every study run, including those not reported, because selective publication is the largest single distortion in the current record and is invisible by design. Use the advertiser's own conversion data rather than the platform's, since the seller's outcome definition tends to favour the seller. Apply a consistent method across platforms, as comparing one seller's lift methodology to another's compares nothing. Report a confidence interval and refuse to act on an underpowered result, which would disqualify a large share of current studies immediately. Validate against the advertiser's aggregate results, since a set of channel lifts that sums to more than the total business growth is arithmetically impossible and this check is rarely run. Build the capacity to evaluate designs in-house or through an independent party, because a right to inspect is worthless without the ability to. And publish an industry standard, since every advertiser negotiating this alone is how the current situation arose.

## Who Feels the Pain
Advertisers allocating budgets on numbers they cannot reproduce; honest platforms whose accurate measurement loses to a flattering one; and the whole category, whose credibility rests on measurements produced by the seller.

## Impact If Fixed
The seller designing, running, analysing and selectively publishing its own measurement is the normal way the central question is answered. Independent randomisation with a pre-registered design is the structural change, and counting unreported studies exposes the selection that makes the visible record meaningless.
