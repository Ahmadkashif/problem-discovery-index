# The Reported Wins Do Not Add Up and Nobody Checks

**Industry:** [[conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** High Impact
**One-liner:** A year of reported test uplifts, if real, would have doubled the conversion rate, and the conversion rate did not double — and the industry has never made that comparison a standard part of its reporting.
**Tags:** #hypothesis-testing #confidence-intervals #bayesian-inference #causal-inference #monte-carlo-methods #evaluation-metrics #probability-distributions #revenue-impact

## The Problem
A conversion optimisation programme runs tests, declares winners, implements them and reports the uplift each was measured at. Over a year a reasonably active programme reports a substantial cumulative figure. The site's actual conversion rate over the same period moved by much less, and frequently not at all.

The gap has identifiable causes, and every one of them is standard practice.

Underpowered tests are the largest. Most pages do not receive enough traffic to detect the effect sizes typically claimed — a one or two percent relative change requires sample sizes far beyond what a mid-traffic page produces in a reasonable window. Tests run anyway, and an underpowered test that reaches significance has, by construction, overestimated the effect; the winner's curse means the reported uplift is systematically inflated even when the direction is right.

Continuous monitoring with early stopping is the second. Platforms display significance in real time and practitioners check daily, stopping when the result looks good. Repeatedly testing a hypothesis until it passes inflates the false positive rate dramatically, and the stopping decision is correlated with favourable noise. Sequential testing methods exist that make continuous monitoring valid, and several platforms now offer them, and a great deal of the industry still peeks at fixed-horizon tests.

Post-hoc segmentation follows. A flat test is sliced by device, browser, traffic source and new-versus-returning until a segment shows significance, and that segment becomes the finding. With enough segments something is always significant.

And regression to the mean does the rest: a test triggered because a metric looked unusually bad will show improvement regardless of the change.

Nobody validates because validation is not part of the deliverable. The client receives the uplift number and is satisfied; the firm's case studies are built from those numbers; and the annual comparison that would expose the gap is nobody's job.

## Why It's Unsolved
The commercial structure punishes rigour. A firm that reports fewer, smaller, honestly-qualified wins loses pitches to one that reports frequent large ones, and the buyer has no way to distinguish them. This is a market where the accurate supplier is at a disadvantage, which is a stable and corrosive equilibrium.

Statistical training is genuinely uneven in the field. Many practitioners came through marketing or design and use platforms that present significance as a green tick, and the platforms have historically encouraged exactly the behaviours that break the inference. Bayesian reporting has made this worse in practice: probability-to-beat-baseline is frequently presented as licensing continuous monitoring and early stopping in a way the underlying method does not support without careful specification.

There is a real capacity constraint too. A properly powered test on a mid-traffic page may need to run for months, which exceeds the attention span of most programmes and the duration of most contracts, and a firm that ran only adequately powered tests would deliver very few results.

And the honest version has an uncomfortable implication: for many sites, the answer is that conversion optimisation at the level of button copy and layout variants cannot be measured reliably at all, and the effort should go to changes large enough to detect.

## What a Solution Looks Like
Run a permanent holdback. A randomised fraction of traffic that never receives any implemented winner, maintained across the year, gives the direct comparison: the accumulated actual effect of the programme against the sum of its reported uplifts. It costs a small amount of conversion and it is the single most valuable thing any firm in this industry could do. It requires no new technique and could start tomorrow.

Power tests honestly and decline the ones that cannot work. A minimum detectable effect computed before launch, stated in the test plan, and used to refuse tests whose traffic cannot support them, redirects capacity from decoration to changes big enough to see. That is a smaller programme and a real one.

Adopt sequential methods properly. If continuous monitoring is desired — and it is operationally reasonable — use methods designed for it, with the stopping rule fixed in advance. Several platforms now support this and the practice has not followed the tooling.

Pre-register segments. Segments of interest declared before the test runs are hypotheses; segments found after are noise. This is a documentation discipline rather than a technique.

Report shrunken estimates. Correcting for the winner's curse means reporting a smaller uplift than the raw measurement, which is both more accurate and commercially awkward, and it is the difference between a number that predicts and a number that flatters.

## Impact If Solved
This determines whether an entire discipline is producing value or reporting it. A holdback answers the question within a year for any firm willing to ask, honest power analysis redirects capacity toward changes that can actually be detected, and correctly reported estimates would make the industry's claims predictive rather than decorative. The firm that does this first competes on evidence in a market where every competitor's case studies are identical and unverifiable — which is a durable position precisely because it is uncomfortable to copy.
