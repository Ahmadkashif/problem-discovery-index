# Rollouts Designed to Be Unmeasurable

**Niche:** [[niches/developer-tools-vendors/productivity-attribution/profile|Productivity Attribution]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Tools are switched on for everybody at once because staging feels like withholding a benefit, which destroys the only comparison that would have answered whether the benefit was real.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #causal-inference #quick-win #workflow-orchestration #automation
**Contested on:** Every serious competitor here is fighting to attribute a change in engineering output to a specific tool or practice — and whoever does that credibly takes the category, because every purchase in it is justified by a claim nobody can currently substantiate.

## The Problem
A platform team plans an assistant rollout. Someone suggests starting with a third of the engineers to see what happens. The objection is immediate and reasonable-sounding: the tool is good, withholding it from six hundred engineers for six weeks is a cost, and the vendor's licence is already paid for everybody. So it goes to everyone on a Tuesday. Twelve months and several million dollars later, nobody can answer the renewal question, and the six weeks that would have answered it look cheap in retrospect.

## Why It's Still Broken
Staging is experienced as withholding, which is politically uncomfortable and is rarely weighed against the value of knowing. Nobody owns the evaluation — the platform team owns the rollout, finance owns the spend, and the question of whether it worked belongs to neither. The vendor prefers full deployment for obvious reasons and frequently prices to encourage it. And organisations have no template for how to do this, so it would have to be invented by someone whose job is something else.

## What a Fix Looks Like
Make staging the default and cheap. A standard rollout template: cohorts by team, sequenced over six to eight weeks, with the order randomised rather than chosen — which is the entire methodological requirement and adds no delay for the average engineer, since everyone gets it within two months either way. Baseline collection for a period before the first cohort, which is free and is usually skipped. A holdout that is small and time-boxed rather than large and indefinite, since the objection is proportional to how many people wait and for how long. Instrument the rollout order itself, so the analysis is possible afterwards even if nobody plans it now — this is the minimum and costs nothing but a recorded date per team. Pre-agree the outcome measures before the rollout starts, because choosing them afterwards guarantees a contested result. And write down the decision rule in advance: what result would lead to expanding, renegotiating or stopping, which is what converts a measurement into a decision and is almost never stated.

## Who Feels the Pain
Engineering leaders defending renewals on sentiment; finance approving large recurring spend with no evidence; and platform teams asked a year later a question they cannot answer because of a decision made in a planning meeting.

## Impact If Fixed
Randomised sequencing over a rollout that was going to be staged anyway costs nothing and is the difference between an answer and an argument. Recording the rollout order is the absolute minimum and makes retrospective analysis possible even where nobody planned for it.
