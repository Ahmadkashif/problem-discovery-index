# A Critical-Path Forecast for Every Site in the Programme

**Niche:** [[niches/wireless-carriers/site-modification-permitting/profile|Site Modifications, Leasing & Permitting]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A deployment programme of thousands of site modifications is managed as a status list, when most of the delay comes from a predictable minority of sites that could be spotted on day one.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #feature-engineering #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to compress the weeks between "this site needs new radios" and "on air" — tower-owner application, structural and mount analysis, landlord consent and municipal approval inside the FCC shot clock — and whoever gets the most sites through that chain fastest takes the deployment programme.

## The Problem
A market's overlay might cover hundreds of sites. Most pass through the chain in weeks; some stall for months on a failed structural analysis, a landlord dispute, a historic district, a municipality that tolls the clock, or a tower owner backlog. Programme managers find the stalls when the status stops moving, too late to re-sequence crews and radios.

## Why Nobody Has Built This
Programme data is spread across the carrier, tower owners, engineering firms and municipalities, each with its own system. Trackers record status; nobody models duration. Each programme is treated as new, though the same towers and towns recur.

## What to Build
A time-to-on-air model per site using tower owner, structure type and age, prior structural results, lease amendment history, jurisdiction track record on shot clocks and tolling, zoning flags and crew availability. It updates as steps complete, ranks sites by expected delay, recommends re-sequencing, and drafts the next document for each stalled step.

## Target Customer
Site development leaders at carriers, and the turf vendors and site acquisition firms running programmes for them.

## Impact If Built
Radios and crews go to sites that are ready, stalls are attacked early, and programmes finish weeks sooner (estimate), which matters when spectrum buildout conditions and FWA capacity depend on them.
