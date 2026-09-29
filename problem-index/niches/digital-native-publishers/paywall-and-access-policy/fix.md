# Three Articles for Everyone

**Niche:** [[niches/digital-native-publishers/paywall-and-access-policy/profile|Paywall & Access Policy]]
**Industry:** [[industries/digital-native-publishers|Digital Native Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** The eight-year reader and the first-time visitor from a search result hit the same wall on the same article.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #revenue-impact #automation #confidence-intervals #worker-facing #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to decide who sees what for free, when, and at what price — and whoever measures the readers a paywall turns away as well as the subscribers it converts optimises the whole thing rather than half of it.

## The Problem
The meter counts articles and applies the same number to everyone. A loyal reader of many years, mid-way through following a story, hits a wall and is annoyed. A first-time visitor arriving from a search result hits the same wall before reading anything and leaves with no impression of the publication at all. A reader deep in a breaking news story hits it at the worst possible moment. One rule, one number, an audience with nothing in common.

## Why It's Still Broken
The meter was implemented as a counter because that is the simplest thing to build, so segmentation requires work nobody scheduled — a rule with one parameter is easy to reason about and easy to leave alone. Segment exceptions are configured manually and rarely. Conversion is reported in aggregate, which hides the segment differences. And nobody has looked at who is hitting the wall.

## What a Fix Looks Like
Segment the obvious cases first. Report who hits the wall by tenure, source and reading frequency, which is the fix and will show immediately that the policy is wrong for several groups. Treat first-visit search and social traffic differently, since walling someone before they read anything wastes the acquisition entirely. Give loyal readers more room, because annoying a nearly-convertible reader is the most expensive mistake the policy can make. Open breaking and high-value news deliberately, as habit and reputation are worth more than a conversion on that piece. Reset or soften the meter for returning readers, since a hard permanent counter treats a lapse as a betrayal. Vary by article rather than treating all content identically, which is a straightforward rule change. Test any change rather than switching globally, as this surface supports experiments easily. Report conversions and wall-hit departures side by side, which is the metric the policy should be managed on. Let the reader see what is happening rather than presenting an abrupt block, because a stated allowance is far less alienating. And review the rule quarterly, since it is currently set once and forgotten.

## Who Feels the Pain
Loyal readers blocked mid-story; first-time visitors who never see the journalism; audience teams whose acquisition is wasted at the wall; and subscription teams optimising a rule they cannot see the cost of.

## Impact If Fixed
A rule with one parameter is easy to reason about and easy to leave alone, so the meter applies uniformly to an audience with nothing in common. Reporting who hits the wall by tenure and source shows immediately which segments the policy is wrong for.
