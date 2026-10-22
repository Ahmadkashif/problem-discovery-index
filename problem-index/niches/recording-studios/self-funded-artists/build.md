# An Hours Estimator Trained on the Studio's Own Projects

**Niche:** [[niches/recording-studios/self-funded-artists/profile|Self-Funded Independent Artists]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A studio owner quotes an independent band by gut feel from a phone demo, and the gap between the quote and the hours actually spent decides whether the job makes money and whether the band comes back.
**Tags:** #tacit-knowledge-ml #gradient-boosting #linear-regression #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to sell a self-funded artist a fixed price for a release-ready record and then deliver it without the hours running over, and whoever estimates a project's real hours best keeps the artist's next release.

## The Problem
An experienced owner-engineer listens to a demo, watches the band rehearse once, and can estimate how long tracking, overdubs and mixing will take: tight drummer, two days; singer who needs to comp every line, add a day per song. That estimate is tacit and often wrong in the same direction for the same reasons. Less experienced studios quote low to win the job and either overrun the artist's budget or eat the hours.

## Why Nobody Has Built This
Studios rarely record actual hours per song and phase; the booking calendar shows days, not what they were spent on. Each studio's data is small. And estimating is treated as sales skill, not as something to measure.

## What to Build
A pre-production intake that captures the demo, arrangement complexity (track counts, instrumentation), tempo-map and click readiness, a short rehearsal recording, and the band's own answers about preparation, then predicts hours per phase per song with a range, trained on the studio's logged history and pooled anonymously across studios. It produces a fixed-price quote with stated assumptions (number of vocal takes, revision rounds) so changes become explicit add-ons rather than overruns.

## Target Customer
Owner-engineers of one- to three-room independent studios whose clients are mostly self-funded.

## Impact If Built
Quotes that hold, fewer half-finished projects, and margins protected without pricing out artists who are paying from their own pockets.
