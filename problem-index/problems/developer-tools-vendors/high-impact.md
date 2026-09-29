# Measuring Whether the Tool Actually Helped

**Industry:** [[developer-tools-vendors|Developer Tools Vendors]]
**Type:** High Impact
**One-liner:** The industry is committing enormous spend to coding assistants on the basis of demonstrations and enthusiasm, and neither vendors nor buyers can say what happened to throughput, defect rates or maintenance burden.
**Tags:** #causal-inference #hypothesis-testing #gradient-boosting #confidence-intervals #time-series-forecasting #evaluation-metrics #descriptive-statistics #revenue-impact

## The Problem
Developer tooling is sold on productivity. It always has been, and the claim has always been unverifiable, which was tolerable when the spend was a per-seat licence for an editor.

Coding assistants changed the stakes. Spend is now large, adoption is rapid, and the claimed effects are dramatic. Meanwhile the evidence is thin and contested: vendor studies measure completion acceptance and self-reported satisfaction, independent studies have found effects ranging from substantial improvement to none, and at least one careful randomised study found experienced developers were slower while believing they were faster. That last finding should be uncomfortable for everyone in the category and mostly has not been.

The measurement problem is genuine rather than lazy. Output in software is not countable — lines of code and commit counts are actively misleading, and optimising for them is famously destructive. DORA metrics measure delivery flow and are heavily influenced by everything other than tooling. Individual measurement is both statistically hopeless at typical volumes and organisationally toxic.

And the effects that matter most arrive latest. Code that was written faster and is harder to maintain shows up as defect rate and change failure rate months later, and as review burden immediately — a real cost that lands on colleagues rather than on the author, which means the person experiencing the benefit is not the person paying the price.

## Why It's Unsolved
Nobody selling has an incentive to measure honestly. A vendor that ran a rigorous trial and found a modest effect would have destroyed its own marketing, and a vendor that found a large one would have been accused of running its own study. The engineering analytics category exists precisely because the platforms would not answer the question, and it is small and treated with suspicion by developers for good reason.

Buyers have an incentive problem too. A CTO who has committed to a large rollout is not looking for evidence that it did nothing.

Attribution is genuinely hard. Teams change, priorities shift, headcount moves, and the counterfactual — what this team would have shipped without the tool — is unobservable. Software organisations also rarely have enough teams for a well-powered comparison, which is exactly why the vendor, with thousands of customers, is the only party who could do it properly.

And the measurement risks becoming surveillance. Any productivity instrumentation can be turned on individuals, which developers will resist, correctly. That constraint is real and it rules out the naive version.

## What a Solution Looks Like
Team-level measurement with proper design. Staged rollouts across teams create natural comparison groups, and a vendor deploying across thousands of organisations can construct genuine randomised or stepped-wedge evidence rather than before-and-after anecdotes.

Outcomes that matter rather than proxies for effort. Change failure rate, defect density in changed code, time from first commit to production, review cycles per change, and the rate at which code is revisited shortly after being written.

The maintenance dimension explicitly. Code written with assistance should be tracked for how much it is subsequently modified, how often it appears in incidents, and how much review it consumed. If the effect is to move work from authoring to reviewing, that is the finding, and it is currently invisible because nobody measures the reviewer's cost.

Individual measurement excluded architecturally rather than discouraged, because the alternative guarantees the data is gamed and the programme is rejected.

## Impact If Solved
The industry is making one of its largest tooling investments in decades on evidence that would not survive scrutiny in any other domain. A vendor able to state honestly what its tool does to delivery outcomes, with a defensible design, would own the buying conversation — and the answer would be worth knowing regardless of which way it comes out.
