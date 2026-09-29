# The Variance That Was a Reporting Artefact

**Niche:** [[niches/restaurant-tech-platforms/multi-unit-chain-operations/profile|Multi-Unit Chains — Making Units Comparable]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Above-store teams investigate variances one at a time by telephone, a large share of them turn out to be data problems rather than operating problems, and nobody tracks what proportion — so the same investigations recur indefinitely.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #change-point-detection #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor selling to multi-unit restaurant operators is fighting to make forty locations' numbers mean the same thing, so that an underperforming unit can be identified rather than argued about — and whoever makes units genuinely comparable takes the account.

## The Problem
A district manager's week consists of calling units about variances. Unit 12's labour is high — because a training week was not coded as training. Unit 31's food cost jumped — because an invoice was entered twice. Unit 7's item mix looks wrong — because a promotion was rung under a different item. Each call takes twenty minutes, each resolves into a data explanation, and the district manager moves on to the next. No record is kept of the cause, so the same class of artefact is investigated again next month by the same person, and the operational variances that deserve attention are buried among them.

## Why It's Still Broken
Variance investigation is conversation-based and leaves no trace. There is no field anywhere for "the cause of this variance was a double-entered invoice," so the aggregate pattern — that a large share of investigations resolve to a handful of recurring data errors — is invisible even to the person doing them. The people doing the investigating are also the people who would have to record it, at the end of a call, with no benefit to themselves.

## What a Fix Looks Like
Record the resolution and count it. Every investigated variance gets a one-tap cause from a short list — data entry, coding error, timing, genuine operational, unexplained — attached to the unit and the metric. Within a quarter the operator knows which artefacts are recurring, where, and how much district manager time they consume, which converts an invisible tax into a prioritised list of fixes. Most of the common causes are preventable at the point of entry: a duplicate invoice check, a training-hours code that cannot be skipped, a promotion mapping enforced centrally. Feed confirmed artefact patterns back into the alerting so that the next occurrence is flagged as a probable data issue before a human is dispatched, with the evidence attached.

## Who Feels the Pain
District managers spending their week on phone calls that resolve into typos; general managers defending numbers that were never about their unit; and above-store teams whose real findings are diluted by noise.

## Impact If Fixed
Coding variance causes takes seconds and typically reveals that a majority of investigations are data artefacts concentrated in a few recurring types, each individually cheap to prevent. The recovered district manager time is substantial, and the residual variances — the genuinely operational ones — finally get the attention they were always supposed to have.
