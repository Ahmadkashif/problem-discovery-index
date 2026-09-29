# A Number With No Uncertainty Attached

**Niche:** [[niches/ai-model-evaluation-firms/evaluation-platforms/profile|Evaluation Platforms]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Evaluation results are reported as single percentages on suites of a few hundred stochastic items, where the sampling error alone is wider than most of the differences being acted on.
**Tags:** #confidence-intervals #hypothesis-testing #descriptive-statistics #evaluation-metrics #monte-carlo-methods #probability-distributions #quick-win #cross-validation
**Contested on:** Not terminal — the contest differs by who is being evaluated and why, and the decomposition is recorded in the profile.

## The Problem
A suite of two hundred items returns 81.5 percent. The previous run returned 79.0. The team ships the change. On two hundred items the standard error is around three percentage points before accounting for the model's own sampling variability or the grader's inconsistency, both of which add more. The observed difference is well inside the noise, and the report displayed it to one decimal place with an upward arrow. Every team using these platforms makes this comparison several times a week and the tooling actively encourages it.

## Why It's Still Broken
A single number with an arrow is what a dashboard wants and what a stakeholder asks for. Reporting intervals makes most week-to-week movement look like nothing, which is true and is commercially unwelcome. Computing the uncertainty properly means accounting for three separate sources — item sampling, model stochasticity, grader inconsistency — and nobody has packaged that. And the convention of bare percentages is universal enough that the first vendor to break it looks worse rather than more honest.

## What a Fix Looks Like
Report the interval, always. Compute and display a confidence interval on every score, accounting for item sampling at minimum, which is elementary statistics, costs nothing, and would prevent most of the wrong decisions being made on these platforms today. Estimate model stochasticity by repeating a sample of items at the same settings, which is cheap and quantifies a source everyone knows exists and nobody measures. Estimate grader inconsistency by re-grading a subset, since an automated judge is non-deterministic and its disagreement with itself sets a floor on the whole measurement. Use paired comparison on the same items when comparing two versions, which removes item sampling error entirely and is dramatically more sensitive than comparing two independent percentages — this is the single best available improvement for regression testing and is almost never implemented. Report the minimum detectable difference for a suite, so a team knows before they start that their two hundred items cannot resolve a two-point change. Recommend a suite size for the difference the team cares about. And stop displaying arrows on differences inside the interval, which is a presentation fix that removes the false signal at its source.

## Who Feels the Pain
Teams shipping changes that did nothing and reverting changes that helped; evaluation engineers asked to explain movement that is noise; and the buyers comparing vendors on differences that no suite of that size could resolve.

## Impact If Fixed
Paired comparison on identical items removes item sampling error entirely and is far more sensitive than comparing two percentages — the single largest available improvement, and almost nobody does it. Reporting the minimum detectable difference tells a team up front what their suite can and cannot resolve.
