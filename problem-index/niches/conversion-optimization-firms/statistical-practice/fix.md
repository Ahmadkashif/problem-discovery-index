# The Test That Was Never Powered

**Niche:** [[niches/conversion-optimization-firms/statistical-practice/profile|Experiment Design & Statistical Practice]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The page gets four hundred visitors a week and the test is looking for a two percent improvement.
**Tags:** #quick-win #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #probability-distributions #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to run experiments whose conclusions their data actually supports, against tooling that makes the opposite easy — and whoever makes good practice the fast path takes the account.

## The Problem
A large share of tests could never have produced a usable result. The page's traffic and baseline conversion rate determine the smallest effect the test can detect, and for many pages that is far larger than any realistic improvement. The test runs for a month, reaches no conclusion or reaches a spurious one, and consumes capacity that could have gone to a page where an effect was detectable. The calculation that would have shown this takes seconds.

## Why It's Still Broken
The calculation is not in the workflow — a platform that lets a test launch without asking what effect it could detect will run tests that cannot detect anything, because nothing in the process poses the question. Practitioners may not know the calculation. The page was easy to test. And a test that ran feels like work done.

## What a Fix Looks Like
Calculate the detectable effect before launching, every time. Compute the minimum detectable effect from traffic, baseline rate and duration before any test starts, which is the fix and takes seconds with a standard calculator. Refuse to launch tests whose detectable effect exceeds anything plausible, which frees capacity immediately. Report the minimum detectable effect alongside every result, so a null is interpretable rather than ambiguous. Combine low-traffic pages into a single test where the change is the same, which is how a detectable effect becomes possible. Prioritise pages by traffic, since detectability is mostly a traffic question. Extend duration deliberately where the effect matters and the traffic is thin, rather than running a short underpowered test. Test bigger changes on low-traffic pages, since only large effects are detectable there. Report how many tests in the programme were underpowered, which is usually a striking number. Educate clients that a page cannot be tested meaningfully, which is a real finding rather than a failure. And build the calculation into the intake so it cannot be skipped.

## Who Feels the Pain
Clients paying for tests that could not have concluded; strategists reporting inconclusive results as learnings; the test capacity, consumed by pages where nothing was detectable; and the reported wins, which on those pages are noise.

## Impact If Fixed
A platform that lets a test launch without asking what effect it could detect will run tests that cannot detect anything. A minimum detectable effect calculation at intake takes seconds and frees a large share of the capacity.
