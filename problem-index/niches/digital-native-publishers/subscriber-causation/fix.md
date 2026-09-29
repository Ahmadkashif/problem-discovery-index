# The Last Article Takes the Credit

**Niche:** [[niches/digital-native-publishers/subscriber-causation/profile|Subscriber Causation]]
**Industry:** [[industries/digital-native-publishers|Digital Native Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** The subscription is credited to whatever article the reader happened to hit the paywall on.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #confidence-intervals #causal-inference #revenue-impact #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to identify which journalism causes a reader to become a subscriber and stay one — and whoever separates that from the articles that merely attract readers who were already going to subscribe changes where every publisher spends its editorial budget.

## The Problem
The subscription report attributes each new subscriber to the article they were reading when they converted. That article is, by construction, whichever piece happened to be the one that exceeded the free allowance — often an arbitrary, ordinary piece, systematically biased toward high-traffic content and toward whatever was published on a busy day. Editors see the list, draw conclusions about what converts, and commission accordingly.

## Why It's Still Broken
Last touch is the only attribution the subscription platform computes, so it is the number in the report — an attribution that requires no data engineering will always be the one that exists. Everyone senses it is wrong and nobody has an alternative to propose. Changing it requires joining reading history, which is a project. And the current report is not obviously absurd, which is worse than if it were.

## What a Fix Looks Like
Show the path, not the point. Report the reader's full reading history before subscribing rather than only the last article, which is the fix and is available in the same warehouse. Show the first article, the most-read beat and the tenure alongside the converting piece, since those are more informative and cost nothing extra. Report how many articles and how many days preceded the subscription, because the distribution will show immediately how misleading a single-touch view is. Flag that the converting article is largely an artefact of the paywall rule, as naming it prevents the wrong conclusion. Report by beat over the whole path, which is the actionable unit and is robust to the attribution problem. Separate subscribers who converted on their first visit from those who read for months, since they are different populations with different sources. Track retention by path type, because a subscriber acquired after months of reading behaves differently from an impulse conversion. Present the top converting beats rather than the top converting articles, as the beat-level signal survives the noise. Say plainly what the report cannot support. And commission the causal work, since decomposition is an improvement and not an answer.

## Who Feels the Pain
Editors commissioning from a misleading list; reporters whose work converts and is never credited; subscription teams defending a number they distrust; and publishers allocating budget on an artefact of a paywall rule.

## Impact If Fixed
An attribution that requires no data engineering is always the one that exists, and everyone senses it is wrong. Showing the full reading path and reporting by beat is available in the same warehouse and is robust to the problem last touch creates.
