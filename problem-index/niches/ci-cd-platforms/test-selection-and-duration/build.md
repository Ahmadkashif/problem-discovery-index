# Everyone Runs Everything Because Nobody Has the Evidence

**Niche:** [[niches/ci-cd-platforms/test-selection-and-duration/profile|Test Selection & Pipeline Duration]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Parallelism, caching and test impact analysis all exist as products, and most organisations still run every test on every change because deciding what to skip requires evidence nobody has assembled.
**Tags:** #graph-theory #gradient-boosting #logistic-regression #evaluation-metrics #confidence-intervals #cross-validation #hypothesis-testing #automation
**Contested on:** Every serious competitor here is fighting to run only the tests a change could plausibly break, with evidence that nothing was missed — and whoever does that takes the platform account, because everyone runs everything and nobody has the evidence to stop.

## The Problem
A pipeline runs a forty-minute test suite on every change. A platform engineer proposes running only the affected subset. The objection is immediate and correct: if the selection is wrong, a defect ships, and nobody can quantify how likely that is. The proposal dies. The suite grows. The same conversation happens the following year with a longer suite. Meanwhile the platform holds every test execution for every change across years, which contains the exact answer — for changes of this shape, how often did a test outside the selected set fail.

## Why Nobody Has Built This
Test impact analysis is sold on its mechanism — relate changes to tests via coverage — rather than on its safety evidence, and coverage instrumentation is impractical in several common stacks, which caps adoption. The counterfactual measurement that would settle the objection has not occurred to anyone as a product: it requires running the full suite while computing what the selection would have been, and comparing, which is an ordinary shadow-mode evaluation and is exactly how a cautious organisation could be persuaded. And the cost of the status quo is engineer waiting time, which no budget records, so the status quo is never under pressure.

## What to Build
Lead with the evidence rather than the mechanism. Run the selection in shadow mode first: compute what would have been skipped on every change while continuing to run everything, and report how often a skipped test would have failed — which is the number that decides the argument and takes weeks of observation rather than a leap of faith. Build the selection from the relationships that are actually available: change-to-test associations from historical co-failure, dependency graph reachability where a build system provides it, file and module proximity, and coverage where it is obtainable — because relying on coverage alone is what has limited adoption. Report the operating point explicitly as a trade-off: this much duration saved at this estimated miss rate, with the confidence interval, so the organisation chooses its own tolerance rather than accepting a vendor's. Keep a safety net — the full suite on a schedule and before release — which makes an occasional miss recoverable and is what makes the whole proposal acceptable. Attribute the marginal value of each pipeline step from its history: how often has this step ever failed, and when it failed did anything change, which identifies the steps that could be removed entirely. And monitor duration growth so accumulation is visible as it happens.

## Target Customer
Platform engineering teams with long pipelines, CI vendors, and the build system vendors whose dependency graphs are the strongest available selection signal.

## Impact If Built
The capability exists and adoption is blocked by an unanswered safety question that the execution history answers directly. Shadow-mode evaluation produces the evidence in weeks, and a stated operating point lets each organisation choose a tolerance rather than trusting a claim.
