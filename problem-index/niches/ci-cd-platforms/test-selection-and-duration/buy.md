# Test Impact Analysis Without Coverage Instrumentation

**Niche:** [[niches/ci-cd-platforms/test-selection-and-duration/profile|Test Selection & Pipeline Duration]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Regression test selection is a mature research area whose commercial implementations depend on coverage instrumentation, which a large share of stacks cannot practically provide.
**Tags:** #graph-theory #gradient-boosting #logistic-regression #k-nearest-neighbors #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to run only the tests a change could plausibly break, with evidence that nothing was missed — and whoever does that takes the platform account, because everyone runs everything and nobody has the evidence to stop.

## The Problem
Regression test selection has decades of research: safe selection based on control flow and coverage, unsafe but effective heuristics, and learned approaches. The commercial products implement the coverage-based version, which requires instrumenting execution to record which tests touch which code. In several widely used stacks that instrumentation is slow, unreliable or unavailable, which is why adoption of a genuinely valuable capability remains low.

## What Already Exists
Regression test selection research with safety proofs for the coverage-based variants; test impact analysis products; build system dependency graphs, which supply a coarse but reliable relationship; historical failure association methods; and the machine learning literature on test failure prediction from change features. All published, with open implementations for several components.

## The Customization Gap
The adaptation is to stacks where coverage is unavailable. It requires: (1) selection from historical co-occurrence — which tests have failed on changes to which files, learned over the execution record — which needs no instrumentation at all and is available to every platform immediately, and is the practical route to broad adoption; (2) dependency graph reachability where a build system provides it, which is coarse and sound and complements the historical signal well; (3) an explicit, measured miss rate rather than a safety claim, since these heuristic approaches are not provably safe and pretending otherwise is both wrong and unnecessary — a measured miss rate with a safety net is a better product than an unprovable guarantee; (4) cold-start handling for new and rarely-changed code, where the historical signal is absent and the correct behaviour is to run more rather than less; and (5) continuous re-evaluation, because the association between changes and failures drifts as the codebase changes.

## Target Customer
CI platform vendors, test tooling vendors, build system vendors, and large platform teams.

## Impact If Solved
The research is mature and adoption is capped by an instrumentation requirement rather than by the idea. Historical co-occurrence selection needs no instrumentation and is available to every platform from data it already stores, which changes who can adopt this from a minority to everyone.
