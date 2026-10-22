# Live Earnings and Recoupment Estimates for Each Writer

**Niche:** [[niches/music-publishers/the-signed-songwriter/profile|The Signed Songwriter]]
**Industry:** [[industries/music-publishers|Music Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A writer can watch a co-write climb the charts and still not know for a year what it is worth to them or when their advance will recoup.
**Tags:** #time-series-forecasting #bayesian-inference #confidence-intervals #feature-engineering #worker-facing #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to show a signed writer what their songs are earning and when the advance will recoup, sooner and more believably than rival publishers, and whoever does that keeps the writer when the option comes up.

## The Problem
Royalties pass through several societies and sub-publishers, each with its own lag, before reaching the writer's statement. The publisher has usage data as it happens but turns it into money only when statements arrive.

## Why Nobody Has Built This
The forecast has to apply each writer's shares and deal terms (co-publishing split, recoupment, controlled rates) and each society's conversion and lag, and publishers have been wary of showing estimates that might prove wrong.

## What to Build
A model that converts streaming, airplay and sync usage into expected writer income by source, period and territory, with ranges. It projects the arrival date for each income stream and the recoupment date for the advance, and when the statement lands it reconciles the estimate with an explanation of any gap.

## Target Customer
Creative and writer-relations heads at publishers competing for writers.

## Impact If Built
Writers can plan their finances and find their own missing registrations. Publishers gain a retention tool at option time that does not cost a bigger advance.
