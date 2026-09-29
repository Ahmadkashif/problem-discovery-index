# Attributing the Subscriber to the Title

**Niche:** [[niches/streaming-video-platforms/title-causal-valuation/profile|Title Causal Valuation]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Millions of subscribers watched it and the question is which of them would have left without it.
**Tags:** #causal-inference #survival-analysis #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #gradient-boosting #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to attribute subscribers acquired and retained to the titles that caused them — and whoever produces a number a chief financial officer will defend changes what the industry spends billions on.

## The Problem
The counterfactual is the whole problem. A title watched by ten million subscribers may have retained none of them, because they had six other reasons to stay. A title watched by half a million may have retained most of its audience, because it was the only thing they came for. Distinguishing those requires knowing what each subscriber would have done without it, and the platform has a complete record of what they did do and no record of the alternative.

## Why Nobody Has Built This
Observational causal inference at this scale requires methods the analytics organisation is not staffed for, so the problem was reduced to a consumption metric — a question whose honest answer requires an experiment gets replaced by one whose answer is already in the dashboard. Withholding content from subscribers to create a control feels commercially unacceptable. The confounds are severe because promotion, recommendation and release all covary with the title. And the answer would be unwelcome.

## What to Build
Construct counterfactuals from what varies. Exploit staggered regional and window releases as natural experiments, which is the core — the same title available to comparable populations at different times is the closest thing to a randomised trial the industry produces and it happens constantly. Use licensing windows opening and closing, since a title leaving the catalogue is a clean withdrawal experiment and the churn that follows is measurable. Analyse catalogue removals retrospectively, as they are the strongest evidence available and are treated as operational events. Run deliberate experiments in promotion and availability where possible, because randomised promotion is entirely acceptable commercially and settles far more than observational work. Model retention contribution over the subscriber's tenure rather than at the viewing moment, since a title's effect persists and decays. Build matched comparison groups from viewers with similar histories, which is the standard observational remedy and is not being applied. Separate acquisition from retention contribution, as they are different questions with different evidence. Estimate segment-level value, because the narrow loyal audience is where the current metric fails worst. Report with intervals and state the design's limits, since credibility is everything for a number this consequential. And publish the method internally so it can be criticised, as an unchallengeable number will not be believed.

## Target Customer
Data and finance leadership, content leadership, studios negotiating licensing, and investors assessing content spend.

## Impact If Built
A question whose honest answer requires an experiment gets replaced by one whose answer is already in the dashboard. Staggered releases and catalogue removals are experiments the industry runs constantly and analyses never.
