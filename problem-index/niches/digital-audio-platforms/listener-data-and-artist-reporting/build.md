# Reporting That Supports a Decision

**Niche:** [[niches/digital-audio-platforms/listener-data-and-artist-reporting/profile|Listener Data & Artist Reporting]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform knows where every listener stopped listening and tells the artist how many there were.
**Tags:** #descriptive-statistics #survival-analysis #k-means-clustering #evaluation-metrics #confidence-intervals #gradient-boosting #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn the most detailed record of listening behaviour ever assembled into something an artist can act on — and whoever reports usefully gives artists the decisions they are currently making blind.

## The Problem
The behavioural record is extraordinary: every play, skip, save, repeat, share and abandonment, with position, context and sequence. The artist's view of it is a stream count, a listener count, a territory map and a demographic split. An artist deciding what to release, where to play, which track to push or whether their audience is building has none of the information that would inform any of those, and is making expensive decisions on intuition while the answer sits in a log.

## Why Nobody Has Built This
Artist reporting was built as a courtesy surface rather than as a product, so it shows the metrics that are easy to aggregate — a dashboard provided as a relationship gesture does not develop a point of view. The artist is not the customer. Detailed behavioural reporting raises listener privacy questions that need handling rather than avoiding. And nobody asked artists what decisions they were trying to make.

## What to Build
Report the behaviour, not the count. Surface skip behaviour by position, which is the core and is the most direct feedback about the music that exists — where listeners stop is a fact about the recording and artists have never seen it. Report audience retention across releases, since a returning audience and a fresh one are completely different assets and look identical in listener counts. Distinguish a growing audience from a churning one, which is the single most consequential distinction for an artist's planning. Report save and repeat behaviour, as those are intent signals far stronger than a play. Name the cities worth playing with enough granularity to route a tour, since that is the highest-value decision the data supports. Show which track is outperforming its promotion, which is directly actionable and common. Compare against similar artists at the same stage, which is the platform's unique aggregate and is absent. Interpret rather than display, because the audience is not analytical and the current product assumes otherwise. Handle listener privacy explicitly with aggregation thresholds, as the detail must not identify individuals. And ask artists which decisions they are making, since the product was designed without doing so.

## Target Customer
Artist services leadership, artists and their managers, labels, and music analytics vendors.

## Impact If Built
A dashboard provided as a relationship gesture does not develop a point of view, so it shows what is easy to aggregate. Skip position and cross-release retention are the two facts artists most need and have never been shown.
