# Channel-by-Channel Attrition Forecast for a Video Neighbourhood

**Niche:** [[niches/satellite-operators/video-distribution-neighbourhoods/profile|Video Distribution & Contribution]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A video operator knows its channel count and its contracts, but not which channels and which distributors will leave satellite at the next renewal, or how fast the neighbourhood's value unwinds when they do.
**Tags:** #survival-analysis #gradient-boosting #graph-theory #causal-inference #revenue-impact #feature-engineering
**Contested on:** Every serious competitor in this sub-niche is fighting to keep broadcasters and pay-TV platforms on its established video neighbourhoods as channels move to IP delivery, and whoever proves, headend by headend and channel by channel, that satellite is still the cheaper and more reliable path keeps the capacity renewal.

## The Problem
A neighbourhood's value is a network effect: channels stay because headends and dishes point there, and headends stay because the channels are there. When a large pay-TV platform moves its channel lineup to IP delivery, or a group of channels leaves, the remaining customers reassess. The operator sees the outcome at renewal, when it is too late to change terms or bundle.

## Why Nobody Has Built This
The relevant data is spread across contracts, headend registries, platform lineups and public announcements of IP migrations, and the event is rare per customer. Operators historically treated video as stable, and vendors serve playout and monitoring rather than commercial forecasting.

## What to Build
A model of the neighbourhood as a graph of channels, distributors and headends, with survival models for each contract's renewal conditioned on channel genre, distributor IP readiness, region and the departures of linked channels. Scenario runs show the revenue path if a named platform migrates, and which retention offers have changed outcomes in the past.

## Target Customer
Heads of media and video sales at GEO operators with established hot-bird or cable-neighbourhood slots.

## Impact If Built
Retention effort and pricing concentrate on the contracts whose departure would cascade, and fleet replacement decisions for video slots rest on a forecast rather than a hope.
