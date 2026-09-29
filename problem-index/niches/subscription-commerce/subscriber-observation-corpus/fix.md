# Cohort Charts Reported and Not Acted On

**Niche:** [[niches/subscription-commerce/subscriber-observation-corpus/profile|Subscriber Observation Corpus]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Fix (Pain Point)
**One-liner:** Cohort analytics are available in every subscription platform, are shown in every board pack, and connect to no decision anybody makes.
**Tags:** #evaluation-metrics #descriptive-statistics #confidence-intervals #revenue-impact #survival-analysis #worker-facing #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to use the repeated observation of the same customer against a known expectation — and whoever does that wins the category, because no other commerce model gets that view and this one throws it away.

## The Problem
The monthly pack contains a cohort retention chart. Everybody looks at it, observes that the recent cohorts are slightly worse, says something about acquisition quality, and moves on. The chart does not say which cohorts, which acquisition sources, which delivery experiences, or which product changes are responsible, because it is a chart of averages by join month. It is reported because it is the category's recognised metric, it has been in the pack for three years, and no decision has ever changed as a result of it.

## Why It's Still Broken
The chart is what the platform produces, which makes it the default artefact. It is genuinely the right high-level view and is mistaken for an analysis rather than a headline. Making it actionable requires decomposition nobody has built. And its presence in the pack satisfies the requirement to be looking at retention.

## What a Fix Looks Like
Make the cohort view lead somewhere. Decompose cohorts by acquisition source, first product, sign-up path and offer, which is available in the data and turns a single declining line into a specific finding about which source is producing subscribers who do not stay. Show the curve by delivery number rather than by month, which is where the front-loading becomes visible and is the single most useful change to the standard chart. Annotate the chart with what changed — product changes, offer changes, operational incidents — so a cohort's difference has candidate causes attached. Attach an owner and an action to every observed deterioration, so the chart produces a work item rather than a comment. Report the cohort's contribution margin rather than its retention alone, since a well-retained cohort acquired expensively is not the good news the curve suggests. Compare against the acquisition cost to give a payback view, which is the number the business actually needs. Highlight what is statistically distinguishable, since most of the month-to-month differences discussed in these meetings are noise. And replace the chart in the pack with the finding it supports, because a chart everybody looks at and nobody acts on is occupying the attention that the finding needs.

## Who Feels the Pain
Operators discussing a chart monthly for years without a decision; analysts producing it; and the subscribers whose experience it summarises without describing.

## Impact If Fixed
The chart is the right headline mistaken for an analysis, and it has produced no decision in three years. Decomposing by acquisition source and plotting by delivery number turns a single declining line into a specific, ownable finding.
