# Reputation & Ratings

**Parent Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Category:** High Market Share
**Contested on:** Whether a freelancer's score reflects their performance or the harshness of the particular clients who happened to hire them.

## Profile
**Market Size:** ~$2.52B — 18% of platform-intermediated gross services volume
**Share of Parent Industry:** ~18%
**Digital Adoption:** High in collection, near zero in calibration — raw averages, displayed as truth
**Target Buyer:** Platform product leadership; freelancers, who bear the consequences
**Automation Potential:** High — the calibration is a well-posed statistical problem over data the platform already holds

## What Makes This a Distinct Niche

A freelancer's score is the single most consequential number attached to them. It gates ranking, tier assignment, invitation eligibility and what they can charge, and it follows them for a year or more.

It is also an average of ratings left by a small number of clients who differ enormously in how they rate. Some clients give five stars to anything delivered; others reserve five stars for work that exceeded a brief they never wrote down. A freelancer who does consistently good work for three demanding clients scores below one who does mediocre work for three generous ones, and the platform reports both numbers as though they measured the same thing.

This is a distinct niche from ranking because the object is different. Ranking is a decision the platform makes; reputation is a measurement the platform publishes and then treats as an input. The measurement error is separable, well characterised in the statistical literature on rater effects, and computable from the platform's own rating history — and essentially no marketplace corrects for it.

## Current Tools & Gaps

Platforms display raw averages, sometimes weighted by recency or contract value, sometimes bucketed into a percentage score. Several run private-feedback channels alongside public ratings to reduce retaliation, which is a genuine improvement to the collection process. A few suppress ratings from clients with disputed payment histories.

What none of them do is model the rater. Every client's ratings are treated as measurements on a common scale, when they are measurements on that client's own scale with that client's own offset and spread. The result is a score dominated by rater variance for anyone with fewer than about twenty ratings, which is most of the supply side. The correction is standard — a hierarchical model with rater effects — and its absence is the largest single piece of unclaimed statistical value in the industry.

## Problems
- [[niches/freelance-marketplaces/reputation-and-ratings/build|🔨 Build: Rater-Calibrated Reputation]]
- [[niches/freelance-marketplaces/reputation-and-ratings/buy|🛒 Buy: Review Infrastructure Adapted to a Score That Sets Income]]
- [[niches/freelance-marketplaces/reputation-and-ratings/fix|🔧 Fix: One Bad Rating That Follows Someone for a Year]]
