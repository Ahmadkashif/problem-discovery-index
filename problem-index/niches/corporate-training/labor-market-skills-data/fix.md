# Taxonomy Revisions Silently Rewrite History

**Niche:** [[niches/corporate-training/labor-market-skills-data/profile|Labour Market & Skills Taxonomy Data Providers]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Fix (Pain Point)
**One-liner:** A skill is split, merged, or reclassified, the archive is reprocessed under the new taxonomy, and a client's trend line moves for reasons that have nothing to do with the labour market.
**Tags:** #change-point-detection #time-series-forecasting #evaluation-metrics #hypothesis-testing #descriptive-statistics #dimensionality-reduction #data-integration #compliance #workflow-orchestration #confidence-intervals

## The Problem
The taxonomy has to change — new skills emerge, categories prove wrong, hierarchies get reorganized — and the archive is reprocessed so that history is expressed in current terms. That is the right instinct and it silently destroys comparability. A client tracking demand for a skill over five years sees a series that reflects both real market movement and every taxonomy decision made in between, with no way to separate them. When a series jumps, the account team's first question is whether something changed in the taxonomy, and answering it means asking the taxonomy team what they did and when. Meanwhile the client has already put the chart in a board deck arguing for a training investment.

## Why It's Still Broken
Reprocessing under the current taxonomy is the natural implementation and produces a clean, self-consistent dataset, which is what a data platform is built to deliver. Preserving comparability means retaining historical taxonomy versions and the mappings between them, which is real storage and engineering cost for a benefit nobody was demanding. And because the effect is invisible — a series that moves for a taxonomy reason looks exactly like one that moves for a market reason — no client has been able to identify it clearly enough to complain about it specifically.

## What a Fix Looks Like
Taxonomy versions as first-class, retained artifacts with explicit mappings between them, classified by comparability: identical, comparable with a stated adjustment, or genuinely broken. Every published series states which taxonomy version it was computed under and where breaks occur, so a client sees a discontinuity marked rather than smoothed. Where a mapping supports adjustment, the adjusted series is available alongside the raw one with the method stated. The same infrastructure supports the analysis the firm cannot currently do about itself — measuring how much of an apparent trend is attributable to taxonomy change, which is the honest answer to the account team's question and today is a matter of recollection. And clients who need stability, particularly those making multi-year commitments, can pin a taxonomy version for a series, which is a straightforward product feature that removes an entire category of dispute.

## Who Feels the Pain
Clients presenting trend evidence to their own leadership that may reflect a classification decision; account teams fielding questions about series movements they cannot explain; the taxonomy team, whose necessary improvements create downstream confusion they are then blamed for; and the firm's credibility, which rests on longitudinal claims it cannot currently guarantee.

## Impact If Fixed
Makes longitudinal analysis defensible, which is the use case that justifies a subscription rather than a one-time data purchase. It also unblocks the taxonomy team: the current implicit cost of any revision is downstream confusion, which makes improvements politically expensive, and version management removes that constraint entirely.
