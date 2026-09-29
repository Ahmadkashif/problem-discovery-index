# Pipeline Duration and Test Selection

**Industry:** [[ci-cd-platforms|CI/CD Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Parallelism, caching and test impact analysis all exist as products, and most organisations still run every test on every change because deciding what to skip requires evidence nobody has assembled.
**Tags:** #gradient-boosting #graph-theory #k-nearest-neighbors #feature-engineering #confidence-intervals #evaluation-metrics #optimization-fundamentals

## The Problem
Pipeline duration grows monotonically. Every team adds a step — a new test suite, a security scan, a lint stage, a build variant — and nobody removes one, because removing a check requires arguing that it is unnecessary and keeping it requires arguing nothing.

The consequence is a feedback loop measured in tens of minutes, sometimes hours. Engineers context-switch while waiting, return to a failure, fix, and wait again. The cost is enormous in aggregate and is paid in fragments of attention that appear in no budget.

The obvious remedy is to run only what the change could affect. Test impact analysis does exactly this, has existed for years, and is used by a small minority. The reason is trust: skipping a test that would have caught a regression is a visible, career-relevant failure, while running everything is defensible. Without evidence about how often selection would miss something, nobody adopts it.

The platform holds that evidence — every test result for every change, and whether each change was later reverted or produced an incident — and does not compute it.

## What Already Exists
Parallelism and matrix builds are standard. Caching for dependencies and build artefacts is available everywhere and configured by copying a template. Build systems like Bazel, Gradle, Nx and Turborepo provide genuine incremental builds and remote caching where adopted. Test impact analysis exists in a few commercial products. Test splitting by historical duration is a common feature.

## The Customisation Gap
Test-to-code relevance is learnable from history rather than requiring static analysis. Which tests have ever failed for changes touching which files is directly observable across thousands of changes, and it is a far more practical basis for selection than a call graph — particularly for integration tests, where static analysis is weakest and runtime is longest.

Confidence is the missing ingredient that would make adoption possible. A selection recommendation carrying a stated miss probability, backtested against the organisation's own history of regressions, is something a team can actually accept. Selection without a measured error rate is not.

Ordering is the cheaper win nobody takes. Running the tests most likely to fail for this change first surfaces failures in the first minute rather than the fortieth, which changes the developer's experience more than total duration does.

Cache effectiveness is unmeasured almost everywhere: hit rates, which steps benefit, and where a cache is costing more to maintain than it saves are all computable and rarely computed.

## Impact If Solved
Feedback loop duration determines how software gets written, and it grows by accretion because removal requires an argument. Learned test relevance with a backtested miss rate makes selection defensible for the first time, and failure-ordered execution improves the experience immediately at no risk.
