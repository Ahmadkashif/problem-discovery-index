# Flaky Tests & Signal Quality

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to make a pipeline failure mean something again — and whoever does that takes the platform account, because once engineers learn to re-run rather than investigate, every other capability in the category is built on a signal nobody trusts.

## Profile
**Market Size:** ~$620M US attributable to test reliability and signal quality
**Share of Parent Industry:** ~16% of category revenue
**Digital Adoption:** Low — basic detection features exist and almost nothing acts on them
**Target Buyer:** Platform engineering and engineering leadership
**Automation Potential:** Very High — every execution result is recorded and joined to the change

## What Makes This a Distinct Niche
A flaky test fails intermittently for reasons unrelated to the change. The first consequence is small: somebody re-runs the pipeline and it passes. The second consequence is enormous: the organisation learns that a red pipeline is not necessarily a real failure, and re-running becomes the default response to any failure. At that point the pipeline has stopped being a signal — real defects are re-run past, the discipline that made continuous integration valuable is gone, and no amount of speed or coverage compensates. This is the category's defining problem, it degrades continuously rather than breaking visibly, and the platforms hold the complete evidence: every test execution for every change, with the code that changed, the environment it ran in and whether the change eventually shipped or was reverted.

## Current Tools & Gaps
Flaky test detection in several platforms at a basic level — usually a rerun-passed counter — test result dashboards, and quarantine mechanisms. The gaps: detection identifies flakiness and stops there, so the list grows and nobody fixes anything; flakiness is not attributed to a cause, and the causes are a small enumerable set — ordering dependence, shared state, timing, resource contention, external dependencies — each with a different remedy; quarantine has no exit, so quarantined tests accumulate permanently and coverage silently erodes; the cost of flakiness is unmeasured, so it never competes for engineering time; and nobody measures the behavioural consequence, which is the proportion of failures re-run without investigation.

## Problems
- [[niches/ci-cd-platforms/flaky-tests-signal-quality/build|🔨 Build: The Habit of Re-Running]]
- [[niches/ci-cd-platforms/flaky-tests-signal-quality/buy|🛒 Buy: Flakiness Research the Platforms Have Not Read]]
- [[niches/ci-cd-platforms/flaky-tests-signal-quality/fix|🔧 Fix: Quarantine With No Way Out]]
