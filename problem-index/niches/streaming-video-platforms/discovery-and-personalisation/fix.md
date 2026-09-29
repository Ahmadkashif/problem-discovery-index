# The Same Forty Titles

**Niche:** [[niches/streaming-video-platforms/discovery-and-personalisation/profile|Discovery & Personalisation]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The catalogue has ten thousand titles and the subscriber is shown the same forty every week.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #matrix-decompositions #confidence-intervals #revenue-impact #automation #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to get each subscriber to the title that will keep them subscribed rather than the one they will watch tonight — and whoever optimises recommendation for retention rather than for engagement changes what the catalogue is worth.

## The Problem
Exposure is enormously concentrated. A small fraction of the catalogue receives the overwhelming majority of impressions, and a subscriber returning weekly sees largely the same rows and the same titles. The platform paid for the rest of the catalogue. Subscribers report that there is nothing to watch while sitting in front of thousands of titles they have never been shown, which is both a churn driver and a direct waste of content spend.

## Why It's Still Broken
The recommender maximises the probability of a play from the next impression, which is always served best by a safe familiar title — a system rewarded for the certain outcome will never risk the uncertain one. Exposure concentration is not reported as a metric. The unseen catalogue's cost is sunk and invisible. And "nothing to watch" is attributed to the catalogue rather than to the surfacing.

## What a Fix Looks Like
Report the concentration and force some breadth. Report what share of the catalogue receives what share of impressions, which is the fix and is one query that will be startling. Track per-subscriber exposure breadth over time, since the repetition is experienced individually and the aggregate hides it. Reserve some surface deliberately for titles outside the recommended set, as a small allocation to exploration costs little and is the only way the rest of the catalogue is ever seen. Measure what happens when subscribers do watch something outside their usual set, because the effect on retention may be positive and nobody has checked. Give new and narrow titles a guaranteed initial exposure, so the cold start does not become permanent. Report cost per impression by catalogue segment, which makes the waste financially legible. Vary the rows shown week to week, since identical presentation is what produces the complaint. Let subscribers browse the catalogue in ways that are not the recommender, as the search and browse surfaces are frequently poor. Measure the "nothing to watch" session — a long browse with no play — which is directly observable and is the clearest churn signal available. And report exposure breadth alongside engagement, so the trade is visible to the team optimising it.

## Who Feels the Pain
Subscribers who cannot find anything in a vast catalogue; content teams whose titles are never surfaced; finance teams paying for an unseen catalogue; and a business whose churn driver is a presentation problem.

## Impact If Fixed
A system rewarded for the certain outcome will never risk the uncertain one, so exposure concentrates. Reporting catalogue exposure share and the long-browse-no-play session makes both the waste and the churn signal visible immediately.
