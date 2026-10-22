# The Cat Analyst in the First Week After an Event

**Industry:** [[reinsurers|Reinsurers]]
**Type:** Worker Life Changing
**One-liner:** When a major catastrophe hits, a reinsurer's cat analysts work ~14-hour days to produce a loss estimate the board, rating agencies and investors want within days, mostly by matching contracts to footprints by hand.
**Tags:** #monte-carlo-methods #bayesian-inference #time-series-forecasting #feature-engineering #worker-facing #workflow-orchestration #automation

## The Problem
A hurricane makes landfall, or a wildfire burns into a city. Within hours the reinsurer's executives want to know what it will cost the firm. Within days the number goes to the board, the rating agencies and, for listed reinsurers and sidecars, to investors. Modelling firms publish industry estimates that move as the event develops. For the January 2025 Los Angeles wildfires, Moody's RMS put insured losses at $20B–$30B and Verisk at $28B–$35B within two weeks. Industry loss indices such as PCS and PERILS follow on their own timetables.

The cat analyst's work in that week is mostly assembly. They take each vendor's event footprint or event-set selection, run it against the in-force exposure for every affected cedent, apply each treaty's terms (retention, limit, reinstatements, hours clause, cedent share), compare the result with the industry estimate scaled by each cedent's market share, and adjust for what cedents are starting to report. Contract terms live in the administration system, exposure in the modelling platform, cedent notifications in email. The estimate is rebuilt every time a vendor revises its footprint, often overnight.

## Why It Matters to the Worker
The hours are punishing and the stakes are personal. An estimate that turns out materially low becomes a reserve increase the next quarter and an awkward call with the rating agency, and the analyst who built it carries that. The judgement the role was hired for — which cedents will run worse than their market share because of where and how they write — gets squeezed into the gaps between re-runs.

The same week repeats with every large event, and the season is stacked. Hurricane season overlaps the run-up to 1 January, so a bad autumn leaves the cat team pricing renewals on top of event response.

## What a Solution Looks Like
A system that, as soon as a vendor issues a footprint, runs it against every affected cedent's exposure and treaty terms automatically. It shows the loss to each layer and contract under each vendor's view and a market-share benchmark from the industry estimate. It flags the cedents whose early notifications are running above or below that benchmark. When a footprint is revised, everything recomputes without a manual re-run. The analyst's time goes to the cedent-by-cedent adjustments and to the memo explaining the range.

## Impact If Solved
Turning the event-response week from assembly into judgement gives each analyst back most of the ~40–60 hours of re-running and reconciling a major event demands (estimate). It produces an estimate with a documented basis that can be updated in minutes when the footprint changes. That shortens the window in which management is deciding on a number nobody fully trusts.
