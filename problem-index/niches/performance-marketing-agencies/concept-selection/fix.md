# The Test That Was Never Powered

**Niche:** [[niches/performance-marketing-agencies/concept-selection/profile|Concept Selection & Prediction]]
**Industry:** [[industries/performance-marketing-agencies|Performance Marketing Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Four creatives ran for a week on a small budget, one produced eleven conversions and three produced seven, and the agency declared a winner.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #monte-carlo-methods #quick-win #revenue-impact #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to know which concepts are worth producing before the money is spent — and whoever builds that prediction from a portfolio of creative and its measured performance owns the one advantage a platform cannot supply.

## The Problem
The creative test ran for seven days across four variants on an account spending modestly. The winning variant produced eleven conversions and the others seven, eight and six. The agency reports a winner, scales it, and pauses the rest. The difference is entirely consistent with chance; at these volumes the test could not have detected anything smaller than an enormous effect, and the observed differences are noise. This is the standard creative testing practice across most of the category's accounts, it is repeated weekly, and the decisions it produces are approximately random while being reported as learning.

## Why It's Still Broken
Nobody runs a power calculation, so the impossibility of the test is never surfaced — the calculation takes a minute and would stop most tests being run, which is precisely why it is not run. Platform interfaces declare winners without qualification, lending authority to noise. Reporting a result each week is what the client expects. And the losing variants are paused, so the error is never discovered.

## What a Fix Looks Like
Say what the test can detect. Run a power calculation before every test and state the minimum detectable effect, which is the fix, takes seconds, and immediately reveals that most small-account creative tests cannot detect anything useful. Report differences with intervals rather than declaring winners, since a winner label on overlapping intervals is the specific error. Aggregate at the concept level across variants and across time to reach usable sample sizes, which is the only route to real learning on small accounts and is why concept-level tagging matters. Pool across clients in the same category, which is the portfolio argument and is what makes testing viable for accounts that cannot test alone. Run fewer, longer tests with fewer variants, because four variants on a small budget guarantees an underpowered test and two would at least be answerable. Use sequential methods with valid stopping rules rather than checking daily and stopping when something looks good, which is the other common error and inflates false findings substantially. Report honestly when a test was inconclusive, which is uncomfortable weekly and correct. Reserve the decisive tests for the accounts with the volume to support them. Educate clients that a weekly winner is not a finding, since their expectation is half of what sustains the practice. And track whether scaled winners actually outperformed, because that retrospective check is what would end the practice fastest.

## Who Feels the Pain
Clients whose creative decisions are noise presented as learning; creative teams whose good concepts are paused at random; and agencies whose testing practice produces no accumulated knowledge.

## Impact If Fixed
The power calculation takes seconds and would stop most of these tests being run, which is why nobody runs it. Stating the minimum detectable effect and aggregating at concept level across time is what turns a weekly coin flip into learning.
