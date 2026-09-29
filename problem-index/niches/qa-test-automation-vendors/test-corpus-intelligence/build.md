# A Labelled Corpus, Used to Render Pass and Fail

**Niche:** [[niches/qa-test-automation-vendors/test-corpus-intelligence/profile|Test Corpus Intelligence]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These vendors observe tests, failures, repairs and the application changes that caused them across enormous numbers of applications, and the corpus that would distinguish a cosmetic change from a regression is used to render pass and fail.
**Tags:** #gradient-boosting #graph-theory #k-means-clustering #bert #evaluation-metrics #confidence-intervals #cross-validation #transfer-learning
**Contested on:** Every serious competitor that gets here is fighting to use a fleet-wide record of tests, failures, repairs and the changes that caused them — and whoever does that can distinguish a cosmetic change from a regression, which is the capability the whole category is missing.

## The Problem
The category's central unsolved question is whether a test that broke did so because the application's presentation changed or because its behaviour did. Within one organisation there are perhaps a few hundred labelled examples — breakages whose disposition is known — which is not many for a subtle classification. Across a vendor's fleet there are millions, spanning the same frameworks, the same component libraries and the same change patterns, each with a recorded outcome: repaired and passed, repaired and later found wrong, or correctly failed. The vendors hold the labelled data for the problem their product cannot solve and use it to display a red or green icon.

## Why Nobody Has Built This
Cross-customer analysis has not been articulated as a governed capability by anyone in the category, so it is avoided — the same pattern as every other corpus opportunity in this vault, with the difference that here the useful representation is structural and contains no customer content at all, which makes the governance story easier than the vendors seem to assume. Repair outcomes, which are the most valuable label, are not collected: a self-healed test that passes is recorded as passing, and whether the heal was correct is never established. And the analytical investment has no immediate demonstrable output, which loses to feature work.

## What to Build
Assemble the corpus and learn the classification the category needs. Represent changes and tests structurally — change type, element and attribute deltas, framework and component library, test binding strategy, assertion type — with no application content, which is sufficient for the classification and makes the position defensible publicly. Collect repair outcomes deliberately, which is the key label and requires only asking: when a healed test later fails, or when a defect escapes through a healed test, that is a negative example, and instrumenting for it costs little. Learn the change-to-breakage relationship across the fleet, which is the model the impact niche needs and is far better estimated from millions of examples than from one organisation's few hundred. Learn framework-specific flakiness patterns, since the same framework produces the same flaky behaviours everywhere and each customer currently rediscovers them. Benchmark suite health — maintenance burden, flakiness rate, effectiveness — against comparable organisations, which is a question customers ask constantly. Feed all of it back into the products in this industry's other niches, since they are all consumers of the same model. And design the governance in: structure only, aggregation thresholds, opt-in, and a public statement.

## Target Customer
Test automation vendors, primarily; and quality engineering functions, who would buy the benchmarking and receive the improved classification.

## Impact If Built
The category's central classification requires labelled examples that no single organisation has enough of and that the vendors have in millions. Collecting repair outcomes is the missing label and is cheap to instrument, and the structural representation makes the whole thing governable.
