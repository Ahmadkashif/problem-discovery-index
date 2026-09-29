# The Ad Test That Won and the Revenue That Fell

**Niche:** [[niches/mobile-game-publishers/hybrid-monetisation-balance/profile|Hybrid Monetisation Balance]]
**Industry:** [[industries/mobile-game-publishers|Mobile Game Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** The ad placement test showed a clear lift, shipped, and total revenue per player was lower a month later.
**Tags:** #quick-win #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #revenue-impact #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to set the balance between advertising and in-app purchase when the two compete for the same player's attention and every test measures only one of them — and whoever measures both together takes the account.

## The Problem
A recurring and expensive pattern: an ad monetisation test measures ad revenue per daily active user over a fortnight, shows a clean lift, and ships. Purchase revenue drifts down, sessions shorten, and thirty-day retention falls by an amount that is individually small and collectively decisive. Nobody connects the two, because the test was closed and declared a win before the effects it caused had time to appear.

## Why It's Still Broken
The test's success metric excludes the channel it damages — an experiment whose objective omits the cost it imposes will reliably report a win while destroying value, and will do so repeatedly. Test windows are shorter than the effects. The two revenue streams sit in different reports. And the team that shipped it was measured on the number that went up.

## What a Fix Looks Like
Change what the test reports, before changing anything else. Report total revenue per player across both streams on every monetisation test, which is the fix and requires only joining two existing datasets. Extend the measurement window past the point where retention effects appear, since a fortnight is structurally too short. Include retention and session length as reported outcomes rather than as guardrails nobody reads. Break the result out by spending segment, as the aggregate frequently hides a large loss among the few players who matter most. Keep a holdout running after ship rather than closing the test, which is how the slow effect gets caught. Re-examine shipped ad changes against subsequent purchase revenue, because the back catalogue of past tests is free evidence. Require both teams to sign off on a monetisation change, which is an organisational fix and often the effective one. Flag tests where ad revenue rose and total revenue did not, as that specific pattern is the whole problem. Show the estimated substitution rate alongside the headline lift. And state plainly when a test cannot detect the effect it is most likely to cause.

## Who Feels the Pain
Publishers whose revenue per player fell after a winning test; IAP teams absorbing losses caused elsewhere; players in shortened sessions; and leadership reading two reports that disagree.

## Impact If Fixed
An experiment whose objective omits the cost it imposes will reliably report a win while destroying value, and will do so repeatedly. Reporting total revenue per player on every monetisation test is a join, not a model.
