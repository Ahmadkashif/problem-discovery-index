# The Cohort That Looked Bad Because the Season Was Bad

**Niche:** [[niches/game-user-acquisition-firms/player-content-decomposition/profile|Player-Content Decomposition]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The source was cut for poor payback and the cohorts it delivered had simply arrived into a weak content period.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #confidence-intervals #causal-inference #data-integration #revenue-impact #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to separate what a cohort was worth from what the game did to it afterwards — and whoever separates them takes the account.

## The Problem
Sources and campaigns are evaluated on realised cohort payback. Cohorts acquired during a weak content period underperform regardless of their quality, so the sources that delivered them are judged poor and cut. The judgement is about the calendar rather than the source, it is made repeatedly, and the same sources are later rediscovered and bought again at higher prices. Nobody adjusts for when the cohort arrived.

## Why It's Still Broken
Nothing normalises for the period — comparing cohorts acquired at different times without accounting for what they met compares the content calendar and calls it a source evaluation. Content history is not in the UA reporting. The comparison is intuitively obvious. And the mistake is never detected because the cut source produces no further data.

## What a Fix Looks Like
Normalise the comparison to the period before judging any source. Compare sources within the same acquisition window rather than across windows, which is the fix and removes most of the confounding immediately. Overlay the content and event calendar on cohort performance charts, so the pattern is visible to anyone looking. Compute a period effect from all cohorts acquired in that window, which is a simple average and adjusts the comparison usefully. Re-examine sources cut during weak periods, as several are likely to have been misjudged. Hold a small always-on spend on cut sources so the decision remains reversible and testable. Report cohort payback alongside the period's average, which reframes every conversation about it. Check whether a source's apparent decline coincided with a content change. Track the period effect over time as a standing series, which is useful to product as well as UA. Share the calendar with the UA team as a matter of course, which many organisations do not do. And state the confounding explicitly in the reporting rather than leaving everyone to infer causation.

## Who Feels the Pain
UA teams cutting good sources and rebuying them dearer; media buyers judged on a calendar; product teams blamed for payback they did not see; and the acquisition budget, twice.

## Impact If Fixed
Comparing cohorts acquired at different times without accounting for what they met compares the content calendar and calls it a source evaluation. Within-window comparison and a period effect removes most of it immediately.
